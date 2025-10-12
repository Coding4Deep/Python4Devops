
### 🧩 Q1. Understanding the Basics

Create a class `Countdown` that counts down from a given number to 1 using the iterator protocol.

Requirements:

* Define `__init__`, `__iter__`, and `__next__`.
* Raise `StopIteration` when it reaches 0.
* Example:

  ```python
  for num in Countdown(3):
      print(num)
  # Output: 3 2 1
  ```

---

### 🧩 Q2. Multiple Iterators

Modify your `Countdown` class so that **each `for` loop gets its own fresh iterator** (it restarts from the top every time).

Hint: Change what `__iter__` returns.

Then test it with:

```python
c = Countdown(3)
for i in c:
    for j in c:
        print(i, j)
```

---

### 🧩 Q3. Manual Iteration

Create an instance of your `Countdown` and manually iterate using `next()` instead of a `for` loop.

Example:

```python
c = Countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))   # should raise StopIteration
```

Explain (in comments) what happens when `StopIteration` occurs.

---

### 🧩 Q4. Iterator Reuse Problem

Create a class `CountUp` that counts from 1 to N.

* Make it return `self` from `__iter__`.
* Create a single object `c = CountUp(3)`
* Run:

  ```python
  for i in c:
      for j in c:
          print(i, j)
  ```

Explain (in comments) why the output is **not 9 pairs** and how to fix it.

---

### 🧩 Q5. Custom Iterable with Fresh Iterator

Fix your `CountUp` class from Q4 so that each `for` loop restarts counting from 1 again.
(Hint: return a *new* iterator object each time `__iter__` is called.)

---

### 🧩 Q6. Using Iterator to Simulate File Reading

Create a class `FakeFile` that simulates reading lines from a file.

Requirements:

* It accepts a list of strings (lines).
* Each call to `next()` returns one line.
* When all lines are read, raise `StopIteration`.

Example:

```python
lines = ["Hello", "World", "Python"]
for line in FakeFile(lines):
    print(line)
```

---

### 🧩 Q7. Infinite Iterator (⚠️ Be careful)

Create a class `EvenNumbers` that **infinitely generates even numbers** starting from 0.

* Don’t raise `StopIteration`.
* Test it carefully by only printing the first 5 numbers (use `itertools.islice`).

Example:

```python
import itertools
evens = EvenNumbers()
for num in itertools.islice(evens, 5):
    print(num)
```

---

### 🧩 Q8. Combining Iterators

Write a function `merge_iterators(it1, it2)` that takes two iterators and yields values alternately:

```python
# Example:
# it1 = [1, 3, 5]
# it2 = [2, 4, 6]
# Output: 1 2 3 4 5 6
```

You must implement it **without using `zip()`** — manually with `next()` and try/except.

---

### 🧩 Q9. Generator vs Iterator Comparison

Create a class-based iterator `SquareIterator(n)` that yields squares from 1² to n².

Then write a **generator function** version `square_generator(n)` that does the same.

Compare:

* Which one is simpler?
* Which one keeps less state?
* Are both lazy (on-demand)?

---

### 🧩 Q10. Deep Understanding Challenge

Here’s a tricky code:

```python
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration

c1 = Counter(3)
c2 = Counter(3)

for i in c1:
    for j in c2:
        print(i, j)
```

