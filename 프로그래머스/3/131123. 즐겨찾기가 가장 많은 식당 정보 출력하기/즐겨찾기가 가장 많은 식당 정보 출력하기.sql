-- 코드를 입력하세요
SELECT FOOD_TYPE,	REST_ID,	REST_NAME,	FAVORITES
from rest_info
where (food_type, favorites) in
    (select food_type, max(FAVORITES)
     from rest_info
    group by 1)
order by food_type desc