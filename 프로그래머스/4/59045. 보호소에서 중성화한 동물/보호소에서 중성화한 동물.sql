-- 코드를 입력하세요
SELECT a.animal_id, a.animal_type, a.name from animal_ins as a
join animal_outs as b
on a.animal_id = b.animal_id
where (a.SEX_UPON_INTAKE="Intact Male" or a.SEX_UPON_INTAKE="Intact Female")
and (b.SEX_UPON_OUTCOME="Neutered Male" or b.SEX_UPON_OUTCOME="Spayed Female")