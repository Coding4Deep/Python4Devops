## **Python Practice Questions: Logging**

---

### **1. Basic Logging (5 Questions)**

1. Import the `logging` module and log a simple message.
2. Log messages of different severity levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
3. Log a variable value in an `INFO` message.
4. Change the logging format to include timestamp, level, and message.
5. Log a message to only display warnings and above.

---

### **2. Logging to a File (5 Questions)**

6. Configure logging to write messages to a file instead of console.
7. Log messages of different severity levels to a file.
8. Append logs to a file instead of overwriting.
9. Use a custom format when logging to a file.
10. Rotate log files daily using `logging.handlers.TimedRotatingFileHandler`.

---

### **3. Advanced Logging (5 Questions)**

11. Use `logging.getLogger()` to create a custom logger.
12. Set different logging levels for different loggers.
13. Add a file handler and a console handler to a single logger.
14. Use `logging.Formatter` to format messages differently for console and file.
15. Filter log messages using `logging.Filter`.

---

### **4. Exception Logging (5 Questions)**

16. Log exceptions using `logging.exception()` inside a `try/except` block.
17. Log stack trace of an exception without stopping the program.
18. Use `exc_info=True` in `logging.error()` to log traceback.
19. Log multiple exceptions occurring in a loop.
20. Create a decorator that logs exceptions for any function it wraps.

---

### **5. Scenario-Based / DevOps Style (10 Questions)**

21. Write a script that logs server status checks to a file.
22. Log both successful and failed HTTP requests with different levels.
23. Log the start and end of a deployment script with timestamps.
24. Implement a function to log disk usage, warning if usage > 80%.
25. Log user login attempts with `INFO` for success and `WARNING` for failure.
26. Log output of a backup script including success/failure.
27. Create a logger for each server in a cluster (separate log files).
28. Implement logging for a function that processes multiple configuration files, logging errors for invalid files.
29. Log a real-time list of active processes on a server every 5 seconds.
30. Combine logging with exception handling in a network monitoring script.

---

### **6. Bonus / Advanced (5 Questions)**

31. Use `logging.config.dictConfig` to configure logging using a dictionary.
32. Log messages in JSON format for easier ingestion in logging systems like ELK/Prometheus.
33. Implement custom logging level (e.g., `TRACE`).
34. Use `RotatingFileHandler` to rotate log files after reaching a size limit.
35. Implement a function that logs both to console and remote syslog server.

---

This gives you **35+ questions**, covering:

* **Basic logging and severity levels**
* **File and console logging**
* **Advanced handlers, formatters, filters**
* **Exception logging**
* **DevOps-style real-world logging scenarios**

---

