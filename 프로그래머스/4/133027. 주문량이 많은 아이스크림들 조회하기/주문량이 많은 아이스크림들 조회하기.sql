with Ju as (select FLAVOR, sum(TOTAL_ORDER) as total
from JULY
group by FLAVOR)


select a.FLAVOR
from FIRST_HALF as a
join Ju as j
on a.FLAVOR	=j.FLAVOR
order by (a.TOTAL_ORDER+j.total) desc
limit 3
