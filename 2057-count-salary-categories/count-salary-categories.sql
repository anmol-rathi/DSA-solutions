# Write your MySQL query statement below
SELECT 'Low Salary' AS category, 
       COUNT(if(income<20000,1,null)) AS accounts_count
FROM Accounts
UNION ALL
SELECT 'Average Salary', 
       COUNT(if(income>=20000 and income<=50000,1,null))
FROM Accounts
UNION ALL
SELECT 'High Salary', 
       COUNT(if(income>50000,1,null))
FROM Accounts;
-- select case when income<20000 then 'Low Salary'
--             when income between 20000 and 50000 then 'Average Salary'
--             else 'High Salary' end as category, ifnull(count(account_id),0) as accounts_count
-- from accounts
-- group by category