# Write your MySQL query statement below
select person_name
from (select *, sum(weight) over (order by turn asc) as total from queue 
) as t
where total<=1000
order by turn desc
limit 1