# Write your MySQL query statement below
select distinct l1.num as ConsecutiveNums
from logs as l1
join logs as l2 on l1.num = l2.num and l2.id-l1.id=1
join logs as l3 on l3.num= l1.num and l3.id-l1.id=2
