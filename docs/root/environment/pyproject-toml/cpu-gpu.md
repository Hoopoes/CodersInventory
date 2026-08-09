## ⚡ UV

### Optional CPU & GPU

This configuration exposes both `cpu` and `gpu` as optional extras.

#### TOML

```toml title="pyproject.toml"
[project]
name = "test-toml"
version = "0.1.0"
requires-python = ">=3.12,<3.13"
dependencies = []

[project.optional-dependencies]
cpu = [
  "torch",
]
gpu = [
  "torch",
]

[tool.uv]
conflicts = [
    [ 
      { extra = "cpu" }, 
      { extra = "gpu" } 
    ]
]

[tool.uv.sources]
torch = [
  { index = "torch-cpu", extra = "cpu" },
  { index = "torch-gpu", extra = "gpu" },
]

[[tool.uv.index]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"

[[tool.uv.index]]
name = "torch-gpu"
url = "https://download.pytorch.org/whl/cu126"
```

#### Command
Install without either extra:
```
uv sync
```

Install the CPU version:

```
uv sync --extra cpu
```

Install the GPU version:
```
uv sync --extra gpu
```

You can also use `uv pip`:

```
uv pip install -r pyproject.toml
```
```
uv pip install -r pyproject.toml --extra cpu
```
```
uv pip install -r pyproject.toml --extra gpu
```

If the installation does not select the expected package from the configured index, try:

```
uv pip install -r pyproject.toml --extra gpu --index-strategy unsafe-best-match
```


## 📦 Poetry

### Optional CPU & GPU

This configuration exposes both `cpu` and `gpu` as optional extras.

#### TOML

```toml title="pyproject.toml"
[project]
name = "test-toml"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
cpu = [
    "torch (==2.2.0+cpu)",
]
gpu = [
    "torch (==2.5.1+cu121)",
]

[tool.poetry.dependencies]
torch = [
    { markers = "extra != 'gpu' and extra == 'cpu'", source = "torch-cpu" },
    { markers = "extra == 'gpu' and extra != 'cpu'", source = "torch-gpu" },
]

[[tool.poetry.source]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"
priority = "explicit"
[[tool.poetry.source]]
name = "torch-gpu"
url = "https://download.pytorch.org/whl/cu121"
priority = "explicit"


[tool.poetry]
package-mode = false
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```


#### Command
Install without either extra:
```
poetry install
```

Install the CPU version:
```
poetry install --extras cpu
```

Install the GPU version:
```
poetry install --extras gpu
```

The mutually exclusive markers are:

`markers = "extra != 'gpu' and extra == 'cpu'"`

for CPU, and:

`markers = "extra == 'gpu' and extra != 'cpu'"`

for GPU.

This ensures that selecting cpu activates only the CPU dependency, while selecting gpu activates only the GPU dependency.

### Default CPU, Optional GPU

This configuration installs the CPU version of PyTorch by default. The GPU version can be selected using the `gpu` extra.

#### TOML

```toml title="pyproject.toml"
[project]
name = "test-toml"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "torch (==2.2.0+cpu) ; extra != 'gpu'",
]

[project.optional-dependencies]
gpu = [
    "torch (==2.5.1+cu121)",
]

[tool.poetry.dependencies]
torch = [
    { markers = "extra != 'gpu'", source = "torch-cpu" },
    { markers = "extra == 'gpu'", source = "torch-gpu" },
]

[[tool.poetry.source]]
name = "torch-cpu"
url = "https://download.pytorch.org/whl/cpu"
priority = "explicit"
[[tool.poetry.source]]
name = "torch-gpu"
url = "https://download.pytorch.org/whl/cu121"
priority = "explicit"


[tool.poetry]
package-mode = false
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

#### Command
Poetry needs re-resolution disabled for this setup:
```
poetry config installer.re-resolve false
```

Install the default CPU configuration:
```
poetry install
```

Install the GPU configuration:
```
poetry install --extras gpu
```

The important part is the marker:

`markers = "extra != 'gpu'"`

When the `gpu` extra is not selected, the CPU dependency is selected. When `gpu` is selected, the GPU dependency is selected instead.