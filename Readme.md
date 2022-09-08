# clive-owen

![Clive Owen](docs/img/clive.jpg)

A simple one-file CLI package. Demonstrates the following:

* How to implement a simple command line utility with Click, in a single .py file
* How to create a `setup.py` file alongside the CLI utility, for a bare-minimum installation
* How to implement git pre-commit hooks with [pre-commit](https://pre-commit.com/)

## Screenshot

Screenshot of pre-commit hooks in action:

![Screenshot of pre-commit hooks in action](docs/img/ss.png)


## Quick start

```
git clone git@github.com:charlesreid1-toy-factory/clive-owen.git
cd clive-owen

# Start a virtual environment if you wish

pip install -r requirements.txt
pip install --editable .
clive --help
```

And to install the pre-commit hooks:

```
pre-commit install
```
