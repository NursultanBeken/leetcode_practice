-- 1159. Market Analysis II
with ranking as (
Select o.order_id, 
    o.order_date,
    o.item_id, 
    o.buyer_id,
    o.seller_id as seller_id, 
    i.item_brand as item_brand, 
    rank() over (partition by seller_id order by order_date) as r
From Orders o, Items i
Where o.item_id = i.item_id
)

Select u.user_id as seller_id, 
Case When u.favorite_brand = r.item_brand then 'yes'
else 'no'
end as 2nd_item_fav_brand

From ranking r 
right join users u
on r.seller_id = u.user_id
And r = 2