This guide walks you through setting up PaddlePaddle in a Python project using `poetry`, `uv`, or plain `requirements.txt`.

## 🔍 Checking for Compatible PaddlePaddle Versions

PaddlePaddle provides separate builds for CPU and CUDA-enabled GPUs. To find the correct installation index for your system, visit:

* [PaddlePaddle Installation Guide](https://www.paddlepaddle.org.cn/en/install/quick){:target="_blank" rel="noopener noreferrer"}

## 📋 Before You Begin

You should be comfortable with at least one dependency management tool below.
If not, stick with `requirements.txt` for a simpler setup.

* **[Poetry](https://python-poetry.org){:target="_blank" rel="noopener noreferrer"}** – Python dependency and packaging manager.
* **[uv](https://docs.astral.sh/uv/){:target="_blank" rel="noopener noreferrer"}** – Fast alternative to pip + virtualenv.

## 🛠️ Setup

Choose the appropriate configuration below (CPU or GPU) and update your `pyproject.toml` or `requirements.txt` accordingly.

### CPU Configuration

This configuration installs the CPU-only PaddlePaddle.

=== "requirements.txt"

    ```bash title="Terminal"
    python -m pip install paddlepaddle==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
    ```

    ```txt title="requirements.txt"
    --extra-index-url https://www.paddlepaddle.org.cn/packages/stable/cpu/
    paddlepaddle==3.1.0
    ```

=== "poetry"

    ```bash title="Terminal"
    # Add Source First
    poetry source add --priority=explicit paddle-cpu https://www.paddlepaddle.org.cn/packages/stable/cpu/

    poetry add paddlepaddle==3.1.0 --source paddle-cpu
    ```

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "paddlepaddle==3.1.0"
    ]

    [[tool.poetry.source]]
    name = "paddle-cpu"
    url = "https://www.paddlepaddle.org.cn/packages/stable/cpu/"
    priority = "explicit"

    [tool.poetry.dependencies]
    paddlepaddle = {source = "paddle-cpu"}

    [tool.poetry]
    package-mode = false

    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```

=== "uv"

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "paddlepaddle==3.1.0"
    ]

    [[tool.uv.index]]
    name = "paddlepaddle-cpu"
    url = "https://www.paddlepaddle.org.cn/packages/stable/cpu/"
    explicit = true

    [tool.uv.sources]
    paddlepaddle = {index = "paddlepaddle-cpu"}
    ```


### GPU Configuration

This configuration installs a version of PaddlePaddle optimized for NVIDIA GPUs with CUDA 12.6 support (`cu126`).

=== "requirements.txt"


    ```bash title="Terminal"
    python -m pip install paddlepaddle-gpu==3.1.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
    ```

    ```txt title="requirements.txt"
    --extra-index-url https://www.paddlepaddle.org.cn/packages/stable/cu126/
    paddlepaddle-gpu==3.1.0
    ```


=== "poetry"

    ```bash title="Terminal"
    # Add Source First
    poetry source add --priority=explicit paddle-cu https://www.paddlepaddle.org.cn/packages/stable/cu126/

    poetry add paddlepaddle-gpu==3.1.0 --source paddle-cu
    ```

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "paddlepaddle-gpu==3.1.0"
    ]

    [[tool.poetry.source]]
    name = "paddle-cu"
    url = "https://www.paddlepaddle.org.cn/packages/stable/cu126/"
    priority = "explicit"

    [tool.poetry.dependencies]
    paddlepaddle-gpu = {source = "paddle-cu"}

    [tool.poetry]
    package-mode = false

    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```

=== "uv"

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "paddlepaddle-gpu==3.1.0"
    ]

    [[tool.uv.index]]
    name = "paddlepaddle-cu"
    url = "https://www.paddlepaddle.org.cn/packages/stable/cu126/"
    explicit = true

    [tool.uv.sources]
    paddlepaddle-gpu = {index = "paddlepaddle-cu"}
    ```




???+ Note
    - If you need a different CUDA version (e.g., CUDA 11.8 or 12.9), update the GPU index URL accordingly by checking the official PaddlePaddle install instructions. [PaddlePaddle Index](https://www.paddlepaddle.org.cn/en/install/quick){:target="_blank" rel="noopener noreferrer"}
    - Always ensure your Python version is compatible with the PaddlePaddle release you are installing.
