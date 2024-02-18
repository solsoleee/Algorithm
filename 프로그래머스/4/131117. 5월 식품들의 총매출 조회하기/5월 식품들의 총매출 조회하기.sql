-- 코드를 입력하세요
SELECT a.PRODUCT_ID, a.PRODUCT_NAME,sum(a.PRICE * b.AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT as a
join food_order as b
on a.product_id = b.product_id
where date_format(b.PRODUCE_DATE, '%Y-%m') = '2022-05'
group by a.product_id, a.PRODUCT_NAME
order by TOTAL_SALES desc, product_id
