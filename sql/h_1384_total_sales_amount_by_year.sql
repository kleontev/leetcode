-- https://leetcode.com/problems/total-sales-amount-by-year/
select 
    to_char(p.product_id) product_id,
    p.product_name, 
    r.report_year,
    r.total_amount    
from product p 
join (
    select
        product_id, 
        to_char(dates.dt, 'YYYY') report_year, 
        sum(s.average_daily_sales) total_amount
    from (
        select ps + rownum - 1 as dt 
        from (
            select 
                min(period_start) ps, 
                max(period_end) pe
            from sales 
        )
        connect by rownum <= pe - ps + 1 
    ) dates
    join sales s on dates.dt between s.period_start and s.period_end
    group by 
        product_id, 
        to_char(dates.dt, 'YYYY')
) r on p.product_id = r.product_id
order by to_char(p.product_id), r.report_year
