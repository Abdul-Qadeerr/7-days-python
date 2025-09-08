---

# **File Handling in Python**

# **Introduction**

* File handling means: **working with files stored on a computer (read, write, update, delete)**.
* Variables exist only during program execution, but files allow **permanent storage of data**.
* Python provides built-in functions to make file handling easy.

---

## 2. **Opening a File**

We use the `open()` function:

```python
file = open("filename.txt", "mode")
```

### **Common Modes**

* `"r"` → Read (default). Error if file doesn’t exist.
* `"w"` → Write. Creates new file or overwrites if it exists.
* `"a"` → Append. Adds new data at the end of the file.
* `"x"` → Create. Creates new file but errors if file already exists.

### **Text vs Binary**

* `"t"` → Text mode (default).
* `"b"` → Binary mode (images, videos, audio).

Example:

```python
f = open("data.txt", "r")
```

---

## 3. **Reading from a File**

Methods to read file contents:

* `read()` → Reads the entire file.
* `readline()` → Reads one line at a time.
* `readlines()` → Reads all lines into a list.

Example:

```python
f = open("data.txt", "r")
print(f.read())
f.close()
```

---

## 4. **Writing to a File**

If a file is opened in `"w"` or `"a"` mode:

```python
f = open("data.txt", "w")
f.write("Hello, Qadeer!\n")
f.write("Learning Python file handling.")
f.close()
```

* `"w"` → Deletes old data and writes new.
* `"a"` → Keeps old data and appends new.

---

## 5. **Closing a File**

Always close files after operations to save changes:

```python
f.close()
```

---

## 6. **Using `with` Statement**

Best practice → file closes automatically:

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 7. **Working with Binary Files**

For images, audio, etc.:

```python
with open("image.jpg", "rb") as f:
    data = f.read()
```

---

## 8. **Useful File Methods**

* `f.read(size)` → Reads given number of characters/bytes.
* `f.tell()` → Returns current pointer position.
* `f.seek(offset)` → Moves pointer to given position.
* `f.name` → File name.
* `f.mode` → File mode used.

---

## 9. **Example Program**

```python
# Writing to file
with open("notes.txt", "w") as f:
    f.write("Python File Handling\n")
    f.write("This is file handling in Python.")

# Reading from file
with open("notes.txt", "r") as f:
    data = f.read()
    print(data)
```

---

## 10. **Advantages of File Handling**

✅ Permanent storage of data.
✅ Handle large data efficiently.
✅ Works with both text and binary files.
✅ Easy to read, write, append, or update data.

---
