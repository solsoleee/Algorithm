-- 코드를 입력하세요
SELECT a.FLAVOR
from FIRST_HALF as a
join ICECREAM_INFO as b 
on a.flavor = b.flavor
where total_order>3000
and INGREDIENT_TYPE='fruit_based'
order by total_order desc;
