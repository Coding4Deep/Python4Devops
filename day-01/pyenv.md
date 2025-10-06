
---

## 🧩 What is **pyenv**?

> **pyenv** is a **Python version manager** — a simple CLI tool that lets you easily **install, switch, and manage multiple versions of Python** on the same system.

It does **not** replace Python itself — it just controls **which version of Python** gets used when you type `python` in your terminal.

---

### 🧠 Why pyenv Exists

Without pyenv:

* You only have one “system Python.”
* If you install a new Python version, you might break system tools.
* Different projects may require **different Python versions** (e.g., 3.8 vs 3.12).

With pyenv:
✅ You can have **multiple Python versions installed** side by side.
✅ Each project can use **its own version**.
✅ The **system Python stays untouched**.

---

### ⚙️ How pyenv Works (Internals)

When you install pyenv, it **shims** the `python`, `pip`, etc. commands.

```
$PATH
┌───────────────────────────────┐
│ ~/.pyenv/shims                │  ← pyenv intercepts here
│ /usr/local/bin                │
│ /usr/bin                      │
└───────────────────────────────┘
```

* When you type `python`, your shell runs the pyenv **shim**.
* The shim checks which Python version should be active (based on rules below).
* It then forwards the call to the **correct Python binary** in `~/.pyenv/versions`.

---

### 🔢 pyenv Version Resolution Order

When you run a Python command, pyenv decides which version to use by checking:

1. **PYENV_VERSION** (environment variable)
2. **.python-version** file in the current directory
3. **Global version** (set via `pyenv global`)
4. **System Python** (fallback)

Example:

```bash
$ pyenv local 3.11.2   # sets version for this project
$ python --version
Python 3.11.2
```

---

### 🧰 Common pyenv Commands

| Command                  | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `pyenv install --list`   | List all available Python versions               |
| `pyenv install 3.11.2`   | Install a specific Python version                |
| `pyenv versions`         | Show all installed versions                      |
| `pyenv global 3.11.2`    | Set the global default                           |
| `pyenv local 3.9.6`      | Set Python version for current directory         |
| `pyenv shell 3.10.13`    | Temporarily set version in current shell session |
| `pyenv uninstall 3.8.12` | Remove an installed version                      |

---

### 📁 pyenv Directory Structure

```
~/.pyenv/
├── versions/
│   ├── 3.9.6/
│   ├── 3.10.13/
│   └── 3.12.0/
├── shims/
│   ├── python
│   ├── pip
│   └── ...
└── plugins/
    └── python-build/
```

* `versions/` → holds all installed Python interpreters.
* `shims/` → intercepts calls to python/pip.
* `python-build/` → helper plugin that compiles Python from source.

---

### 💡 pyenv + virtualenv = 🔥

`pyenv` handles **Python versions**,
`virtualenv` or `venv` handles **per-project dependencies**.

To simplify both, you can use:

```bash
pyenv virtualenv 3.11.2 myproject-env
pyenv activate myproject-env
```

That gives you an isolated environment with a specific interpreter version.

---

### 🧠 Summary Table

| Concept               | Description                                    |
| --------------------- | ---------------------------------------------- |
| **System Python**     | The OS-installed Python, used for system tools |
| **CPython**           | The actual Python interpreter written in C     |
| **pyenv**             | Tool to manage multiple Python versions        |
| **virtualenv / venv** | Tool to manage dependencies per project        |

---

### 🧩 Analogy

| Concept           | Analogy                                                     |
| ----------------- | ----------------------------------------------------------- |
| **CPython**       | The actual Python “engine”                                  |
| **System Python** | The car that came with your OS                              |
| **pyenv**         | A garage where you can park multiple cars (Python versions) |
| **virtualenv**    | The individual passengers (dependencies) for each project   |

---

