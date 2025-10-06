

## 🧠 **Main Difference Between Compiler and Interpreter**

| Feature                   | **Compiler**                                                                   | **Interpreter**                                                                 |
| ------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **Definition**            | Translates the **entire program** into machine code (binary) before execution. | Translates and executes the program **line by line** (one statement at a time). |
| **Execution Speed**       | 🏎️ Fast — because code is already converted to machine code.                  | 🐢 Slower — translates during execution.                                        |
| **Error Detection**       | Detects **all errors at once** (after compilation).                            | Detects **one error at a time** (stops at first error).                         |
| **Output**                | Generates an **executable file** (e.g., `.exe`, `.class`).                     | No separate output file — executes directly.                                    |
| **Memory Usage**          | Higher (stores compiled code).                                                 | Lower (no need to store compiled code).                                         |
| **Examples of Languages** | C, C++, Java (compiles to bytecode), Go, Rust                                  | Python, JavaScript, PHP, Ruby                                                   |
| **Portability**           | Less portable (depends on compiled binary).                                    | More portable (source code can run anywhere with interpreter).                  |

---

## 🧩 **In Simple Words**

* A **compiler** reads the *whole book* before telling you if there’s a mistake.
* An **interpreter** reads *one line at a time*, and stops if it finds an error.

---

## ⚙️ **Example**

### Compiler (e.g., C)

```c
#include <stdio.h>
int main() {
    printf("Hello World");
    return 0;
}
```

➡️ You must **compile** it first:

```bash
gcc hello.c -o hello
./hello
```

Output:

```
Hello World
```

---

### Interpreter (e.g., Python)

```python
print("Hello World")
```

➡️ Just run it directly:

```bash
python hello.py
```

Output:

```
Hello World
```

---

## 🧠 **Bonus: Some Languages Use Both**

* **Java** → Compiled to **bytecode** by compiler (`javac`),
  then executed by **JVM interpreter**.
* **Modern Python** → Also compiles to **bytecode (`.pyc`)**, but still interpreted at runtime.

---

### ✅ **In one line:**

> A **compiler** translates the whole program before running it,
> while an **interpreter** translates and runs it line by line.

---
