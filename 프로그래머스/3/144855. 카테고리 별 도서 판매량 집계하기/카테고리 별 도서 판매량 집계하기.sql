-- 코드를 입력하세요
SELECT a.CATEGORY, sum(b.SALES) as TOTAL_SALES
from book as a
join book_sales as b on a.book_id=b.book_id
where year(b.SALES_DATE)=2022 and month(b.SALES_DATE)=1
group by CATEGORY
order by a.category
