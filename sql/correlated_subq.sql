-- 177	Nth Highest Salary   

select max(salary) as  SecondHighestSalary
from Employee outer_tab
where (
    select count(1)
    from ( select distinct salary from Employee) iner_tab
    where iner_tab.salary > outer_tab.salary
) = N - 1;