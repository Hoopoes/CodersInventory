A comprehensive guide to Markdown formatting, covering essential Markdown syntax and features.


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





## 🔗 Links  
Create clickable hyperlinks using `[text](URL)`.
```md
[Visit MkDocs](https://www.mkdocs.org)
```

**OUTPUT**

[Visit MkDocs](https://www.mkdocs.org)  




<br>

---




## 🖼️ Images
Embed images using `![Alt Text](Image URL)`.
```md
![Alt Text](https://via.placeholder.com/150)
```

**OUTPUT**
  
![Alt Text](https://via.placeholder.com/150)  




<br>

---




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


### Inline Code  
Use backticks to insert inline code within text.
```md
Use `print("Hello, World!")` inside a sentence.
```

**OUTPUT**
  
Use `print("Hello, World!")` inside a sentence.  





<br>

---




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




## 😀 Emojis (If Supported)
Insert emojis using Unicode characters.
```md
🚀 🎉 🔥
```

**OUTPUT**
  
🚀 🎉 🔥  




<br>

---



