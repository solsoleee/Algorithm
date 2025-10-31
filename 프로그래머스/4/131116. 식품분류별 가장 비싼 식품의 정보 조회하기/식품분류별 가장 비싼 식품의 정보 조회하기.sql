-- 코드를 입력하세요
SELECT category, price as MAX_PRICE, product_name 
from FOOD_PRODUCT
where price in (
    SELECT max(price) as MAX_PRICE
    from FOOD_PRODUCT
    group by CATEGORY
)
group by CATEGORY
having CATEGORY in ('과자','국','김치','식용유')
order by MAX_PRICE desc


