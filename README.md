# devcontainer-poetry-example
This is an example project using VS Code and Devcontainers to build a Python Poetry project.

[Poetry - Python Dependency Manager](https://python-poetry.org/)

[VS Code - Devolping inside a Container](https://code.visualstudio.com/docs/remote/containers)

## Running this Project
If you have VS Code and Docker installed correctly you should be able to run this project very easily. There is only 1 thing left to do:
1. Add file `.env` to the `/hello-world/.devcontainer` folder.  This file can be empty but needs to exist.  This is where we will put any environment variables that are required.  DO NOT check your .env into git.

#### Here is a list of steps I used to create this project.

## Creating a Poetry Project
1. First make sure you have Python installed correctly.
2. Install the Poetry package - https://python-poetry.org/docs/#installation
3. In the directory you want to create the package in run `poetry new hello-world`

## Adding devcontainer to the project
1. Navigate to the folder you created the project in (ex: `/hello-world`)
2. Create a folder for devcontainer config: `\hello-world\.devcontainer`
3. Add files `devcontainer.json` and `Dockerfile`
4. Copy contents from this repository to their respective .devcontainer files
5. Add file `.env` to the `/hello-world/.devcontainer` folder.  This file can be empty but needs to exist.  This is where we will put any environment variables that are required.  DO NOT check your .env into git.

## Reopen Project in VS Code as devcontainer
1. Inside VS Code open the Command Pallete with `CTRL + SHIFT + P`
2. Run the command `>Remote-Containers: Open Folder in Container`
3. Select the folder containing the `.devcontainer` folder (ex: `\hello-world\.devcontainer`) 
4. The project should be up and running now.  Try running tests to make sure.
