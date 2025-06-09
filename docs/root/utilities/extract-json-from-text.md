Parsing JSON objects from noisy or mixed-content text (e.g., LLM responses) is easy with this utility function.

!!! dependencies
    ```bash
    pip install jsonfinder
    ```

## ⚙️ Function Definition

```python title="utils.py"
import re
import jsonfinder

def extract_json_objects(text: str, sanitize_text: bool = False):
    """
    Extracts valid JSON objects from a text string.

    Args:
        text (str): Input text that may contain embedded JSON objects.
        sanitize_text (bool): If True, removes control characters often introduced by LLMs (e.g., Gemini).

    Yields:
        Any: Parsed JSON objects found in the text.

    Examples:
        >>> list(extract_json_objects('Text: {"a": 1}'))
        [{'a': 1}]
    """
    if sanitize_text:
        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]+', '', text)

    for i in jsonfinder.jsonfinder(text):
        if i[2] is not None:
            yield i[2]
```


## ✅ When to Use

* When parsing JSON embedded in LLM outputs.
* When processing logs, responses, or raw strings that **contain but are not purely** JSON
* When cleaning or extracting structured data from **mixed-format text blobs**

## 📝 Usage Example

### 1. Basic JSON object extraction
```py
text = 'Text before {"key": "value"} text after'
result = next(extract_json_objects(text))
"""
{"key": "value"}
"""
```

### 2. Multiple JSON objects in one string
```py
text = '{"a": 1} some text {"b": 2}'
result = list(extract_json_objects(text))
"""
[{"a": 1}, {"b": 2}]
"""
```

### 3. Malformed JSON should not be returned
```py
text = 'Invalid: {key: 1}, valid: {"c": 3}, and valid: {"q": "b"}'
for json_obj in extract_json_objects(text):
    print(json_obj)
"""
{"c": 3}
{"q": "b"}
"""
```

### 4. Input with invalid control characters, no cleaning
```py
text = '{"d": 4\x01}'
result = next(extract_json_objects(text), None)
"""
None
"""
```

### 5. Input with control characters and cleaning enabled
```py
text = '{"d": 4\x01}'
result = next(extract_json_objects(text, sanitize_text=True), None)
"""
{"d": 4}
"""
```

### 6. No JSON present
```py
text = 'Just some plain text.'
result = list(extract_json_objects(text))
"""
[]
"""
```

### 7. Nested JSON object
```py
text = 'Here is a nested one: {"outer": {"inner": "value"}}'
result = next(extract_json_objects(text))
"""
{"outer": {"inner": "value"}}
"""
```

### 8. JSON array
```py
text = 'This is an array: [{"x": 1}, {"y": 2}]'
result = list(extract_json_objects(text))
"""
[
    [{"x": 1}, {"y": 2}]
]
"""
```