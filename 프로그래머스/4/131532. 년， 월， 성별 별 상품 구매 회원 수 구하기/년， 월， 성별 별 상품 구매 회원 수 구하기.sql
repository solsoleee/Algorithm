-- 코드를 입력하세요 ,, 
SELECT year(b.sales_date) as year, month(b.sales_date) as month, a.gender,
count(distinct a.user_id) as users
from user_info as a
join online_sale as b
on a.user_id=b.user_id
group by month, a.gender, year
having a.gender is not null
order by 1, 2, 3