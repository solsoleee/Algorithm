-- 코드를 입력하세요
-- 보호 기간이 가장 길었던 동물
-- ins에서 가장 먼저 들어오고 out에서 가장 나중에 나간
-- out - ins 가 가장 큰거
SELECT a.animal_id, a.name from ANIMAL_INS as a
join ANIMAL_OUTS as b
on a.animal_id = b.animal_id
order by b.DATETIME - a.DATETIME desc
limit 2