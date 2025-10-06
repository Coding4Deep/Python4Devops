

## 🧮 1. **Numbers in Python**

Numbers are **data types** that represent numeric values.

### 🔢 Types of Numbers

| Type        | Example               | Description                                   |
| ----------- | --------------------- | --------------------------------------------- |
| **int**     | `5`, `-42`, `1000`    | Whole numbers (no decimal point)              |
| **float**   | `3.14`, `-0.5`, `2e3` | Numbers with decimals (floating point)        |
| **complex** | `2 + 3j`              | Complex numbers with real and imaginary parts |

---

### ⚙️ Common **Functions and Operations** on Numbers

#### ➕ Basic Arithmetic Operators

| Operator | Example   | Result     | Meaning                      |
| -------- | --------- | ---------- | ---------------------------- |
| `+`      | `3 + 2`   | `5`        | Addition                     |
| `-`      | `5 - 3`   | `2`        | Subtraction                  |
| `*`      | `4 * 2`   | `8`        | Multiplication               |
| `/`      | `10 / 3`  | `3.333...` | Division (returns float)     |
| `//`     | `10 // 3` | `3`        | Floor division (rounds down) |
| `%`      | `10 % 3`  | `1`        | Modulus (remainder)          |
| `**`     | `2 ** 3`  | `8`        | Exponentiation (power)       |

---

### 🧰 Built-in **Functions for Numbers**

| Function        | Example            | Result   | Description                   |
| --------------- | ------------------ | -------- | ----------------------------- |
| `abs(x)`        | `abs(-5)`          | `5`      | Absolute value                |
| `pow(x, y)`     | `pow(2, 3)`        | `8`      | Power function (`x ** y`)     |
| `round(x, n)`   | `round(3.1416, 2)` | `3.14`   | Round to n decimals           |
| `max(a, b, c)`  | `max(1, 5, 3)`     | `5`      | Largest value                 |
| `min(a, b, c)`  | `min(1, 5, 3)`     | `1`      | Smallest value                |
| `divmod(a, b)`  | `divmod(10, 3)`    | `(3, 1)` | Returns (quotient, remainder) |
| `int(x)`        | `int(3.9)`         | `3`      | Converts to integer           |
| `float(x)`      | `float(5)`         | `5.0`    | Converts to float             |
| `complex(a, b)` | `complex(2, 3)`    | `(2+3j)` | Creates a complex number      |

---

### 🧮 Math Module Functions

To use advanced math operations, import `math`:

```python
import math
```

| Function            | Example               | Result       | Description    |
| ------------------- | --------------------- | ------------ | -------------- |
| `math.sqrt(x)`      | `math.sqrt(9)`        | `3.0`        | Square root    |
| `math.factorial(x)` | `math.factorial(5)`   | `120`        | Factorial      |
| `math.ceil(x)`      | `math.ceil(3.2)`      | `4`          | Round up       |
| `math.floor(x)`     | `math.floor(3.9)`     | `3`          | Round down     |
| `math.pi`           | `math.pi`             | `3.14159...` | Pi constant    |
| `math.e`            | `math.e`              | `2.718...`   | Euler’s number |
| `math.log(x)`       | `math.log(10)`        | `2.302...`   | Natural log    |
| `math.sin(x)`       | `math.sin(math.pi/2)` | `1.0`        | Sine           |
| `math.cos(x)`       | `math.cos(0)`         | `1.0`        | Cosine         |
| `math.tan(x)`       | `math.tan(math.pi/4)` | `1.0`        | Tangent        |

---

## 🧱 2. **Variables in Python**

A **variable** is a name that stores a value in memory.

Example:

```python
x = 10
name = "Priyanshu"
pi = 3.14
```

---

### ⚙️ Rules for Variables

1. Must start with a **letter** or **underscore** (`_`)
2. Cannot start with a number
3. Can contain letters, digits, and underscores
4. Case-sensitive (`Name` ≠ `name`)
5. Should describe the value they hold

✅ **Valid examples:**

```python
age = 25
_total = 100
user_name = "Alice"
```

❌ **Invalid examples:**

```python
2cool = 5      # starts with a number
my-name = "A"  # contains a hyphen
```

---

### 🧰 Variable Operations

| Operation               | Example        | Description                 |
| ----------------------- | -------------- | --------------------------- |
| **Assignment**          | `x = 10`       | Store a value               |
| **Reassignment**        | `x = x + 5`    | Update value                |
| **Multiple assignment** | `a, b = 5, 10` | Assign multiple values      |
| **Swap values**         | `a, b = b, a`  | Swap variables              |
| **Delete variable**     | `del x`        | Remove variable from memory |

---

### 🔄 Variable Type Conversion

You can convert between types easily:

```python
x = 5
y = float(x)     # 5.0
z = str(x)       # '5'
n = int("42")    # 42
```

---

### 🧠 Type Checking Functions

| Function             | Example              | Result          | Description     |
| -------------------- | -------------------- | --------------- | --------------- |
| `type(x)`            | `type(5)`            | `<class 'int'>` | Shows data type |
| `isinstance(x, int)` | `isinstance(5, int)` | `True`          | Checks type     |

---

### 🧾 Example Putting It All Together

```python
import math

x = 10
y = 3.5
z = x ** 2 + math.sqrt(y)
print("x:", x)
print("y:", y)
print("z:", round(z, 2))
```

**Output:**

```
x: 10
y: 3.5
z: 102.87
```

---

