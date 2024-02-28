-- 코드를 입력하세요
SELECT a.PRODUCT_ID, a.PRODUCT_NAME, sum(b.AMOUNT*a.PRICE) as TOTAL_SALES
from FOOD_PRODUCT as a
join FOOD_ORDER as b
on a.PRODUCT_ID=b.PRODUCT_ID
where PRODUCE_DATE like '2022-05%'
group by product_id
order by TOTAL_SALES desc, product_id 