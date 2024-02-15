-- 코드를 입력하세요
SELECT a.INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from icecream_info as a
join FIRST_HALF as b
on a.flavor=b.flavor
group by a.INGREDIENT_TYPE
