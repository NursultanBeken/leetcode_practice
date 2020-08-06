select
round(  sum(1.00*per_date)/count( action_date ) , 2 ) as average_daily_percent
from (

        select 
        act.action_date,
        count (case when remove_date is not null then post_id else null end )* 100/ count(distinct act.post_id)  as per_date
        
        
        from Actions act 
        left join Removals rem
        on act.post_id=rem.post_id
        where extra in ('spam')
        group by act.action_date
) a;



select ROUND(sum(daily_avg)/count(date)*100,2) as average_daily_percent FROM
(select 
    t.action_date as date,
    (count(distinct case when remove_date is not null then post_id else null end)/count(distinct post_id)) as daily_avg
FROM
(
    SELECT a.post_id, a.action_date, r.remove_date
    from Actions a left join Removals r
    on a.post_id = r.post_id
WHERE a.extra='spam'
) t
GROUP BY t.action_date) t2;