-- 코드를 입력하세요
SELECT b.ANIMAL_ID,	b.NAME
from ANIMAL_INS as a
right join animal_outs as b
on a.animal_id=b.animal_id
where a.animal_id is null
order by b.animal_id, b.name