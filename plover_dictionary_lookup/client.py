"""An example client for the lookup server."""

import socket

from plover_dictionary_lookup.server import BUFFER_SIZE, ENCODING, HOST, PORT


def main() -> None:
    """Client logic."""
    word = "hello"
    matches = ""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        word_as_bytes = str.encode(str(word), ENCODING)
        client_socket.sendall(word_as_bytes)

        matches = client_socket.recv(BUFFER_SIZE).decode(ENCODING)

    print(f"{word}: {matches}")


if __name__ == "__main__":
    main()
