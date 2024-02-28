-- 코드를 입력하세요
SELECT a.AUTHOR_ID,	a.AUTHOR_NAME,	b.CATEGORY, sum(c.SALES*b.PRICE) as TOTAL_SALES
from BOOK as b
join AUTHOR as a on a.author_id = b.author_id
join BOOK_SALES as c on b.book_id=c.book_id
where year(c.SALES_DATE)=2022 and month(c.SALES_DATE)=1
group by a.AUTHOR_NAME, b.CATEGORY
order by a.author_id asc, b.CATEGORY desc