# TITLE :
	
SQL Queries - all types of Join, Sub-Query and View: Write at least10 SQL queries for suitable database application using SQL DML statements. Note: Instructor will design the queries which demonstrate the use of concepts like all types of Join, Sub-Query and View.
	

Certainly! Below are 10 SQL queries that demonstrate the use of different types of joins, subqueries, and views in a suitable database application:

### SQL DML Queries:

#### 1. Inner Join:

```sql

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

```

#### 2. Left Join:

```sql

SELECT Employees.EmployeeID, Employees.FirstName, Departments.DepartmentName
FROM Employees
LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;

```

#### 3. Right Join:

```sql

SELECT Departments.DepartmentID, Departments.DepartmentName, Employees.FirstName
FROM Departments
RIGHT JOIN Employees ON Departments.DepartmentID = Employees.DepartmentID;

```

#### 4. Full Outer Join:

```sql

SELECT Employees.EmployeeID, Employees.FirstName, Departments.DepartmentName
FROM Employees
FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;

```

#### 5. Cross Join:

```sql

SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
CROSS JOIN Departments;

```

#### 6. Self Join:

```sql

SELECT e1.EmployeeID, e1.FirstName AS EmployeeName, e2.FirstName AS ManagerName
FROM Employees e1
INNER JOIN Employees e2 ON e1.ManagerID = e2.EmployeeID;

```

#### 7. Subquery with IN:

```sql

SELECT ProductName
FROM Products
WHERE SupplierID IN (SELECT SupplierID FROM Suppliers WHERE Country = 'USA');

```

#### 8. Subquery with EXISTS:

```sql

SELECT CustomerName
FROM Customers
WHERE EXISTS (SELECT * FROM Orders WHERE Orders.CustomerID = Customers.CustomerID);

```

#### 9. Subquery with Scalar Subquery:

```sql

SELECT EmployeeID, FirstName, LastName, (SELECT AVG(Salary) FROM Employees) AS AvgSalary
FROM Employees;

```

#### 10. View:
Assuming you have a view named "HighValueOrders" that shows orders with a total value greater than 1000:

```sql

SELECT * FROM HighValueOrders;

```

These queries cover various types of joins (inner, left, right, full outer, cross, and self), subqueries with different operators (IN, EXISTS, scalar subquery), and the use of a view. Adjust the queries based on the structure and requirements of your specific database application.


