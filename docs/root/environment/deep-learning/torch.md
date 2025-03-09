This guide walks you through setting up PyTorch in a Poetry-managed Python project.

## 🔍 Checking for Compatible PyTorch Versions

PyTorch provides different versions for CPU and CUDA-enabled GPUs. To find the correct package index for your system, visit:

- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}

## 📋 Prerequisites

Before setting up this project, ensure you have a basic understanding of the following tools:

- **[Poetry](https://python-poetry.org){:target="_blank" rel="noopener noreferrer"}**: A dependency management tool (similar to npm for Node.js).

## 🛠️ Setup

Based on your hardware, update your `pyproject.toml` file with the appropriate configuration.

### CPU Configuration `(pyproject.toml)`

This configuration installs a version of PyTorch optimized for CPU usage.


```toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = ""
authors = ["author-name <author-email>"]
readme = "README.md"
package-mode = false

[[tool.poetry.source]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
priority = "explicit"

[tool.poetry.dependencies]
python = ">=3.11,<3.12"
torch = {version = "^2.2.0+cpu", source = "pytorch-cpu"}
torchvision = {version = "^0.17.0+cpu", source = "pytorch-cpu"}
torchaudio = {version = "^2.2.0+cpu", source = "pytorch-cpu"}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### GPU Configuration `(pyproject.toml)`

This configuration is optimized for NVIDIA GPUs with CUDA support (CUDA 12.1).


```toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = ""
authors = ["author-name <author-email>"]
readme = "README.md"
package-mode = false


[[tool.poetry.source]]
name = "pytorch-cu"
url = "https://download.pytorch.org/whl/cu121"
priority = "explicit"


[tool.poetry.dependencies]
python = ">=3.11,<3.12"
torch = {version = "^2.2.0+cu121", source = "pytorch-cu"}
torchvision = {version = "^0.17.0+cu121", source = "pytorch-cu"}
torchaudio = {version = "^2.2.0+cu121", source = "pytorch-cu"}


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

???+ Warning
    - NumPy 2.0 may cause compatibility issues with older PyTorch models. If you experience problems, try specifying one of these NumPy versions in your dependencies:
        - `numpy = "^1.26.4"` 
        - `numpy = "^1.26.3"`

???+ Note
    - If you need a different CUDA version (e.g., CUDA 11.8 or 12.0), update the `url` in the GPU configuration by checking the official [PyTorch Index](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}.
    - Always ensure your Python version is compatible with the PyTorch release you are installing.