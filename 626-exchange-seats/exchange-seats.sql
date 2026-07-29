# Write your MySQL query statement below
-- select s1.id,s2.student from seat as s1
-- join seat as s2 on s2.id-s1.id=1 
-- where s1.id%2=1
-- union
-- select s3.id,s4.student from seat as s3
-- join seat as s4 on s4.id-s3.id=-1
-- where s3.id%2=0
-- order by id
select s1.id,ifnull(s2.student,s1.student) as student from seat as s1
left join seat as s2 on s2.id-s1.id=1 
where s1.id%2=1
union
select s3.id,s4.student from seat as s3
join seat as s4 on s4.id-s3.id=-1
where s3.id%2=0
order by id