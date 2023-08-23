-- 1.1 Basic SQL Operations:
-- SELECT: Fetches data from a table.

SELECT column1, column2 FROM table_name;
WHERE: Filters records based on a condition.

SELECT column1, column2 FROM table_name WHERE condition;
JOIN: Combines rows from two or more tables based on a related column.

SELECT orders.order_id, customers.customer_name 
FROM orders 
JOIN customers ON orders.customer_id = customers.customer_id;
GROUP BY: Groups rows that have the same values in specified columns.

SELECT column1, COUNT(column2) 
FROM table_name 
GROUP BY column1;
ORDER BY: Sorts the result set in ascending or descending order.

SELECT column1, column2 
FROM table_name 
ORDER BY column1 ASC;