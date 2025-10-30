## **Python Practice Questions: API Interaction (`requests`)**

---

### **1. Basic GET & POST Requests (10 Questions)**

1. Send a simple GET request to `https://jsonplaceholder.typicode.com/posts/1`.
2. Send a POST request to `https://jsonplaceholder.typicode.com/posts` with JSON data.
3. Send a GET request with query parameters (e.g., `?userId=1`).
4. Access and print the response status code.
5. Access and print the response headers.
6. Access and print the response body as JSON.
7. Send a POST request with form-encoded data (`data={...}`).
8. Handle responses that return text instead of JSON.
9. Use `requests.get()` with `timeout=5` seconds.
10. Handle a GET request that raises a `requests.exceptions.Timeout`.

---

### **2. Headers, Cookies, and Authentication (5 Questions)**

11. Send a GET request with custom headers.
12. Send a request with cookies.
13. Use Basic Authentication with `requests`.
14. Use Bearer Token authentication with a header.
15. Send a POST request with both headers and JSON payload.

---

### **3. Error Handling & Response Codes (5 Questions)**

16. Check if the response status code is 200 before processing.
17. Handle 4xx and 5xx HTTP errors using `raise_for_status()`.
18. Retry a failed request 3 times using a loop.
19. Handle network-related exceptions (e.g., `ConnectionError`).
20. Gracefully handle invalid JSON responses.

---

### **4. Advanced Requests (5 Questions)**

21. Send a GET request with query parameters using `params={}`.
22. Send a POST request with file upload (`files={}`) using `requests`.
23. Stream a large response without loading it entirely into memory (`stream=True`).
24. Use a session (`requests.Session()`) to maintain cookies across requests.
25. Set a custom redirect behavior using `allow_redirects=False`.

---

### **5. Scenario-Based / DevOps Style (5 Questions)**

26. Write a script to fetch server status from a REST API and print online/offline.
27. Send a POST request to trigger a deployment and check the response.
28. Write a script to fetch JSON data from multiple endpoints and merge results.
29. Write a script to monitor API latency and log if it exceeds a threshold.
30. Write a function that retries a request with exponential backoff on failure.

---

### **6. Bonus / Practical Exercises (5 Questions)**

31. Fetch a list of users from a public API and filter users from a specific city.
32. Write a function that updates a resource via PUT request.
33. Implement a function to delete a resource using DELETE request.
34. Write a function that paginates through an API and aggregates all results.
35. Fetch data from an API and save it as a JSON file for later processing.

---


