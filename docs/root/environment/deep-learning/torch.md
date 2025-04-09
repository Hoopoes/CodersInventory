This guide walks you through setting up PyTorch in a Poetry-managed Python project.

## 🔍 Checking for Compatible PyTorch Versions

PyTorch provides different versions for CPU and CUDA-enabled GPUs. To find the correct package index for your system, visit:

- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}

## 📋 Prerequisites

Before setting up this project, ensure you have a basic understanding of the following tools:

- **[Poetry](https://python-poetry.org){:target="_blank" rel="noopener noreferrer"}**: A dependency management tool (similar to npm for Node.js).

## 🛠️ Setup

Based on your hardware, update your `pyproject.toml` file with the appropriate configuration.

=== "CPU Configuration" 

    This configuration installs a version of PyTorch optimized for CPU usage.


    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "torch (>=2.2.0)",
        "torchvision (>=0.17.0)",
        "torchaudio (>=2.2.0)"
    ]

    [[tool.poetry.source]]
    name = "pytorch-cpu"
    url = "https://download.pytorch.org/whl/cpu"
    priority = "explicit"

    [tool.poetry.dependencies]
    torch = {source = "pytorch-cpu"}
    torchvision = {source = "pytorch-cpu"}
    torchaudio = {source = "pytorch-cpu"}

    [tool.poetry]
    package-mode = false

    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```

=== "GPU Configuration" 

    This configuration is optimized for NVIDIA GPUs with CUDA support (CUDA 12.1).


    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "torch (>=2.2.0)",
        "torchvision (>=0.17.0)",
        "torchaudio (>=2.2.0)"
    ]

    [[tool.poetry.source]]
    name = "pytorch-cu121"
    url = "https://download.pytorch.org/whl/cu121"
    priority = "explicit"

    [tool.poetry.dependencies]
    torch = {source = "pytorch-cu121"}
    torchvision = {source = "pytorch-cu121"}
    torchaudio = {source = "pytorch-cu121"}

    [tool.poetry]
    package-mode = false

    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
    ```

???+ Warning
    - NumPy 2.0 may cause compatibility issues with older PyTorch & Python. If you experience problems, try specifying one of these NumPy versions in your dependencies:
        - `numpy = "1.26.4"` 
        - `numpy = "1.26.3"`

???+ Note
    - If you need a different CUDA version (e.g., CUDA 11.8 or 12.0), update the `url` in the GPU configuration by checking the official [PyTorch Index](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}.
    - Always ensure your Python version is compatible with the PyTorch release you are installing.