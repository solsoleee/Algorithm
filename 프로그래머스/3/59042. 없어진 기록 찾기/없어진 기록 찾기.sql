-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.name
from ANIMAL_OUTS as a
left join ANIMAL_ins as b
on a.ANIMAL_ID=b.ANIMAL_ID
where b.ANIMAL_ID is null
order by a.animal_id, a.name