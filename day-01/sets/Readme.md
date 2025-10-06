# 🔥 **Python Sets — Complete Guide**

---

## 🧠 **1. What is a Set?**

A **set** in Python is an **unordered**, **mutable** collection of **unique** elements.
Sets are used when you want to **store multiple items** but don’t want **duplicates** and **don’t care about order**.

```python
my_set = {1, 2, 3, 4}
```

---

## ⚙️ **2. Key Properties of Sets**

| Property                 | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| **Unordered**            | No fixed order; elements’ positions change.             |
| **Mutable**              | You can add or remove elements.                         |
| **Unique elements only** | Duplicates are automatically removed.                   |
| **No indexing/slicing**  | You cannot access items by position (e.g., `set[0]` ❌). |

---

## 🧩 **3. Creating Sets**

### ✅ Normal Set

```python
s = {1, 2, 3, 4}
```

### ✅ Using `set()` Constructor

```python
s = set([1, 2, 3, 4])
```

### ✅ Empty Set

⚠️ Be careful — `{}` creates an empty **dictionary**, not a set!

```python
s = set()   # ✅ empty set
```

### ✅ Mixed Data Types

```python
s = {1, 3.14, "Hello", True}
```

---

## ⚠️ **4. No Duplicates**

```python
s = {1, 2, 2, 3, 3, 3}
print(s)   # Output: {1, 2, 3}
```

---

## 🧮 **5. Adding & Removing Elements**

| Operation          | Example           | Description                              |
| ------------------ | ----------------- | ---------------------------------------- |
| `add(x)`           | `s.add(10)`       | Adds one element                         |
| `update(iterable)` | `s.update([5,6])` | Adds multiple elements                   |
| `remove(x)`        | `s.remove(5)`     | Removes element; ❌ error if not found    |
| `discard(x)`       | `s.discard(5)`    | Removes element; ✅ no error if not found |
| `pop()`            | `s.pop()`         | Removes a random element                 |
| `clear()`          | `s.clear()`       | Removes all elements                     |

---

### 🔹 Example:

```python
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.remove(2)
s.discard(10)  # no error
print(s)       # {1, 3, 4, 5, 6}
```

---

## 🔁 **6. Iterating Over a Set**

```python
for i in {10, 20, 30}:
    print(i)
```

---

## 🔗 **7. Set Operations (Mathematical)**

Sets support common **mathematical operations** like union, intersection, difference, etc.

| Operation                | Symbol | Example | Description                     |    |                             |
| ------------------------ | ------ | ------- | ------------------------------- | -- | --------------------------- |
| **Union**                | `      | `       | `A                              | B` | All elements from both sets |
| **Intersection**         | `&`    | `A & B` | Common elements                 |    |                             |
| **Difference**           | `-`    | `A - B` | Elements in A not in B          |    |                             |
| **Symmetric Difference** | `^`    | `A ^ B` | Elements in A or B but not both |    |                             |

### Example:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A & B)  # {3, 4}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 5, 6}
```

---

## 🧮 **8. Set Comparison Operators**

| Operator          | Description                             |
| ----------------- | --------------------------------------- |
| `A == B`          | True if both sets have same elements    |
| `A != B`          | True if different                       |
| `A < B`           | True if A is a **subset** of B          |
| `A > B`           | True if A is a **superset** of B        |
| `A.isdisjoint(B)` | True if A and B have no common elements |

### Example:

```python
A = {1, 2}
B = {1, 2, 3}
print(A < B)  # True
print(B > A)  # True
print(A.isdisjoint({4, 5}))  # True
```

---

## 🧱 **9. Useful Built-in Functions for Sets**

| Function        | Example           | Description                         |
| --------------- | ----------------- | ----------------------------------- |
| `len(s)`        | `len({1,2,3})`    | Count elements                      |
| `max(s)`        | `max({1,5,3})`    | Largest value                       |
| `min(s)`        | `min({1,5,3})`    | Smallest value                      |
| `sum(s)`        | `sum({1,2,3})`    | Sum of elements                     |
| `sorted(s)`     | `sorted({3,1,2})` | Returns sorted list                 |
| `set(iterable)` | `set([1,1,2])`    | Converts to set, removes duplicates |

---

## 🧩 **10. Frozen Sets (Immutable Sets)**

A **frozenset** is an **immutable** version of a set — cannot be changed after creation.

```python
fs = frozenset([1, 2, 3, 3])
print(fs)       # frozenset({1, 2, 3})
# fs.add(4) ❌ → Error (immutable)
```

They are useful when you want a **set inside another set or dictionary key**, since normal sets are not hashable.

---

## 🧮 **11. Converting Between Data Types**

| From        | To                           | Example |
| ----------- | ---------------------------- | ------- |
| List → Set  | `set([1,2,2,3])` → `{1,2,3}` |         |
| Tuple → Set | `set((1,2,3))` → `{1,2,3}`   |         |
| Set → List  | `list({1,2,3})` → `[1,2,3]`  |         |

---

## 🧠 **12. Real-life Use Cases**

* Removing duplicates from a list
* Checking membership efficiently
* Performing mathematical set operations (like common students, etc.)
* Filtering data or comparing unique values

Example:

```python
nums = [1,2,2,3,4,4,5]
unique_nums = list(set(nums))
print(unique_nums)  # [1,2,3,4,5]
```

---

# 🧮 **13. Practice Questions**

### 🟢 Level 1 — Basics

1. Create a set of 5 colors.

   * Print all colors.
   * Add one more color.
   * Remove one color using `discard()`.

2. Create a set of numbers `{1,2,3,4,5}`

   * Add `6`
   * Remove `3`
   * Print length of set.

---

### 🟡 Level 2 — Intermediate

3. Create two sets:

   ```python
   A = {1, 2, 3, 4}
   B = {3, 4, 5, 6}
   ```

   * Find union, intersection, and difference.
   * Find elements only in one of them (symmetric difference).

4. Check if `{1,2}` is a subset of `{1,2,3,4}`.

5. Remove duplicates from `[10, 20, 20, 30, 30, 40]` using a set.

---

### 🔵 Level 3 — Advanced

6. Create a set from user input of numbers and:

   * Print max, min, sum.
   * Print sorted list of numbers.

7. Create a frozen set and try to add an element (observe the error).

8. Use two sets to find which students are in **both** math and science classes.

9. Write a Python program to find elements present in **either of two sets but not both** (symmetric difference).

10. Convert a list to a set, then back to a list — to remove duplicates but keep it ordered using `sorted()`.

---

## 🧩 Bonus: Common Pitfalls

| Mistake            | Why                                  |
| ------------------ | ------------------------------------ |
| `{}`               | Creates an empty **dict**, not a set |
| Sets are unordered | No indexing like `s[0]`              |
| Duplicates vanish  | `set({1,1,2})` becomes `{1,2}`       |

---

