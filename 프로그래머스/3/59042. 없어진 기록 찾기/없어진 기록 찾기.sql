-- 코드를 입력하세요 입양간 기록은 있는데 보호소에 들어온 기록이 없는 
select ANIMAL_ID, name from animal_outs
where animal_id not in (SELECT a.animal_id from animal_ins as a
join animal_outs as b
on a.animal_id = b.animal_id)
-- 겹치는 것만
