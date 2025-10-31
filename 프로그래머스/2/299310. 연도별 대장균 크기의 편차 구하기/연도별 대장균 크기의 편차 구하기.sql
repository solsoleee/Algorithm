-- 코드를 작성해주세요

-- 그 연에 해당하는 max만 서브 쿼리로 구하기

select Year(DIFFERENTIATION_DATE) as year, 
((select max(size_of_colony) from ecoli_data where YEAR(DIFFERENTIATION_DATE) = year ) - SIZE_OF_COLONY) as YEAR_DEV, 
id
from ecoli_data
order by year asc,YEAR_DEV asc
