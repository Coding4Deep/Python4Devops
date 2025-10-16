

# 🧩 Python `re` Module — Full Explanation

## 📘 Introduction

`re` (Regular Expression) is Python’s built-in module for working with **regular expressions** — patterns that describe sets of strings.

You typically use it to:

* Search for patterns in text
* Replace text
* Validate formats (emails, phone numbers, etc.)
* Split strings based on complex rules

---

## ✅ Import

```python
import re
```

---

# 🧠 MAIN FUNCTIONS

---

## 1️⃣ `re.match(pattern, string, flags=0)`

Matches a pattern **only at the beginning** of the string.

```python
import re

result = re.match(r'Hello', 'Hello world!')
print(result.group())  # Hello

# Doesn't match because "world" isn't at start
print(re.match(r'world', 'Hello world!'))  # None
```

---

## 2️⃣ `re.search(pattern, string, flags=0)`

Searches **anywhere** in the string (first occurrence).

```python
text = "Python is fun"
result = re.search(r'is', text)
print(result.start(), result.end())  # 7 9
```

---

## 3️⃣ `re.fullmatch(pattern, string, flags=0)`

Matches the **entire string** (not just the start).

```python
re.fullmatch(r'\d+', '12345')    # ✅ matches (digits only)
re.fullmatch(r'\d+', '123abc')   # ❌ None
```

---

## 4️⃣ `re.findall(pattern, string, flags=0)`

Returns **all matches** as a **list of strings**.

```python
text = "cat bat rat mat"
print(re.findall(r'\b\w{3}\b', text))
# ['cat', 'bat', 'rat', 'mat']
```

---

## 5️⃣ `re.finditer(pattern, string, flags=0)`

Returns **an iterator** of `Match` objects for all matches.

```python
text = "apple, banana, cherry"
for match in re.finditer(r'\w+', text):
    print(match.group(), match.start(), match.end())
```

---

## 6️⃣ `re.split(pattern, string, maxsplit=0, flags=0)`

Splits a string **by the pattern**.

```python
text = "apple,banana;cherry orange"
print(re.split(r'[;, ]+', text))
# ['apple', 'banana', 'cherry', 'orange']
```

---

## 7️⃣ `re.sub(pattern, repl, string, count=0, flags=0)`

Replaces matches of the pattern with a replacement string.

```python
text = "one two three two one"
print(re.sub(r'two', '2', text))
# "one 2 three 2 one"
```

---

## 8️⃣ `re.subn(pattern, repl, string, count=0, flags=0)`

Like `re.sub()`, but also returns **the number of replacements** made.

```python
print(re.subn(r'two', '2', text))
# ('one 2 three 2 one', 2)
```

---

## 9️⃣ `re.compile(pattern, flags=0)`

Compiles a regex pattern into a **RegexObject** for reuse.

```python
pattern = re.compile(r'\d+')
print(pattern.findall("There are 12 apples and 3 bananas"))
# ['12', '3']
```

This lets you reuse the same pattern efficiently.

---

# 🧩 RegexObject METHODS

When you use `re.compile()`, you get a **RegexObject**.
It has the same methods as top-level ones, but operates on its own pattern.

| Method                | Description             |
| --------------------- | ----------------------- |
| `.match(string)`      | Same as `re.match()`    |
| `.search(string)`     | Same as `re.search()`   |
| `.findall(string)`    | Same as `re.findall()`  |
| `.finditer(string)`   | Same as `re.finditer()` |
| `.split(string)`      | Same as `re.split()`    |
| `.sub(repl, string)`  | Same as `re.sub()`      |
| `.subn(repl, string)` | Same as `re.subn()`     |

---

# 🧱 MatchObject METHODS

When you get a match (from `match()`, `search()`, etc.), you get a **MatchObject**.

### Attributes & Methods:

| Method / Attribute | Description                                  | Example      |
| ------------------ | -------------------------------------------- | ------------ |
| `.group([n])`      | Returns the entire match or a specific group | `m.group(0)` |
| `.groups()`        | Returns a tuple of all groups                |              |
| `.groupdict()`     | Returns named groups as dict                 |              |
| `.start([group])`  | Start index of match                         |              |
| `.end([group])`    | End index                                    |              |
| `.span([group])`   | Tuple of (start, end)                        |              |
| `.string`          | Original string searched                     |              |
| `.re`              | The regex object used                        |              |

Example:

```python
text = "My phone number is 123-456-7890"
m = re.search(r'(\d{3})-(\d{3})-(\d{4})', text)

print(m.group())      # '123-456-7890'
print(m.groups())     # ('123', '456', '7890')
print(m.start(), m.end())  # 19 31
```

---

# ⚙️ FLAGS

Flags modify how patterns are matched.

| Flag                      | Description                                  |
| ------------------------- | -------------------------------------------- |
| `re.IGNORECASE` or `re.I` | Case-insensitive matching                    |
| `re.MULTILINE` or `re.M`  | `^` and `$` match start/end of each line     |
| `re.DOTALL` or `re.S`     | `.` matches newline too                      |
| `re.VERBOSE` or `re.X`    | Allows whitespace/comments in pattern        |
| `re.ASCII` or `re.A`      | Make `\w`, `\b`, `\d`, etc. match ASCII only |
| `re.LOCALE`               | Locale-aware matching (rarely used)          |

Example:

```python
text = "Hello\nWorld"
print(re.findall(r'^World', text))            # []
print(re.findall(r'^World', text, re.M))      # ['World']
```

---

# 🎯 COMMON REGEX PATTERNS

| Task            | Pattern                  | Example                 |
| --------------- | ------------------------ | ----------------------- |
| Digits only     | `^\d+$`                  | `"12345"`               |
| Email           | `^[\w.-]+@[\w.-]+\.\w+$` | `"abc@xyz.com"`         |
| Word boundaries | `\bword\b`               | Match whole word “word” |
| Whitespace      | `\s+`                    | Spaces, tabs, newlines  |
| Alphanumeric    | `\w+`                    | Letters + digits + `_`  |

---

# 🔍 Example: Validate Email

```python
email = "test@example.com"
pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
print(bool(pattern.match(email)))  # True
```

---

# 🧾 SUMMARY TABLE

| Category             | Functions / Classes                       |
| -------------------- | ----------------------------------------- |
| **Pattern matching** | `match()`, `search()`, `fullmatch()`      |
| **Multiple matches** | `findall()`, `finditer()`                 |
| **Substitution**     | `sub()`, `subn()`                         |
| **Splitting**        | `split()`                                 |
| **Compilation**      | `compile()`                               |
| **Objects**          | `RegexObject`, `MatchObject`              |
| **Flags**            | `IGNORECASE`, `MULTILINE`, `DOTALL`, etc. |

---

# 🧪 Quick Demo

```python
import re

text = "Email me at hello@example.com or admin@test.org"

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(emails)
# ['hello@example.com', 'admin@test.org']

# Replace emails with [REDACTED]
print(re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED]', text))
```

---
