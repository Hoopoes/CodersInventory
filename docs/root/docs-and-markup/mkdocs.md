A comprehensive guide to MkDocs formatting, highlighting its exclusive features. While MkDocs supports standard Markdown, this guide focuses solely on its unique enhancements. For general Markdown syntax, check [Markdown Formatting](markdown.md).

## ⚠️ Admonitions (Notes, Warnings, Tips)  
Use `!!!` for special alert boxes like notes, warnings, and tips.
```md
!!! note
    This is an informational note.

!!! warning
    Be careful with this action!

!!! tip
    Here’s a useful tip for you!

!!! danger
    This is a dangerous operation.
```

**OUTPUT**
  
!!! note  
    This is an informational note.  

!!! warning  
    Be careful with this action!  

!!! tip  
    Here’s a useful tip for you!  

!!! danger  
    This is a dangerous operation.  




<br>

---




## 📂 Expandable Code Blocks (Collapsible Sections)  

### Basic Collapsible Code Block
Use `???+` to create expandable sections.
```md
???+ note "Click to Expand"
    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```
```

**OUTPUT**  

???+ note "Click to Expand"  
    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```

### Collapsible Code Block with Filename
Attach filenames to collapsible sections.
```md
???+ info "View greet.py"
    ```python title="greet.py"
    def greet(name):
        return f"Hello, {name}!"
    ```
```

**OUTPUT**  

???+ info "View greet.py"  
    ```python title="greet.py"
    def greet(name):
        return f"Hello, {name}!"
    ```

### Collapsible Code Block with Explanation
Combine text and collapsible code blocks for better explanation.
```md
???+ warning "See Code with Explanation"
    Here's a simple Python function:
    
    ```python
    def square(num):
        return num * num
    ```
    
    This function takes a number and returns its square.
```

**OUTPUT**  

???+ warning "See Code with Explanation"  
    Here's a simple Python function:  
    
    ```python
    def square(num):
        return num * num
    ```
    
    This function takes a number and returns its square.




<br>

---



## 💻 Code Blocks  

### With Filename  
Label the code block with a filename.
```md
    ```python title="greet.py"
    def greet(name):
        return f"Hello, {name}!"
    ```
```

**OUTPUT**
  
```python title="greet.py"
def greet(name):
    return f"Hello, {name}!"
```

<br>


### With Line Numbers  
Enable line numbers for better readability.
```md
    ```python linenums="1"
    def greet(name):
        return f"Hello, {name}!"
    ```
```

**OUTPUT**
  
```python linenums="1"
def greet(name):
    return f"Hello, {name}!"
```

<br>


### With Highlighted Lines  
Highlight specific lines in the code block.
```md
    ```python hl_lines="2 4 6-8"
    def greet(name):
        message = f"Hello, {name}!" 
        print(message)  
        return message

    def farewell(name):
        message = f"Goodbye, {name}!" 
        print(message)
        return message  
    ```
```

**OUTPUT**
  
```python hl_lines="2 4 6-8"
def greet(name):
    message = f"Hello, {name}!"  
    print(message)  
    return message

def farewell(name):
    message = f"Goodbye, {name}!"
    print(message)
    return message  
```

<br>


### With Line Numbers and Highlighted Lines  
```md
    ```python linenums="1" hl_lines="2"
    def greet(name):
        message = f"Hello, {name}!"  # Highlighted
        return message
    ```
```

**OUTPUT**
  
```python linenums="1" hl_lines="2"
def greet(name):
    message = f"Hello, {name}!"  # Highlighted
    return message
```





<br>

---




## 🏷️ Code Annotation

```
    ```python
    def greet(name):  # Function definition
        message = f"Hello, {name}!"  # (1)!  
        return message # (2)!
    ```
    { .annotate }

    1. Formats a greeting message using f-string.  
    2. Returns the formatted message. 


    Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
    { .annotate }

    1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
        text__, images, ... basically anything that can be expressed in Markdown.
```

**OUTPUT**
  
```python
def greet(name):  # Function definition
    message = f"Hello, {name}!"  # (1)!  
    return message # (2)!
```
{ .annotate }

1. Formats a greeting message using f-string.  
2. Returns the formatted message.
  
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.





<br>

---




