Everything I found in glasdoor

```
            # sales                                       # products
        # +------------------+---------+         +---------------------+---------+
        # | product_id | INTEGER       |>--------| product_id | INTEGER          |
        # | store_id | INTEGER         | +---<   | product_class_id | INTEGER    |
        # | customer_id | INTEGER      | |       | brand_name | VARCHAR          |
     +---<| promotion_id | INTEGER     | |       | product_name | VARCHAR        |
    #|    | store_sales | DECIMAL      | |       | is_low_fat_flg | TINYINT      |
     |    | store_cost | DECIMAL       | |       | is_recyclable_flg | TINYINT   |
     |    | units_sold | DECIMAL       | |       | gross_weight | DECIMAL        |
     |    | transaction_date | DATE    | |       | net_weight | DECIMAL          |
     |    +------------------+-------+   |       +---------------------+---------+
     |                                   | 
     |      # promotions                 |             # product_classes
     |    +------------------+---------+ |    +---------------------+---------+
     +----| promotion_id | INTEGER     | +----| product_class_id | INTEGER    |
          | promotion_name | VARCHAR   |      | product_subcategory | VARCHAR |
          | media_type | VARCHAR       |      | product_category | VARCHAR    |
          | cost | DECIMAL             |      | product_department | VARCHAR  |
          | start_date | DATE          |      | product_family | VARCHAR      |
          | end_date | DATE            |      +---------------------+---------+
          +------------------+---------+
```

###########SQL
### Question 1:
 -- What percent of all products in the grocery chain's catalog
 -- are both low fat and recyclable?

```
select 
count( case 
        when is_low_fat_flg ='Y' and is_recyclable_flg ='Y' then product id 
        end) * 100
/ count(product_id) as total
from products;
```

### Question 2:
-- What are the top five (ranked in decreasing order)
-- single-channel media types that correspond to the most money
-- the grocery chain had spent on its promotional campaigns?

```
select promotion_name
from promotions
where media_type='single-channel'
order by cost desc
limit 5
```

### Question 3:
-- % Of sales that had a valid promotion, the VP of marketing
-- wants to know what % of transactions occur on either
-- the very first day or the very last day of a promotion campaign.

```
select count(*) as total_num_of_transactions  from sales ;
--
select count(*) as num_of_transactions_in_promotion_date
from sales
join promotions on promotions.promotion_id = sales.promotion_id
where transaction_date = start_date or transaction_date = end_date;

select
(

) *100 / count(*) as 
from sales
join promotions on promotions.promotion_id = sales.promotion_id
```

```
products                                sales
+------------------+---------+        +------------------+---------+
| product_id | int           |------->| product_id | int           |
| product_class_id | int     | +----> | store_id | int             |
| brand_name | varchar       | | +->  | customer_id | int          |
| product_name | varchar     | | |    | promotion_id | int         |
| price | int                | | |    | store_sales | decimal      |
+------------------+---------+ | |    | store_cost | decimal       |
                               | |    | units_sold | decimal       |
                               | |    | transaction_date | date    |
                               | |    +------------------+---------+
                               | |
stores                         | |   customers
+-------------------+--------+ | |  +---------------------+---------+
| store_id | int             |-+ +--| customer_id | int             |
| type | varchar             |      | first_name | varchar          |
| name | varchar             |      | last_name | varchar           |
| state | varchar            |      | state | varchar               |     
| first_opened_date| datetime|      | birthdate | date              |
| last_remodel_date |datetime|      | education | varchar           |
| area_sqft | int            |      | gender | varchar              |
+-------------------+--------+      | date_account_opened | date    |
                                    +---------------------+---------+

```

### Question 1:
-- What brands have an average price above $3 and contain at least 2 different products?

```
select brand_name
from products
group by brand_name
having avg(price) > 3
and count(distinct product_id) >= 2
```

### Question 2:
To improve sales, the marketing department runs various types of promotions.
The marketing manager would like to analyze the effectiveness of these promotion campaigns.
In particular, what percent of our sales transactions had a valid promotion applied?

### Question 3:
 -- We want to run a new promotion for our most successful category of products
 -- (we call these categories “product classes”).
 -- Can you find out what are the top 3 selling product classes by total sales?

Question to clarify : total sales for some specific date?

```
select product_class_id
from sales 
join products on products.product_id = sales.product_id
group by product_class_id
order by sum(store_sales) desc
limit 3
```

### Question 4:
 -- We are considering running a promo across brands. We want to target
 -- customers who have bought products from two specific brands.
 -- Can you find out which customers have bought products from both the
 -- “Fort West" and the "Golden" brands?  

```
select customer_id
from customers
join sales on sales.customer_id = customers.customer_id
join products on products.product_id = sales.product_id
group by customer_id
having sum( case when products.brand_name = “Fort West"  then 1 else 0 end) > 0 
and sum( case when products.brand_name = “Golden"  then 1 else 0 end) > 0 
```

```
employees                             projects
+---------------+---------+           +---------------+---------+
| id            | int     |<----+  +->| id            | int     |
| first_name    | varchar |     |  |  | title         | varchar |
| last_name     | varchar |     |  |  | start_date    | date    |
| salary        | int     |     |  |  | end_date      | date    |
| department_id | int     |--+  |  |  | budget        | int     |
+---------------+---------+  |  |  |  +---------------+---------+
                             |  |  |
departments                  |  |  |  employees_projects
+---------------+---------+  |  |  |  +---------------+---------+
| id            | int     |<-+  |  +--| project_id    | int     |
| name          | varchar |     +-----| employee_id   | int     |
+---------------+---------+           +---------------+---------+
*/
```




-- a. The names of all salespeople that have an order with Samsonic. 

-- b. The names of all salespeople that do not have any order with Samsonic. 

-- c. The names of salespeople that have 2 or more orders. 

-- d. The names and ages of all salespersons must having a salary of 100,000 or greater.

-- e. What sales people have sold more than 1400 total units?

-- f. When was the earliest and latest order made to Samony?