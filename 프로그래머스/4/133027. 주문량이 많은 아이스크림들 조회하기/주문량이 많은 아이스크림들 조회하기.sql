-- 코드를 입력하세요
with j as(
select FLAVOR, sum(total_order) as total
from july
group by flavor
)

SELECT a.flavor
from FIRST_HALF as a
join j as b
on a.FLAVOR=b.FLAVOR
order by a.total_order + b.total  desc
limit 3