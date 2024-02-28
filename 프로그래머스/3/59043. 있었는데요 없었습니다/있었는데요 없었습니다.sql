-- 코드를 입력하세요
SELECT a.ANIMAL_ID,	a.NAME
from ANIMAL_INS as a
join animal_outs as b
on a.animal_id = b.animal_id
where a.datetime > b.datetime
order by a.datetime 