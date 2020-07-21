-- Friend Requests II: Who Has the Most Friends

select 
a.id, count(*) as num
from 
(
    select requester_id as id, accepter_id
    from request_accepted
    union all
    select accepter_id, requester_id
    from request_accepted 
) a
group by a.id
order by num desc
limit 1;