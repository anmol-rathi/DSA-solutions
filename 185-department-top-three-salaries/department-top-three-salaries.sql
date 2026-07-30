# Write your MySQL query statement below
select d.name as Department, e.name as Employee, salary
from employee as e
join department as d on d.id=e.departmentId
where 3> (select count(distinct e2.salary) from employee as e2 where e2.salary >e.salary and e2.departmentId=e.departmentId)
