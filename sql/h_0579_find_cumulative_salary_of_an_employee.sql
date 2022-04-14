-- https://leetcode.com/problems/find-cumulative-salary-of-an-employee/

select 
    id, 
    month,
    salary
from ( 
    select 
        id,
        month,
        sum(salary) over(
            partition by id 
            order by month 
            range between 2 preceding and current row
        ) salary,
        decode(
            lead(month) over(
                partition by id
                order by month
            ),
            null,
            'Y',
            'N'
        ) is_last_month
    from employee 
) 
where is_last_month = 'N'
order by id, month desc

