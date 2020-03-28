"""Entry point for the lookup server."""

import socket
from threading import Event, Thread

from plover import log
from plover.engine import StenoEngine


LOG_PREFIX = "plover_dictionary_lookup:"
BUFFER_SIZE = 1024
CONNECTION_LIMIT = 5
ENCODING = "utf-8"
HOST = "127.0.0.1"  # TODO: Make this configuration
PORT = 1245  # TODO: Make this configuration


class LookupServer(Thread):
    """Server to look up dictionary entries over TCP sockets."""

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()
        log.info(f"{LOG_PREFIX} initializing")

        self._engine = engine
        self._stop_event = Event()

    def start(self) -> None:
        """Called to start the server."""
        log.info(f"{LOG_PREFIX} starting")
        super().start()

    def stop(self) -> None:
        """Called to stop the server."""
        log.info(f"{LOG_PREFIX} stopping")
        self._stop_event.set()

    def run(self) -> None:
        """Main server loop."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind((HOST, PORT))
        server_socket.listen(CONNECTION_LIMIT)

        while not self._stop_event.is_set():
            connection, address = server_socket.accept()

            with connection:
                log.info(f"{LOG_PREFIX} connection from {address}")

                # TODO: Should support pulling longer / segmented mesages
                word = connection.recv(BUFFER_SIZE).decode(ENCODING)
                if not word:
                    break

                matches = self._engine.reverse_lookup(word)

                log.info(
                    f"{LOG_PREFIX} request from {address} for {word}, found {matches}"
                )

                matches_as_bytes = str.encode(str(matches), ENCODING)
                connection.sendall(matches_as_bytes)

        server_socket.close()
