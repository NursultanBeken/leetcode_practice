SELECT
    id,
    first_name,
    department,
    gross_salary,
    ROUND(
        CAST(gross_salary AS numeric(9,2)) / SUM(gross_salary) OVER (PARTITION BY department) * 100
        , 2) as dep_ratio,
    ROUND(CAST(gross_salary AS numeric(9,2)) / SUM(gross_salary) OVER () * 100, 2) as total_ratio
FROM Salary
ORDER BY department, dep_ratio DESC;