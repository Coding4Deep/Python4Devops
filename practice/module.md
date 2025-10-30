## **Python Practice Questions: Modules for DevOps**

---

### **1. pathlib (5 Questions)**

1. Create a `Path` object for a file.
2. Check if a file or directory exists using `Path.exists()`.
3. Create a new directory using `Path.mkdir()`.
4. Iterate over all `.txt` files in a directory.
5. Get the parent directory, name, and suffix of a file path.

---

### **2. python-dotenv (5 Questions)**

6. Load environment variables from a `.env` file using `load_dotenv()`.
7. Access an environment variable using `os.getenv()`.
8. Set a default value for a missing environment variable.
9. Write a function to validate required environment variables.
10. Update or add a variable in the `.env` file programmatically.

---

### **3. shutil (5 Questions)**

11. Copy a file from one location to another.
12. Copy a directory recursively.
13. Move a file or directory.
14. Delete a directory tree.
15. Get disk usage statistics using `shutil.disk_usage()`.

---

### **4. os (5 Questions)**

16. Get the current working directory.
17. List all files and directories in a path.
18. Create and remove directories.
19. Check if a path is a file or a directory.
20. Set, get, and delete environment variables using `os.environ`.

---

### **5. subprocess (5 Questions)**

21. Run a shell command using `subprocess.run()`.
22. Capture the output of a shell command.
23. Run a command and handle errors using `check=True`.
24. Run a long-running command and capture stdout/stderr.
25. Use `subprocess.Popen()` to run a command asynchronously.

---

### **6. sys (5 Questions)**

26. Print command-line arguments using `sys.argv`.
27. Exit a script with a specific exit code using `sys.exit()`.
28. Print the Python version and platform information.
29. Redirect stdout to a file using `sys.stdout`.
30. Check and modify the Python module search path (`sys.path`).

---

### **7. Scenario-Based / DevOps Style (10 Questions)**

31. Write a script to read a `.env` file and validate API keys.
32. Write a script to backup a directory using `shutil` and `pathlib`.
33. List all `.log` files in a directory and delete files older than 7 days.
34. Write a script to get free disk space using `shutil.disk_usage()` and log it.
35. Run a shell command to check server uptime and log the result.
36. Run multiple shell commands sequentially and capture outputs.
37. Write a script to parse command-line arguments and execute actions.
38. Check if a configuration file exists, and if not, create it using `pathlib`.
39. Move log files to an archive directory using `shutil.move()`.
40. Exit a script gracefully with a custom error message if an environment variable is missing.

---

This gives you **40+ questions**, covering:

* **File & directory manipulation** (`pathlib`, `shutil`, `os`)
* **Environment variables** (`python-dotenv`, `os`)
* **Subprocess management** (`subprocess`)
* **Script interaction & system info** (`sys`)
* **Scenario-based DevOps automation tasks**

---

