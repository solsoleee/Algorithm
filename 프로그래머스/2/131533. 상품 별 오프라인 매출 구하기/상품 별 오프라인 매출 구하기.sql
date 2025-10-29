-- 코드를 입력하세요
SELECT a.PRODUCT_CODE,(sum(b.sales_amount) * a.price)as SALES from product as a
join offline_sale as b
on a.PRODUCT_ID	=b.PRODUCT_ID
group by a.PRODUCT_CODE
order by sales desc, a.PRODUCT_CODE asc
-- select * from offline_sale