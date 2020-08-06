select Department.Name as Department, emp_out.Name as Employee, emp_out.Salary
from Employee emp_out  join Department on Department.Id = emp_out.DepartmentId
    
where 3 > (
select count(distinct emp_iner.salary)
    from Employee emp_iner
    where emp_out.Salary < emp_iner.salary
    and emp_out.DepartmentId=emp_iner.DepartmentId
);