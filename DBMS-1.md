# TITLE :

SQL Queries:
* Design and Develop SQL DDL statements which demonstrate the use of SQL objects such as Table, View, Index, Sequence, Synonym, different constraints etc.
* Write at least 10 SQL queries on the suitable database application using SQL DML statements.


Certainly! Below are examples of SQL DDL (Data Definition Language) statements to create various SQL objects, followed by 10 SQL DML (Data Manipulation Language) queries:

### SQL DDL Statements:

#### 1. Create Table:
```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Salary DECIMAL(10, 2)
);
```

#### 2. Create View:
```sql
CREATE VIEW HighSalaryEmployees AS
SELECT * FROM Employees WHERE Salary > 50000;
```

#### 3. Create Index:
```sql
CREATE INDEX idx_LastName ON Employees(LastName);
```

#### 4. Create Sequence:
```sql
CREATE SEQUENCE EmployeeSeq START WITH 1 INCREMENT BY 1;
```

#### 5. Create Synonym:
```sql
CREATE SYNONYM EmpSynonym FOR Employees;
```

#### 6. Add Primary Key Constraint:
```sql
ALTER TABLE Employees
ADD CONSTRAINT PK_EmployeeID PRIMARY KEY (EmployeeID);
```

#### 7. Add Foreign Key Constraint:
```sql
ALTER TABLE Orders
ADD CONSTRAINT FK_EmployeeID
FOREIGN KEY (EmployeeID)
REFERENCES Employees(EmployeeID);
```

#### 8. Add Check Constraint:
```sql
ALTER TABLE Employees
ADD CONSTRAINT CHK_Age CHECK (Age >= 18);
```

#### 9. Add Unique Constraint:
```sql
ALTER TABLE Employees
ADD CONSTRAINT UQ_Email UNIQUE (Email);
```

#### 10. Add Default Constraint:
```sql
ALTER TABLE Employees
MODIFY COLUMN Country VARCHAR(50) DEFAULT 'USA';
```

### SQL DML Queries:

#### 1. Insert Data:
```sql
INSERT INTO Employees (EmployeeID, FirstName, LastName, Age, Salary)
VALUES (1, 'John', 'Doe', 30, 60000);
```

#### 2. Update Data:
```sql
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;
```

#### 3. Delete Data:
```sql
DELETE FROM Employees
WHERE EmployeeID = 1;
```

#### 4. Select with Join:
```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

#### 5. Aggregate Function:
```sql
SELECT AVG(Salary) AS AverageSalary
FROM Employees;
```

#### 6. Subquery:
```sql
SELECT FirstName, LastName
FROM Employees
WHERE DepartmentID IN (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'IT');
```

#### 7. Group By:
```sql
SELECT DepartmentID, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentID;
```

#### 8. Order By:
```sql
SELECT FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
```

#### 9. Limit Rows:
```sql
SELECT *
FROM Employees
LIMIT 10;
```

#### 10. Conditional Query:
```sql
SELECT FirstName, LastName
FROM Employees
WHERE Age > 25 AND Salary > 50000;
```

These examples cover a range of SQL DDL and DML operations on different SQL objects. Adjust the statements according to the specific requirements and structure of your database.