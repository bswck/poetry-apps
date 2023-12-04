
# poetry-pipx [![Package version](https://img.shields.io/pypi/v/poetry-pipx?label=PyPI)](https://pypi.org/project/poetry-pipx/) [![Supported Python versions](https://img.shields.io/pypi/pyversions/poetry-pipx.svg?logo=python&label=Python)](https://pypi.org/project/poetry-pipx/)
[![Tests](https://github.com/bswck/poetry-pipx/actions/workflows/test.yml/badge.svg)](https://github.com/bswck/poetry-pipx/actions/workflows/test.yml)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/bswck/poetry-pipx.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/bswck/poetry-pipx)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg?label=Code%20style)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/bswck/poetry-pipx.svg?label=License)](https://github.com/bswck/poetry-pipx/blob/HEAD/LICENSE)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A [Poetry](https://python-poetry.org/) plugin that allows [pipx](https://github.com/pypa/pipx#readme) to take precedence when installing CLI dependencies.

# Installation
If you want to…



## …use this tool in your project 💻
```shell
poetry self add poetry-pipx
```

## …contribute to [poetry-pipx](https://github.com/bswck/poetry-pipx) 🚀


> [!Note]
> If you use Windows, it is highly recommended to complete the installation in the way presented below through [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install).



1.  Fork the [poetry-pipx repository](https://github.com/bswck/poetry-pipx) on GitHub.

1.  [Install Poetry](https://python-poetry.org/docs/#installation).<br/>
    Poetry is an amazing tool for managing dependencies & virtual environments, building packages and publishing them.
    You might use [pipx](https://github.com/pypa/pipx#readme) to install it globally (recommended):

    ```shell
    pipx install poetry
    ```

    <sub>If you encounter any problems, refer to [the official documentation](https://python-poetry.org/docs/#installation) for the most up-to-date installation instructions.</sub>

    If you want to use pipx to install dev dependencies as well, install the [export plugin](https://github.com/python-poetry/poetry-plugin-export#readme):
    ```shell
    pipx inject poetry poetry-plugin-export poetry-pipx
    ```

    Be sure to have Python 3.8 installed—if you use [pyenv](https://github.com/pyenv/pyenv#readme), simply run:

    ```shell
    pyenv install 3.8
    ```

1.  Clone your fork locally and install dependencies.

    ```shell
    git clone https://github.com/your-username/poetry-pipx path/to/poetry-pipx
    cd path/to/poetry-pipx
    poetry env use $(cat .python-version)
    ```

    If you use pipx, run the following command to install dev dependencies globally:
    ```shell
    poetry install --without=dev
    poetry pipx install dev
    ```
    Otherwise, run:

    ```shell
    poetry install
    ```
    Next up, simply activate the virtual environment and install pre-commit hooks:

    ```shell
    poetry shell
    pre-commit install --hook-type pre-commit --hook-type pre-push
    ```

For more information on how to contribute, check out [CONTRIBUTING.md](https://github.com/bswck/poetry-pipx/blob/HEAD/CONTRIBUTING.md).<br/>
Always happy to accept contributions! ❤️


# Legal info
© Copyright by Bartosz Sławecki ([@bswck](https://github.com/bswck)).
<br />This software is licensed under the terms of [MIT License](https://github.com/bswck/poetry-pipx/blob/HEAD/LICENSE).
