-- 1077. Project Employees III
select t.project_id, t.employee_id
from
    (select project_id,
    p.employee_id,
    rank() over(partition by project_id order by experience_years desc) as rank
    from Project p join Employee e
    on p.employee_id = e.employee_id) t
where t.rank = 1;