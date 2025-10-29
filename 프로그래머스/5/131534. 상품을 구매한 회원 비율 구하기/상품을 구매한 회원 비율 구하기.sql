SELECT Year(b.SALES_DATE) as Year, Month(b.SALES_DATE) as month, count (distinct (a.user_id)) as PURCHASED_USERS, round (count(distinct (a.user_id)) / (SELECT count(*) from user_info as a
where Year(a.JOINED)=2021) ,1) as PUCHASED_RATIO
from user_info as a
join online_sale as b
on a.user_id = b.user_id
where Year(a.JOINED)=2021
group by Year(b.SALES_DATE), Month(b.SALES_DATE)
order by Year(b.SALES_DATE) asc, Month(b.SALES_DATE) asc