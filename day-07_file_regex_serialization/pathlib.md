# 🧭 1. What is `pathlib`?

`pathlib` is a **standard Python module** (added in Python 3.4) that provides an **object-oriented interface** for working with filesystem paths.

Instead of juggling strings like `os.path.join("folder", "file.txt")`, you use objects like:

```python
from pathlib import Path

p = Path("folder") / "file.txt"
print(p)  # folder/file.txt
```

✅ It works on all platforms (Windows, macOS, Linux) and automatically handles `/` vs `\`.

---

# 2. Importing and Creating Paths

```python
from pathlib import Path

# Current directory
p = Path('.')

# Specific file
f = Path("C:/Users/Priyanshu/Documents/file.txt")

# Join paths easily using '/'
new_path = Path("folder") / "subfolder" / "file.txt"
print(new_path)
```

---

# 🧱 3. Important Classes in `pathlib`

| Class             | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `Path`            | Main class for filesystem paths (OS-independent)                     |
| `PurePath`        | Abstract class for path operations *without* touching the filesystem |
| `PurePosixPath`   | POSIX (Linux/Mac) style pure path                                    |
| `PureWindowsPath` | Windows-style pure path                                              |
| `PosixPath`       | Filesystem-aware subclass (on Linux/Mac)                             |
| `WindowsPath`     | Filesystem-aware subclass (on Windows)                               |

---

# 🗂️ 4. Attributes of Path Objects

Let’s say:

```python
p = Path("/home/user/docs/report.txt")
```

| Attribute    | Example Output                                | Description              |
| ------------ | --------------------------------------------- | ------------------------ |
| `p.name`     | `'report.txt'`                                | File name                |
| `p.stem`     | `'report'`                                    | File name without suffix |
| `p.suffix`   | `'.txt'`                                      | File extension           |
| `p.suffixes` | `['.tar', '.gz']`                             | List of all suffixes     |
| `p.parent`   | `'/home/user/docs'`                           | Parent directory         |
| `p.parents`  | sequence of all parents                       | All ancestors            |
| `p.anchor`   | `'/'`                                         | Root anchor              |
| `p.parts`    | `('/', 'home', 'user', 'docs', 'report.txt')` | Path broken into parts   |
| `p.drive`    | `'C:'` (on Windows)                           | Drive letter             |
| `p.root`     | `'/'`                                         | Root directory           |

---

# ⚙️ 5. Common Methods of `Path` Objects

Let’s categorize them 👇

---

## 🧾 A. **Path Inspection (Read Info)**

```python
p = Path("example.txt")

print(p.exists())     # True if file/directory exists
print(p.is_file())    # True if file
print(p.is_dir())     # True if directory
print(p.is_absolute())# True if absolute path
print(p.resolve())    # Returns absolute path
print(p.stat())       # Get file metadata (size, mtime, etc.)
print(p.owner())      # File owner name
print(p.group())      # File group
```

---

## 🧱 B. **Path Manipulation**

```python
p = Path("/home/user/docs/report.txt")

print(p.with_name("data.csv"))       # /home/user/docs/data.csv
print(p.with_suffix(".csv"))         # /home/user/docs/report.csv
print(p.relative_to("/home/user"))   # docs/report.txt
print(p.joinpath("backup"))          # /home/user/docs/report.txt/backup
print(p.match("*.txt"))              # True
```

---

## 📂 C. **Directory Operations**

```python
p = Path("/home/user/docs")

# Iterate through entries
for item in p.iterdir():
    print(item)

# Recursive search
for txt in p.rglob("*.txt"):
    print(txt)

# Non-recursive glob
for f in p.glob("*.txt"):
    print(f)
```

---

## 🪄 D. **File/Folder Creation and Removal**

```python
p = Path("new_folder")
p.mkdir(exist_ok=True)      # Create folder
(p / "file.txt").touch()    # Create empty file
(p / "file.txt").unlink()   # Delete file
p.rmdir()                   # Remove folder (only if empty)
```

---

## 🧾 E. **Reading and Writing Files**

```python
file = Path("notes.txt")

