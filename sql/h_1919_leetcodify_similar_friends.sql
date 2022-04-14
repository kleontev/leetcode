-- https://leetcode.com/problems/leetcodify-similar-friends/
select distinct
    u1.user_id user1_id, 
    u2.user_id user2_id    
from listens u1
join listens u2 on 1 = 1 
    and u2.song_id = u1.song_id
    and u2.day = u1.day 
    and u2.user_id > u1.user_id
where exists (
    select null 
    from friendship f 
    where 1 = 1 
        and f.user1_id = u1.user_id
        and f.user2_id = u2.user_id
)
group by 
    u1.day,
    u1.user_id,
    u2.user_id
having count(distinct u1.song_id) >= 3
