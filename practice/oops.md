## **Python Practice Questions: Classes & OOP**

### **1. Basic Class & Object (10 Questions)**

1. Define a simple class `Car` with no attributes or methods.
2. Create an object of the class `Car`.
3. Add an attribute `brand` to the `Car` class and initialize it.
4. Print the value of the `brand` attribute of a `Car` object.
5. Add a method `start()` that prints `"Car started"`.
6. Call the `start()` method of a `Car` object.
7. Add an `__init__` constructor to initialize `brand` and `model`.
8. Print all attributes of an object using `__dict__`.
9. Add a class attribute `wheels = 4` and access it using the class name and object.
10. Try creating an object without passing required `__init__` parameters (observe what happens).

---

### **2. Instance & Class Methods (5 Questions)**

11. Add an instance method `full_name()` that returns `brand + model`.
12. Add a class method to change the class attribute `wheels`.
13. Call a class method without creating an object.
14. Add a static method `vehicle_type()` that prints `"Vehicle"`.
15. Call a static method using both class and object.

---

### **3. Encapsulation (5 Questions)**

16. Create a private attribute `__speed` and try accessing it outside the class.
17. Add a getter method to access `__speed`.
18. Add a setter method to modify `__speed`.
19. Demonstrate Python’s name mangling for private variables.
20. Try modifying a private attribute directly and observe behavior.

---

### **4. Inheritance (10 Questions)**

21. Create a class `Vehicle` and inherit it in class `Car`.
22. Add a method `vehicle_type()` in `Vehicle` and call it from `Car` object.
23. Override a method in child class.
24. Use `super()` to call parent class method.
25. Multiple inheritance: create another class `Flyable` and inherit `Vehicle` and `Flyable` in `FlyingCar`.
26. Demonstrate method resolution order (MRO) with `FlyingCar`.
27. Check `issubclass(Car, Vehicle)` and `isinstance(car_obj, Vehicle)`.
28. Call parent constructor from child class using `super().__init__()`.
29. Add attributes in child class and access both parent and child attributes.
30. Create a `Bike` class inheriting `Vehicle` and override a class attribute.

---

### **5. Polymorphism & Magic Methods (10 Questions)**

31. Demonstrate method overloading using default arguments.
32. Demonstrate operator overloading with `__add__` for a class `Vector`.
33. Override `__str__` method to customize object print.
34. Override `__repr__` method and compare with `__str__`.
35. Implement `__len__` to get the “length” of an object.
36. Implement `__eq__` to compare two objects.
37. Demonstrate duck typing with two unrelated classes having the same method.
38. Use a function to call the same method on different object types.
39. Implement `__getitem__` to make an object subscriptable.
40. Implement `__setitem__` to allow modifying elements using index.

---

### **6. Advanced OOP Concepts (10 Questions)**

41. Create an abstract base class using `abc` module and inherit it.
42. Implement abstract methods in child class.
43. Demonstrate interface-like behavior in Python.
44. Use `@property` decorator to create a getter for a private attribute.
45. Use `@attribute.setter` decorator to create a setter.
46. Demonstrate class variable vs instance variable.
47. Implement a singleton pattern.
48. Demonstrate method chaining by returning `self`.
49. Create a mixin class and use it in multiple inheritance.
50. Use `__slots__` to restrict dynamic attribute creation.

---

### **7. Scenario-Based / DevOps Style (5 Questions)**

51. Create a `Server` class with attributes `IP` and `status`. Add methods to start, stop, and restart server.
52. Create a list of `Server` objects and loop through them to start all servers.
53. Add a method to a class that logs actions to a file (simulate logging in DevOps).
54. Create a `DockerContainer` class inheriting `Server`, adding container-specific methods.
55. Implement a method in `Server` to check if the IP address is valid.

