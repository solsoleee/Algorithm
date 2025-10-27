-- 코드를 입력하세요
SELECT a.product_id, product_name,  sum(a.PRICE * b.AMOUNT) as TOTAL_SALES from food_product as a
join food_order as b
on a.product_id = b.product_id
where (PRODUCE_DATE >= '2022-05-01' and PRODUCE_DATE <='2022-05-31')
group by a. PRODUCT_id
order by (TOTAL_SALES ) desc,product_id asc  # 총매출


-- a.product_id, product_name, product_cd, category, a.PRICE * b.AMOUNT