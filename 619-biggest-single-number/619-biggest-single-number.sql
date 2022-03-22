# Write your MySQL query statement below

select max(x.n) as num
from (

select num as n, count(*) as c
from MyNumbers
group by num

) as x
where x.c = 1