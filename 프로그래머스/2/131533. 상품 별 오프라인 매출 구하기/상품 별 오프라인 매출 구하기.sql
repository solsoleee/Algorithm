-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, (a.PRICE * sum(b.SALES_AMOUNT)) as SALES
from PRODUCT as a 
join offline_sale as b
on a.PRODUCT_ID=b.PRODUCT_ID
group by b.product_id
order by sales desc, product_code asc