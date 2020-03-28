# Plover Dictionary Lookup

External dictionary lookup extension for [Plover](https://github.com/openstenoproject/plover).

This code is meant to serve as a basic example for external communication with Plover's engine.

## How to Use

After installing, enable the plugin in the Plover Configure -> Plugins menu. For writing a client, just look at plover_dictionary_lookup.client or server for now.

## Development

Update README.rst with [pandoc](https://pandoc.org/):

```bash
pandoc README.md -o README.rst
```

Install dependencies with [pipenv](https://github.com/pypa/pipenv):

```bash
pipenv install --dev
```

Test with the example client:

```bash
pipenv run python -m plover_dictionary_lookup.client
```

Build and publish to PyPI with [twine](https://twine.readthedocs.io/en/latest/):

```bash
pipenv run python setup.py sdist bdist_wheel
pipenv run twine upload dist/*
```
