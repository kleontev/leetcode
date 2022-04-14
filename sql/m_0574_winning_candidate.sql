-- https://leetcode.com/problems/winning-candidate/
select name 
from candidate 
where id = (
    select min(v.candidateid) keep(dense_rank last order by count(*))
    from vote v
    group by candidateid
)