# Write text
file.write_text("Hello, Pathlib!")

# Read text
print(file.read_text())

# Write bytes
file.write_bytes(b"BinaryData")

# Read bytes
print(file.read_bytes())
```

---

## 🚚 F. **Copying, Moving, and Renaming**

`pathlib` doesn’t have built-in copy/move; use `shutil` for that.

```python
import shutil
src = Path("old.txt")
dst = Path("new.txt")

shutil.copy(src, dst)
shutil.move(dst, Path("backup/new.txt"))
```

But renaming is supported:

```python
p = Path("oldname.txt")
p.rename("newname.txt")
```

---

# 🔍 6. Methods of `PurePath` (No filesystem access)

For example:

```python
from pathlib import PurePath

p = PurePath("/home/user/docs/file.txt")

print(p.parts)                # ('/', 'home', 'user', 'docs', 'file.txt')
print(p.parent)               # /home/user/docs
print(p.name)                 # file.txt
print(p.suffix)               # .txt
print(p.with_suffix('.csv'))  # /home/user/docs/file.csv
```

These methods don’t check if files exist — just manipulate path strings safely.

---

# 🧰 7. Advanced Usage Examples

### Example 1 — Find all `.py` files recursively

```python
from pathlib import Path

for file in Path('.').rglob('*.py'):
    print(file)
```

### Example 2 — Create nested folders if they don’t exist

```python
p = Path("a/b/c")
p.mkdir(parents=True, exist_ok=True)
```

### Example 3 — Change file extension

```python
p = Path("report.docx")
p = p.with_suffix(".pdf")
print(p)  # report.pdf
```

### Example 4 — Get file size

```python
p = Path("example.txt")
print(p.stat().st_size, "bytes")
```

### Example 5 — Platform-specific paths

```python
from pathlib import PureWindowsPath, PurePosixPath

print(PureWindowsPath("C:/Users/User/file.txt"))
print(PurePosixPath("/home/user/file.txt"))
```

---

# 📖 8. Summary — All Key Members

### Attributes

`name`, `suffix`, `suffixes`, `stem`, `parent`, `parents`, `parts`, `anchor`, `drive`, `root`

### Common Methods

| Category      | Methods                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| File Info     | `exists()`, `is_file()`, `is_dir()`, `stat()`, `owner()`, `group()`                                            |
| Manipulation  | `with_name()`, `with_suffix()`, `joinpath()`, `relative_to()`, `match()`, `resolve()`                          |
| Traversal     | `iterdir()`, `glob()`, `rglob()`                                                                               |
| File Ops      | `read_text()`, `write_text()`, `read_bytes()`, `write_bytes()`, `touch()`, `unlink()`, `rename()`, `replace()` |
| Directory Ops | `mkdir()`, `rmdir()`                                                                                           |
| PurePath Only | `as_posix()`, `as_uri()`, `is_relative_to()`, `relative_to()`                                                  |

---

# 🧩 9. Key Differences from `os.path`

| `os.path`             | `pathlib`                            |
| --------------------- | ------------------------------------ |
| String-based          | Object-oriented                      |
| Manual concatenation  | Uses `/` operator                    |
| Older, procedural API | Modern, clean API                    |
| Harder cross-platform | Automatically handles OS differences |

---

# ✅ 10. Quick Cheatsheet

```python
from pathlib import Path

p = Path("folder/file.txt")

# Info
p.name           # 'file.txt'
p.suffix         # '.txt'
p.stem           # 'file'
p.parent         # folder

# Check
p.exists()
p.is_file()
p.is_dir()

# Manipulate
p.with_suffix('.csv')
p.with_name('data.txt')
p.resolve()

# I/O
p.read_text()
p.write_text("Hello")

# Directory
for f in p.parent.glob('*.txt'):
    print(f)
```

---
