/* Write your T-SQL query statement below */
SELECT e.Name AS Employee
FROM Employee e
LEFT JOIN Employee m ON m.Id = e.ManagerId
WHERE e.Salary > m.Salary