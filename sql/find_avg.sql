-- 1142. User Activity for the Past 30 Days II


SELECT ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id), 2),0.00) 
AS average_sessions_per_user
FROM Activity 
WHERE activity_date >= '2019-06-28' and activity_date <= '2019-07-27'; 


SELECT
CASE 
WHEN COUNT(DISTINCT user_id) = 0 THEN 0
WHEN COUNT(DISTINCT user_id) != 0 THEN ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id),2)
END AS average_sessions_per_user
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27';

select 
nvl(
    ROUND(
    sum(ses_cnt_per_user)/count(distinct user_id),
    2), 0.00 ) as average_sessions_per_user
from (
    select user_id, count(*) as ses_cnt_per_user
     from Activity a
     where a.activity_date <= '2019-07-27' and a.activity_date>='2019-06-28'
     and activity_type not in ('open_session', 'end_session')
     group by user_id, session_id
);