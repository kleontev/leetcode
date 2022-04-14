-- https://leetcode.com/problems/game-play-analysis-v
select 
    to_char(install_date, 'YYYY-MM-DD') install_dt,
    count(*) installs,
    round(avg(returned_next_day), 2) day1_retention
from (
    select 
        player_id,
        first_value(event_date) over(
            partition by player_id 
            order by event_date
        ) install_date,
        event_date, 
        count(*) over(
            partition by player_id 
            order by event_date 
            range between 1 following and 1 following
        ) returned_next_day
    from activity
) where event_date = install_date
group by to_char(install_date, 'YYYY-MM-DD')
