

# 🧱 **Python Dictionary**

---

## 🧠 **1. What is a Dictionary?**

A **dictionary** in Python is an **unordered**, **mutable** collection of **key-value pairs**.
It’s used to **store data in a structured way** — similar to a real-life dictionary where each word (key) has a meaning (value).

```python
student = {
    "name": "Priyanshu",
    "age": 21,
    "course": "Python"
}
```

---

## ⚙️ **2. Key Properties**

| Property                                            | Description                                                     |
| --------------------------------------------------- | --------------------------------------------------------------- |
| **Key-Value Pair**                                  | Each element has a key and a value                              |
| **Mutable**                                         | You can add, modify, or remove pairs                            |
| **Unordered (since Python 3.7: insertion ordered)** | Maintains insertion order                                       |
| **Unique Keys**                                     | Keys cannot be duplicated                                       |
| **Keys must be immutable**                          | Keys can be strings, numbers, or tuples, but not lists or dicts |

---

## 🧩 **3. Creating Dictionaries**

### ✅ Using Curly Braces

```python
student = {"name": "Priyanshu", "age": 21, "course": "Python"}
```

### ✅ Using `dict()` Constructor

```python
student = dict(name="Priyanshu", age=21, course="Python")
```

### ✅ Empty Dictionary

```python
d = {}
```

### ✅ Nested Dictionary

```python
students = {
    "student1": {"name": "Aman", "age": 20},
    "student2": {"name": "Neha", "age": 22}
}
```

---

## 🧮 **4. Accessing Dictionary Elements**

| Operation                | Example                       | Output        |
| ------------------------ | ----------------------------- | ------------- |
| Access value             | `student["name"]`             | `'Priyanshu'` |
| Safe access              | `student.get("course")`       | `'Python'`    |
| Missing key with default | `student.get("grade", "N/A")` | `'N/A'`       |

---

## 🧱 **5. Changing and Adding Items**

```python
student["age"] = 22       # Change value
student["grade"] = "A+"   # Add new key-value pair
```

---

## 🧹 **6. Removing Items**

| Method      | Example               | Description                       |
| ----------- | --------------------- | --------------------------------- |
| `pop(key)`  | `student.pop("age")`  | Removes key and returns its value |
| `popitem()` | `student.popitem()`   | Removes last inserted item        |
| `del`       | `del student["name"]` | Deletes specific key              |
| `clear()`   | `student.clear()`     | Removes all items                 |

Example:

```python
student = {"name": "Priyanshu", "age": 21, "course": "Python"}
student.pop("age")
student["city"] = "Delhi"
student.popitem()   # removes last item (city)
```

---

## 🔁 **7. Looping (Iteration) in Dictionaries**

### 🔹 Loop through keys:

```python
for key in student:
    print(key)
```

### 🔹 Loop through values:

```python
for value in student.values():
    print(value)
```

### 🔹 Loop through key-value pairs:

```python
for key, value in student.items():
    print(key, ":", value)
```

---

## 🧮 **8. Dictionary Methods (All)**

Here’s the **complete list** of dictionary methods in Python 👇

| Method                     | Description                                                   | Example                                         |
| -------------------------- | ------------------------------------------------------------- | ----------------------------------------------- |
| `clear()`                  | Removes all items                                             | `d.clear()`                                     |
| `copy()`                   | Returns a shallow copy                                        | `new_d = d.copy()`                              |
| `fromkeys(seq, value)`     | Creates a new dict with keys from seq and all values same     | `dict.fromkeys(['a','b'], 0)` → `{'a':0,'b':0}` |
| `get(key, default)`        | Returns value for key or default if not found                 | `d.get('age', 0)`                               |
| `items()`                  | Returns view object of (key, value) pairs                     | `d.items()`                                     |
| `keys()`                   | Returns view object of all keys                               | `d.keys()`                                      |
| `values()`                 | Returns view object of all values                             | `d.values()`                                    |
| `pop(key, default)`        | Removes key and returns value                                 | `d.pop('name')`                                 |
| `popitem()`                | Removes last inserted item                                    | `d.popitem()`                                   |
| `setdefault(key, default)` | Returns value if key exists, else adds key with default value | `d.setdefault('grade', 'A')`                    |
| `update(other_dict)`       | Adds or updates key-value pairs from another dict             | `d.update({'city': 'Delhi'})`                   |

