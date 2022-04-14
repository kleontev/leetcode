-- https://leetcode.com/problems/median-employee-salary/
select 
    id, 
    company, 
    salary
from 
(
    select 
        e.*,
        count(*) over (partition by company) cnt, 
        row_number() over(partition by company order by salary) rnk
    from employee e 
) 
where rnk in (
    floor((cnt + 1) / 2), 
    ceil((cnt + 1) / 2)
)