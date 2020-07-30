 -- 1076. Project Employees II
-- Write an SQL query that reports all the projects that have the most employees.

SELECT project_id
FROM project
GROUP BY project_id
HAVING COUNT(employee_id) =
(
    SELECT count(employee_id)
    FROM project
    GROUP BY project_id
    ORDER BY count(employee_id) desc
    LIMIT 1
);



select a.project_id
from 
(
    select  project_id, count(distinct employee_id) as cnt_emp
    from Project pr
    group by project_id
 ) a
join
( 
    select project_id,
    count(distinct employee_id) as max_emp
    from Project pr
    group by project_id
    order by max_emp desc
    limit 1
) b
on a.cnt_emp=b.max_emp;