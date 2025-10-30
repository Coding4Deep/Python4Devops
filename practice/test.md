## **Python Practice Questions: Testing, Fixtures, Mocking**

---

### **1. Basics of Testing (5 Questions)**

1. Write a simple function and test it using `assert`.
2. Write a function that adds two numbers and test it with multiple cases.
3. Test a function that returns a string in uppercase.
4. Write a failing test to see how Python asserts fail.
5. Write a function that divides two numbers and test for `ZeroDivisionError`.

---

### **2. `unittest` Module (10 Questions)**

6. Create a test class inheriting from `unittest.TestCase`.
7. Write a test method to check equality using `assertEqual()`.
8. Test for exceptions using `assertRaises()`.
9. Test boolean conditions using `assertTrue()` and `assertFalse()`.
10. Run tests using `unittest.main()`.
11. Use `setUp()` method to initialize data before each test.
12. Use `tearDown()` method to clean up after each test.
13. Use `setUpClass()` and `tearDownClass()` for class-level setup.
14. Skip a test using `@unittest.skip()`.
15. Test floating-point equality using `assertAlmostEqual()`.

---

### **3. `pytest` Basics (5 Questions)**

16. Write a simple test function using `pytest`.
17. Use `pytest.raises()` to test for exceptions.
18. Parametrize a test to run multiple inputs using `@pytest.mark.parametrize`.
19. Run `pytest` from the command line and generate a report.
20. Use `pytest` to skip a test conditionally.

---

### **4. Fixtures in `pytest` (5 Questions)**

21. Create a simple fixture using `@pytest.fixture`.
22. Use a fixture to provide input data for multiple test functions.
23. Demonstrate fixture scope: `function`, `module`, `session`.
24. Use `yield` in a fixture for setup and teardown.
25. Chain fixtures: use one fixture as input to another.

---

### **5. Mocking Basics (5 Questions)**

26. Use `unittest.mock.Mock` to mock a function.
27. Set a return value for a mock object.
28. Use `side_effect` to raise an exception from a mock.
29. Mock a method in a class using `patch()`.
30. Mock a module-level function used inside another function.

---

### **6. Advanced Mocking / Scenario-Based (5 Questions)**

31. Mock an API call using `requests.get`.
32. Mock a database connection and test CRUD operations.
33. Test a function with multiple external dependencies using multiple mocks.
34. Use `patch.object()` to mock an object method temporarily.
35. Verify that a mock function was called with specific arguments.

---

### **7. Scenario-Based / DevOps Style Testing (5 Questions)**

36. Write tests for a server monitoring function that returns CPU usage.
37. Test a deployment script function that triggers shell commands.
38. Mock reading a configuration file to test a parser function.
39. Test a function that sends alerts (mock email or Slack API).
40. Write tests for a log parser function, mocking log file inputs.

---


