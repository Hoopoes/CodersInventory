A comprehensive guide to MkDocs formatting, covering essential Markdown syntax and features.




<br>

---

<br>





## 📝 Headings
Use `#` symbols to create headings of different levels.
```md
# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
##### H5 Heading
###### H6 Heading
```





<br>

---

<br>





## ✍️ Text Formatting  
Style text using bold, italic, strikethrough, or a combination.
```md
**Bold Text**  
*Italic Text*  
~~Strikethrough~~  
**_Bold & Italic_**  
```

**OUTPUT**
  
**Bold Text**  
*Italic Text*  
~~Strikethrough~~  
**_Bold & Italic_**  





<br>

---

<br>





## 📋 Lists  

### Unordered List  
Create bulleted lists using `-` or `*`.
```md
- Item 1
- Item 2
    - Sub-item 1
    - Sub-item 2
```

**OUTPUT**

- Item 1  
- Item 2  
    - Sub-item 1  
    - Sub-item 2  

### Ordered List
Use numbers for ordered lists.
```md
1. First item
2. Second item
    1. Sub-item
    2. Sub-item
```

**OUTPUT**
  
1. First item  
2. Second item  
    1. Sub-item  
    2. Sub-item  





<br>

---

<br>





## 💬 Blockquotes  
Use `>` to create blockquotes for emphasis or citations.
```md
> This is a blockquote.  
> It can span multiple lines.
```

**OUTPUT**
  
> This is a blockquote.  
> It can span multiple lines.  





<br>

---

<br>





## ➖ Horizontal Rule/Line
Use `---`, `***`, or `___` to insert a horizontal line.
```md
---
***
___
```

**OUTPUT**
  
---  
***  
___  





<br>

---

<br>





## 🔗 Links  
Create clickable hyperlinks using `[text](URL)`.
```md
[Visit MkDocs](https://www.mkdocs.org)
```

**OUTPUT**
  
[Visit MkDocs](https://www.mkdocs.org)  





<br>

---

<br>





## 🖼️ Images
Embed images using `![Alt Text](Image URL)`.
```md
![Alt Text](https://via.placeholder.com/150)
```

**OUTPUT**
  
![Alt Text](https://via.placeholder.com/150)  





<br>

---

<br>





## 📊 Tables
Organize data using pipes `|` and hyphens `-`.
```md
| Name  | Age |  Country |
|-------|----:|----------|
| Alice |  25 | USA      |
| Bob   |  30 | Canada   |
```

**OUTPUT**
  
| Name  | Age | Country  |  
|-------|----:|---------|  
| Alice |  25 | USA     |  
| Bob   |  30 | Canada  |  





<br>

---

<br>





## 💻 Code Blocks  

### Basic Code Block
Wrap code snippets inside triple backticks.
```md
    ```py
    print("Hello, World!")
    ```
```

**OUTPUT**
  
```py
print("Hello, World!")
```

<br>

### With Language Syntax Highlighting 
Specify the programming language for syntax highlighting.
```md
    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```
```

**OUTPUT**
  
```python
def greet(name):
    return f"Hello, {name}!"
```

<br>


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
    ```python hl_lines="2 3"
    def greet(name):
        message = f"Hello, {name}!"  # Highlighted
        return message  # Highlighted
    ```
```

**OUTPUT**
  
```python hl_lines="2 3"
def greet(name):
    message = f"Hello, {name}!"  # Highlighted
    return message  # Highlighted
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


### Inline Code  
Use backticks to insert inline code within text.
```md
Use `print("Hello, World!")` inside a sentence.
```

**OUTPUT**
  
Use `print("Hello, World!")` inside a sentence.  





<br>

---

<br>





## 🏷️ Code Annotation

```
    ```python
    def greet(name):  # ⮑ Function definition
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
def greet(name):  # ⮑ Function definition
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

<br>





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

<br>





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

<br>





## ✅ Task Lists
Create interactive task lists with `[ ]` for incomplete and `[x]` for completed tasks.
```md
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```

**OUTPUT**
  
- [x] Task 1  
- [ ] Task 2  
- [ ] Task 3  





<br>

---

<br>





## 🔢 Math Equations (LaTeX)  
Use LaTeX syntax within `$$` to display mathematical equations.
```md
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$
```

**OUTPUT**
  
$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$  





<br>

---

<br>





## 😀 Emojis (If Supported)
Insert emojis using Unicode characters.
```md
🚀 🎉 🔥
```

**OUTPUT**
  
🚀 🎉 🔥  


<br>

---

<br>

