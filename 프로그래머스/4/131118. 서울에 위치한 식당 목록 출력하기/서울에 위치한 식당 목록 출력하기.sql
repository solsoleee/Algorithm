-- 코드를 입력하세요 
SELECT a.rest_id, a.rest_name, a.food_type, a.favorites, a.address, round(avg(b.review_score),2) as score
from rest_info as a
join rest_review as b
on a.rest_id = b.rest_id
where a.address like '서울%'
group by b.rest_id
order by score desc, a.favorites desc