
# 🧱 **Python Tuples — Complete Guide**

---

## 🧠 **1. What is a Tuple?**

A **tuple** is an **ordered**, **immutable** (unchangeable) collection of items.
They are used to store multiple items in a single variable, just like lists — but once created, they **cannot be modified**.

```python
my_tuple = (10, 20, 30)
```

---

## ⚙️ **2. Key Properties**

| Property                      | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| **Ordered**                   | Items have a fixed order and position                     |
| **Immutable**                 | You cannot change, add, or remove elements after creation |
| **Allows duplicates**         | `(1, 2, 2, 3)` is valid                                   |
| **Can hold mixed data types** | `(1, "Hello", 3.14)`                                      |

---

## 🧩 **3. Creating Tuples**

### ✅ Normal Tuples

```python
t1 = (1, 2, 3, 4)
```

### ✅ Mixed Data

```python
t2 = (10, "hello", 3.14, True)
```

### ✅ Nested Tuple

```python
t3 = ((1, 2), (3, 4))
```

### ✅ Tuple Without Parentheses (Tuple Packing)

```python
t4 = 1, 2, 3
```

### ✅ Single Element Tuple

⚠️ Be careful — you must include a **comma**:

```python
t5 = (5,)   # ✅ Tuple with one element
t6 = (5)    # ❌ This is just an integer
```

---

## 🧮 **4. Accessing Tuple Elements**

```python
t = (10, 20, 30, 40)
print(t[0])     # 10
print(t[-1])    # 40
print(t[1:3])   # (20, 30)
```

---

## 🧱 **5. Tuple Immutability**

Tuples cannot be changed once created:

```python
t = (1, 2, 3)
# t[0] = 10   ❌ This will cause an error
```

But you can **reassign** a new tuple:

```python
t = (1, 2, 3)
t = (10, 20, 30)  # ✅ new tuple assigned
```

---

## 🧰 **6. Tuple Functions (Built-in Functions)**

| Function     | Example          | Output    | Description              |
| ------------ | ---------------- | --------- | ------------------------ |
| `len(t)`     | `len((1,2,3))`   | `3`       | Number of elements       |
| `max(t)`     | `max((1,5,3))`   | `5`       | Largest element          |
| `min(t)`     | `min((1,5,3))`   | `1`       | Smallest element         |
| `sum(t)`     | `sum((1,2,3))`   | `6`       | Sum (for numeric tuples) |
| `tuple(seq)` | `tuple([1,2,3])` | `(1,2,3)` | Convert list to tuple    |

---

## 🧮 **7. Tuple Methods (Only 2)**

| Method      | Example              | Output | Description                      |
| ----------- | -------------------- | ------ | -------------------------------- |
| `.count(x)` | `(1,2,2,3).count(2)` | `2`    | Count occurrences                |
| `.index(x)` | `(1,2,3,4).index(3)` | `2`    | Return index of first occurrence |

✅ Because tuples are **immutable**, they have **fewer methods** than lists.

---

## 🔁 **8. Iterating Over Tuples**

```python
t = ("apple", "banana", "cherry")
for item in t:
    print(item)
```

---

## 🧮 **9. Tuple Operations**

| Operation         | Example         | Output          | Description        |
| ----------------- | --------------- | --------------- | ------------------ |
| **Concatenation** | `(1,2) + (3,4)` | `(1,2,3,4)`     | Combine tuples     |
| **Repetition**    | `(1,2) * 3`     | `(1,2,1,2,1,2)` | Repeat tuple       |
| **Membership**    | `3 in (1,2,3)`  | `True`          | Check if exists    |
| **Slicing**       | `t[1:3]`        | Subtuple        | Extract portion    |
| **Iteration**     | `for i in t:`   | —               | Loop through items |

---

## 🧩 **10. Nested Tuples**

Tuples can store other tuples:

```python
t = ((1,2,3), (4,5,6), (7,8,9))
print(t[1])      # (4,5,6)
print(t[1][2])   # 6
```

---

## 🧱 **11. Tuple Packing and Unpacking**

### 🔹 Packing:

Combine values into a tuple

```python
person = ("Priyanshu", 21, "India")
```

### 🔹 Unpacking:

Extract values into variables

```python
name, age, country = person
print(name)     # Priyanshu
print(age)      # 21
```

### 🔹 With `*` Operator:

```python
nums = (1, 2, 3, 4, 5)
a, *b, c = nums
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

---

## 🧮 **12. Tuple vs List — Key Differences**

| Feature     | List         | Tuple      |
| ----------- | ------------ | ---------- |
| Syntax      | `[ ]`        | `( )`      |
| Mutable     | ✅ Yes        | ❌ No       |
| Methods     | Many         | Few        |
| Performance | Slower       | Faster     |
| Use case    | Dynamic data | Fixed data |
| Nesting     | Allowed      | Allowed    |

---

## 🧠 **13. Useful Built-in Functions (that work on tuples)**

| Function       | Description                    |
| -------------- | ------------------------------ |
| `all(t)`       | True if all elements are True  |
| `any(t)`       | True if any element is True    |
| `enumerate(t)` | Returns pairs (index, value)   |
| `sorted(t)`    | Returns sorted list from tuple |
| `reversed(t)`  | Returns reversed iterator      |
| `zip(t1, t2)`  | Combines tuples element-wise   |

Example:

```python
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(list(zip(t1, t2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

# 🧠 **14. Practice Questions**

### 🟢 Level 1 — Basics

1. Create a tuple of your 5 favorite fruits.

   * Print the first and last fruit.
   * Print the number of fruits using `len()`.

2. Create a tuple with numbers `(10, 20, 30, 40, 50)`.

   * Access the third element.
   * Slice it to get `(20, 30, 40)`.

3. Create a tuple `colors = ("red", "green", "blue", "green")`.

   * Count how many times `"green"` appears.
   * Find the index of `"blue"`.

---

### 🟡 Level 2 — Intermediate

4. Concatenate two tuples `(1,2,3)` and `(4,5,6)` and print the result.
5. Repeat the tuple `(“Hi”, “Bye”)` three times.
6. Check whether `5` exists in `(2,4,6,8,10)`.
7. Convert the list `[1,2,3,4]` into a tuple using `tuple()`.

---

### 🔵 Level 3 — Advanced

8. Unpack the tuple `person = ("Priyanshu", 21, "India")` into 3 variables and print them.

9. Use tuple unpacking with `*` to split `(1,2,3,4,5)` into `first`, `middle`, and `last`.

10. Create a nested tuple `matrix = ((1,2,3), (4,5,6), (7,8,9))` and print:

    * The entire 2nd row
    * The last element of the 3rd row

11. Write a program to input 5 numbers from the user and store them in a tuple.
    Then find:

    * Maximum
    * Minimum
    * Sum

12. Create two tuples:

    ```python
    names = ("A", "B", "C")
    marks = (85, 90, 80)
    ```

    Use `zip()` to combine them and print as pairs.

---

