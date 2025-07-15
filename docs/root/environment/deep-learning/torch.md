This guide walks you through setting up PyTorch in a Python project using `poetry`, `uv`, or plain `requirements.txt`.

## 🔍 Checking for Compatible PyTorch Versions

PyTorch provides different versions for CPU and CUDA-enabled GPUs. To find the correct package index for your system, visit:

- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}

## 📋 Before You Begin

You should be comfortable with at least one dependency management tool below.
If not, stick with `requirements.txt` for a simpler setup.

- **[Poetry](https://python-poetry.org){:target="_blank" rel="noopener noreferrer"}** – Python dependency and packaging manager.

- **[uv](https://docs.astral.sh/uv/){:target="_blank" rel="noopener noreferrer"}** – Fast alternative to pip + virtualenv.

## 🛠️ Setup

Choose the appropriate configuration below (CPU or GPU) and update your `pyproject.toml` or `requirements.txt` accordingly.

### CPU Configuration

This configuration installs a version of PyTorch optimized for CPU-only systems.

=== "requirements.txt"

    ```bash title="Terminal"
    pip install torch --index-url https://download.pytorch.org/whl/cpu
    pip install torchvision --index-url https://download.pytorch.org/whl/cpu
    pip install torchaudio --index-url https://download.pytorch.org/whl/cpu

    # OR

    # Install all PyTorch packages in a single command
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ```

    ```txt title="requirements.txt"
    --extra-index-url https://download.pytorch.org/whl/cpu
    torch
    torchvision
    torchaudio
    ```

=== "poetry" 

    ```bash title="Terminal"
    # Add Source First
    poetry source add --priority=explicit pytorch-cpu https://download.pytorch.org/whl/cpu

    poetry add torch --source pytorch-cpu
    poetry add torchvision --source pytorch-cpu
    poetry add torchaudio --source pytorch-cpu
    ```

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "torch>=2.2.0",
        "torchvision>=0.17.0",
        "torchaudio>=2.2.0"
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

=== "uv" 

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "torch>=2.2.0",
        "torchvision>=0.17.0",
        "torchaudio>=2.2.0"
    ]

    [[tool.uv.index]]
    name = "pytorch-cpu"
    url = "https://download.pytorch.org/whl/cpu"
    explicit = true

    [tool.uv.sources]
    torch = {index = "pytorch-cpu"}
    torchvision = {index = "pytorch-cpu"}
    torchaudio = {index = "pytorch-cpu"}
    ```

### GPU Configuration

This configuration installs a version of PyTorch optimized for NVIDIA GPUs with CUDA 12.1 support (`cu121`). 

=== "requirements.txt"

    ```bash title="Terminal"
    pip install torch --index-url https://download.pytorch.org/whl/cu121
    pip install torchvision --index-url https://download.pytorch.org/whl/cu121
    pip install torchaudio --index-url https://download.pytorch.org/whl/cu121

    # OR

    # Install all PyTorch packages in a single command
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    ```

    ```txt title="requirements.txt"
    --extra-index-url https://download.pytorch.org/whl/cu121
    torch
    torchvision
    torchaudio
    ```

=== "poetry" 

    ```bash title="Terminal"
    # Add Source First
    poetry source add --priority=explicit pytorch-cu https://download.pytorch.org/whl/cu121

    poetry add torch --source pytorch-cu
    poetry add torchvision --source pytorch-cu
    poetry add torchaudio --source pytorch-cu
    ```

    ```toml title="pyproject.toml"
    [project]
    name = "project-name"
    version = "0.1.0"
    requires-python = ">=3.11,<3.12"
    dependencies = [
        "torch>=2.2.0",
        "torchvision>=0.17.0",
        "torchaudio>=2.2.0"
    ]

    [[tool.poetry.source]]
    name = "pytorch-cu"
    url = "https://download.pytorch.org/whl/cu121"
    priority = "explicit"

    [tool.poetry.dependencies]
    torch = {source = "pytorch-cu"}
    torchvision = {source = "pytorch-cu"}
    torchaudio = {source = "pytorch-cu"}

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
        "torch>=2.2.0",
        "torchvision>=0.17.0",
        "torchaudio>=2.2.0"
    ]

    [[tool.uv.index]]
    name = "pytorch-cu"
    url = "https://download.pytorch.org/whl/cu121"
    explicit = true

    [tool.uv.sources]
    torch = {index = "pytorch-cu"}
    torchvision = {index = "pytorch-cu"}
    torchaudio = {index = "pytorch-cu"}
    ```

???+ Warning "NumPy Compatibility"
    - NumPy 2.0 may cause compatibility issues with older PyTorch & Python. If you experience problems, try specifying one of these NumPy versions in your dependencies:
        - `numpy = "1.26.4"` 
        - `numpy = "1.26.3"`

???+ Note
    - If you need a different CUDA version (e.g., CUDA 11.8 or 12.0), update the `url` in the GPU configuration by checking the official [PyTorch Index](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}.
    - Always ensure your Python version is compatible with the PyTorch release you are installing.