---

## 🧮 **9. Built-in Functions Used with Dictionaries**

| Function    | Description                   | Example           |
| ----------- | ----------------------------- | ----------------- |
| `len(d)`    | Number of key-value pairs     | `len(student)`    |
| `str(d)`    | Returns string representation | `str(student)`    |
| `type(d)`   | Returns dictionary type       | `type(student)`   |
| `sorted(d)` | Returns sorted list of keys   | `sorted(student)` |
| `any(d)`    | True if any key is True       | `any(student)`    |
| `all(d)`    | True if all keys are True     | `all(student)`    |

---

## 🧩 **10. Dictionary Comprehension**

You can create dictionaries in one line using **comprehension syntax**:

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}
```

Or with conditions:

```python
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

---

## 🧱 **11. Nested Dictionaries**

Dictionaries inside dictionaries:

```python
students = {
    "Aman": {"age": 20, "course": "Python"},
    "Neha": {"age": 22, "course": "Java"}
}

print(students["Aman"]["course"])  # Python
```

---

## 🧩 **12. Merging Dictionaries**

### ✅ Using `update()`

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
a.update(b)
# {'x': 1, 'y': 3, 'z': 4}
```

### ✅ Using Dictionary Unpacking (Python 3.9+)

```python
c = a | b
```

---

## 🧠 **13. Copying Dictionaries**

Be careful:
`d2 = d1` just creates a reference — both point to same object.
Use:

```python
copy_d = d1.copy()
```

---

## 🧩 **14. Dictionary vs JSON**

Dictionaries are very similar to **JSON** objects (JavaScript Object Notation).
You can easily convert between them using Python’s `json` module.

```python
import json

d = {"name": "Priyanshu", "age": 21}
json_str = json.dumps(d)
print(json_str)   # '{"name": "Priyanshu", "age": 21}'
```

---

# 🧮 **15. Practice Questions**

### 🟢 Level 1 — Basics

1. Create a dictionary with keys `name`, `age`, and `city`. Print all values.
2. Add a new key `course` = `'Python'`.
3. Change the `age` value to `25`.
4. Delete the key `city`.

---

### 🟡 Level 2 — Intermediate

5. Create two dictionaries:

   ```python
   d1 = {"a": 10, "b": 20}
   d2 = {"b": 30, "c": 40}
   ```

   Merge them using `update()` and `|`.

6. Create a dictionary using `fromkeys(['a','b','c'], 0)`.

7. Write a loop to print keys and values separately.

8. Use `setdefault()` to insert a missing key `'grade': 'A'`.

---

### 🔵 Level 3 — Advanced

9. Create a dictionary of 5 students with their marks.

   * Find highest and lowest marks using `max()` and `min()`.
   * Print only names (keys).

10. Create a **nested dictionary**:

    ```python
    students = {
        "A": {"math": 85, "science": 90},
        "B": {"math": 78, "science": 88}
    }
    ```

    * Access B’s science marks.
    * Add a new subject to A.

11. Convert this list into a dictionary:

    ```python
    keys = ["name", "age", "city"]
    values = ["Priyanshu", 21, "Delhi"]
    ```

    (Hint: use `zip()` and `dict()`)

12. Write a program to count the frequency of each character in a string using a dictionary.

---

## 🧩 **16. Summary Table**

| Feature                | List     | Tuple      | Set               | Dictionary        |
| ---------------------- | -------- | ---------- | ----------------- | ----------------- |
| **Syntax**             | `[ ]`    | `( )`      | `{ }`             | `{key: value}`    |
| **Ordered**            | ✅        | ✅          | ❌                 | ✅                 |
| **Mutable**            | ✅        | ❌          | ✅                 | ✅                 |
| **Duplicates Allowed** | ✅        | ✅          | ❌                 | ❌ (keys only)     |
| **Access by**          | Index    | Index      | No Index          | Key               |
| **Use Case**           | Sequence | Fixed Data | Unique Collection | Key-Value Mapping |

---

