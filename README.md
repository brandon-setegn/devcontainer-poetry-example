# devcontainer-poetry-example
This is an example project using VS Code and Devcontainers to build a Python Poetry project.

[Poetry - Python Dependency Manager](https://python-poetry.org/)

[VS Code - Devolping inside a Container](https://code.visualstudio.com/docs/remote/containers)


## Creating a Poetry Project
1. First make sure you have Python installed correctly.
2. Install the Poetry package - https://python-poetry.org/docs/#installation
3. In the directory you want to create the package in run `poetry new hello-world`

## Adding devcontainer to the project
1. Navigate to the folder you created the project in (ex: `\hello-world`)
2. Create a folder for devcontainer config: `\hello-world\.devcontainer`
3. Add files `devcontainer.json` and `Dockerfile`
4. Copy contents from this repository to their respective .devcontainer files

## Reopen Project in VS Code as devcontainer
