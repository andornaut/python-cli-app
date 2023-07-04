# Python CLI App

Project scaffolding to develop Command Line Interface (CLI) applications using Python.

* [andornaut@github /python-exercises](https://github.com/andornaut/python-exercises)
* [andornaut@github /til/python](https://github.com/andornaut/til/blob/master/docs/python.md)

## Getting Started

*Environment:*

* Operating system: Ubuntu 22.04
* Python interpreter: Python 3.10

1. Install python3 using [Ansible](https://www.ansible.com/) and
[ansible-ctrl/roles/dev](https://github.com/andornaut/ansible-ctrl/blob/master/roles/dev/tasks/python.yml)

1. Install application and development dependencies into a virtualenv

   ```bash
   pipenv install --dev
   ```

1. Activate the virtualenv

   ```bash
   pipenv shell
   python --version
   > Python 3.10.6
   ```

1. Run a command

   ```bash
   # Run as a Python module
   python -m cliapp
   python -m cliapp hello --name andornaut

   # Run as a CLI application
   cliapp --version
   > cliapp v0.1.0
   ```

## Dependencies

Name | Description
--- | ---
[black](https://github.com/psf/black) | The uncompromising Python code formatter
[pytest](https://docs.pytest.org/en/) | A framework that makes it easy to write small, readable tests
[Typer](https://github.com/tiangolo/typer) | Build great CLIs. Easy to code. Based on Python type hints.

## Developing

See [.vscode](./.vscode) for [VS Code](https://code.visualstudio.com/) integration files.

```bash
# Format Python files
black .

# Check code style
flake8

# Run tests
pytest

# Run only tests whose names contain "version"
pytest -k version
```
