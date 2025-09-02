---

## 🔹 What are Data Structures?

A **data structure** is a way of organizing and storing data so it can be accessed and modified efficiently.
In Python, data structures are broadly classified into **built-in** and **user-defined (custom)**.

---

## 🔹 Built-in Data Structures in Python

1. **List**

   * Ordered, mutable (can change), allows duplicates.
   * Example: `numbers = [1, 2, 3, 4]`
   * Supports indexing, slicing, iteration, and methods like `.append()`, `.remove()`, `.sort()`.

2. **Tuple**

   * Ordered, immutable (cannot change after creation), allows duplicates.
   * Example: `coordinates = (10, 20, 30)`
   * Faster than lists and used for fixed data.

3. **Set**

   * Unordered, mutable, does not allow duplicates.
   * Example: `unique_values = {1, 2, 3}`
   * Supports mathematical operations like union, intersection, difference.

4. **Dictionary**

   * Unordered (in Python 3.6+ insertion order is preserved), mutable, key-value pairs.
   * Example: `student = {"name": "Alice", "age": 22}`
   * Keys must be unique and immutable (string, number, tuple).

---

## 🔹 User-defined Data Structures

These are created using classes and modules:

1. **Stack** – LIFO (Last In, First Out)
   Implemented with lists (`append()` & `pop()`).

2. **Queue** – FIFO (First In, First Out)
   Implemented with `collections.deque`.

3. **Linked List** – Nodes connected by references (not built-in, implemented manually).

4. **Tree & Graphs** – For hierarchical and network structures (implemented using classes, `dict`, or external libraries like `networkx`).

---

## 🔹 Why are Data Structures Important?

* Efficient data access and manipulation.
* Save memory and improve performance.
* Help solve complex problems (e.g., graphs in networking, trees in AI).

---
