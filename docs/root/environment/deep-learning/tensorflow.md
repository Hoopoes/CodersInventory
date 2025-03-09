This guide walks you through setting up TensorFlow in a Poetry-managed Python project.

## 🔍 Checking for Compatible TensorFlow Versions

To ensure compatibility with your system's configuration, visit:

- [TensorFlow Installation Guide](https://www.tensorflow.org/install){:target="_blank" rel="noopener noreferrer"}.

## 📋 Prerequisites

Before setting up this project, ensure you have a basic understanding of the following tools:

- **[Poetry](https://python-poetry.org){:target="_blank" rel="noopener noreferrer"}**: A dependency management tool (similar to npm for Node.js).

## 🛠️ Setup

Based on your hardware, update your `pyproject.toml` file with the appropriate configuration.

### CPU Configuration `(pyproject.toml)` on Windows/Linux

This configuration installs a version of Tensorflow optimized for CPU usage.

```toml
[tool.poetry]
name = "project-name"
version = "0.1.0"
description = ""
authors = ["author-name <author-email>"]
readme = "README.md"
package-mode = false

[tool.poetry.dependencies]
python = ">=3.11,<3.12"
tensorflow = "^2.18.0"
tf-keras = "^2.18.0"
tensorflow-io-gcs-filesystem = "^0.31.0"
tensorflow-intel = {version = "^2.18.0", markers = "sys_platform != 'linux'"}

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
???+ Warning
    - TensorFlow no longer supports GPU acceleration on Windows.

???+ Note    
    - The configuration above is set up for Python versions between 3.11 (inclusive) and 3.12 (exclusive). Adjust the Python version in your `pyproject.toml` file if your project uses a different version.
    - For any issues related to version compatibility or performance, double-check your system’s drivers and ensure all dependencies are up-to-date.

## 🚀 Future Updates

Guidance for configuring TensorFlow with GPU support on Linux is forthcoming. Stay tuned for updates.
In the meantime, you can refer to the official [TensorFlow Installation Guide](https://www.tensorflow.org/install/pip){:target="_blank" rel="noopener noreferrer"} for the latest information.