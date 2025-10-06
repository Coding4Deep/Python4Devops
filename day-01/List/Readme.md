
# 🧱 **Python Lists **

---

## 🧠 **What is a List?**

A **list** in Python is an **ordered**, **mutable (changeable)** collection of items.
You can store **multiple data types** (integers, strings, floats, even other lists) in one list.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14, True]
```

---

## ⚙️ **Key Properties**

| Property                         | Description                             |
| -------------------------------- | --------------------------------------- |
| **Ordered**                      | Items have a fixed order                |
| **Mutable**                      | You can change, add, or remove elements |
| **Allow duplicates**             | `[1, 2, 2, 3]` is valid                 |
| **Can contain mixed data types** | e.g., `[1, "two", 3.0]`                 |

---

## 🧩 **1. Creating and Accessing Lists**

```python
my_list = [10, 20, 30, 40]
print(my_list[0])    # Access first element → 10
print(my_list[-1])   # Last element → 40
print(my_list[1:3])  # Slice → [20, 30]
```

---

## 🧮 **2. Modifying Lists**

```python
my_list[1] = 25          # Change value
my_list.append(50)       # Add at end
my_list.insert(2, 35)    # Insert at index 2
del my_list[0]           # Delete by index
```

---

## 🧰 **3. Common List Functions**

| Function       | Example                         | Description               |
| -------------- | ------------------------------- | ------------------------- |
| `len(list)`    | `len([1,2,3])` → `3`            | Length of list            |
| `max(list)`    | `max([1,5,3])` → `5`            | Largest element           |
| `min(list)`    | `min([1,5,3])` → `1`            | Smallest element          |
| `sum(list)`    | `sum([1,2,3])` → `6`            | Sum of numeric elements   |
| `sorted(list)` | `sorted([3,1,2])` → `[1,2,3]`   | Returns sorted copy       |
| `list()`       | `list("abc")` → `['a','b','c']` | Converts iterable to list |

---

## 🧱 **4. Important List Methods**

Here’s the **complete list** of Python list methods (with examples):

| Method                  | Example                           | Description                                       |
| ----------------------- | --------------------------------- | ------------------------------------------------- |
| **append(x)**           | `fruits.append("mango")`          | Add element to the end                            |
| **extend(iterable)**    | `fruits.extend(["grape","kiwi"])` | Add multiple elements                             |
| **insert(i, x)**        | `fruits.insert(1, "orange")`      | Insert at specific index                          |
| **remove(x)**           | `fruits.remove("banana")`         | Remove first occurrence                           |
| **pop([i])**            | `fruits.pop(2)`                   | Remove and return item at index (last by default) |
| **clear()**             | `fruits.clear()`                  | Remove all elements                               |
| **index(x)**            | `fruits.index("apple")`           | Return index of first match                       |
| **count(x)**            | `numbers.count(2)`                | Count occurrences                                 |
| **sort(reverse=False)** | `numbers.sort()`                  | Sort list in place                                |
| **reverse()**           | `numbers.reverse()`               | Reverse list order                                |
| **copy()**              | `new_list = fruits.copy()`        | Shallow copy of list                              |

---

## 🧮 **5. Slicing and Iterating**

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])     # [20, 30, 40]
print(nums[::-1])    # [50, 40, 30, 20, 10] — reverse list
for n in nums:
    print(n)
```

---

## 🧱 **6. Nested Lists**

Lists can contain other lists.

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])   # 6
```

---

## 🧠 **7. List Comprehension**

A shorthand for creating lists.

```python
squares = [x**2 for x in range(1,6)]
print(squares)   # [1, 4, 9, 16, 25]
```

You can also add conditions:

```python
even = [x for x in range(10) if x%2 == 0]
```

---

## 🧰 **8. Copying Lists (Important Concept)**

```python
a = [1,2,3]
b = a          # both refer to same list (linked)
c = a.copy()   # creates new independent copy
```

---

## 🧾 **9. Combining Lists**

```python
a = [1, 2, 3]
b = [4, 5]
combined = a + b        # [1,2,3,4,5]
a.extend(b)             # modifies 'a' → [1,2,3,4,5]
```

---

## 🧮 **10. Built-in Functions that Work on Lists**

| Function             | Description                               |
| -------------------- | ----------------------------------------- |
| `any(list)`          | Returns True if **any** element is True   |
| `all(list)`          | Returns True if **all** elements are True |
| `enumerate(list)`    | Returns pairs of (index, value)           |
| `zip(list1, list2)`  | Combine lists element-wise                |
| `map(func, list)`    | Apply function to all elements            |
| `filter(func, list)` | Filter elements by condition              |

Example:

```python
nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums))
```

---

# 🧩 **Summary Table — Most Useful List Methods**

| Category        | Methods                            |
| --------------- | ---------------------------------- |
| Add Elements    | `append()`, `insert()`, `extend()` |
| Remove Elements | `remove()`, `pop()`, `clear()`     |
| Search          | `index()`, `count()`               |
| Reorder         | `sort()`, `reverse()`              |
| Copy            | `copy()`                           |
| Utility         | `len()`, `sum()`, `max()`, `min()` |

---

# 🧠 **Practice Questions**

### 🟢 Level 1 — Basics

1. Create a list of 5 numbers and print:

   * The first, middle, and last elements.
   * The length of the list.
   * The list reversed using slicing.

2. Create a list `fruits = ["apple", "banana", "cherry"]`.

   * Add `"mango"` to the end.
   * Insert `"orange"` at index 1.
   * Remove `"banana"`.

3. Given `numbers = [1, 2, 3, 4, 5]`,

   * Replace the 3rd element with `99`.
   * Append `6`.
   * Delete the first element.

---

### 🟡 Level 2 — Intermediate

4. Create a list of numbers from 1 to 10, and:

   * Print only even numbers using list comprehension.
   * Square all numbers using a loop.

5. Combine two lists `[1,2,3]` and `[4,5,6]` into one using:

   * `+`
   * `.extend()`

6. Given `marks = [90, 80, 95, 70, 85]`

   * Find the highest and lowest marks.
   * Sort the list in ascending and descending order.

7. Remove duplicates from `[1,2,3,2,4,1,5]` while maintaining order.

---

### 🔵 Level 3 — Advanced

8. Create a list of words from a sentence using `.split()` and:

   * Count how many words there are.
   * Find which word appears most often.

9. Write a program to input 5 numbers from the user into a list and print the average.

10. Given a nested list:

    ```python
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    ```

    * Print the second row.
    * Print all elements of the first column.

11. Sort a list of strings by their length.

12. Use list comprehension to create a list of all multiples of 3 between 1 and 30.

---
