select Customers.customer_id, Customers.customer_name
  from Customers join
  (
  
  select customer_id
    from Orders
        where product_name in ('A', 'B')
        group by customer_id
        having count(distinct product_name) > 1 
    EXCEPT
    select distinct customer_id
    from Orders
        where product_name='C'
  ) tmp
  on tmp.customer_id=Customers.customer_id;



select a.customer_id, a.customer_name
from customers a , orders b
where a.customer_id  = b.customer_id
group by a.customer_id
having sum(b.product_name="A") >0 and sum(b.product_name="B") > 0 and sum(b.product_name="C")=0