-- 코드를 입력하세요
SELECT a.NAME, a.DATETIME
from ANIMAL_INS as a
left join ANIMAL_OUTS as b
on a.animal_id=b.animal_id
where b.ANIMAL_ID is null
order by a.DATETIME
limit 3