# koneoppiminen

Datan käsittely ja koneoppiminen kurssi

## Setup

- Install [Python 3.11](https://www.python.org/downloads/).

- Create a virtual environment.
  - Using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

    - ```bash
      conda env create
      ```

      - Activate the conda environment.

      - ```bash
        conda activate koneoppiminen-env
        ```

- Install required python packages. (using [poetry](https://python-poetry.org/)) the packages are defined in the [pyproject.toml](./pyproject.toml) file.

```bash
poetry install
```

## Making changes

- Adding new packages
**Add the new packages to the [pyproject.toml](./pyproject.toml) file.**
After adding the packages run

```bash
poetry lock
```

```bash
poetry install
```
