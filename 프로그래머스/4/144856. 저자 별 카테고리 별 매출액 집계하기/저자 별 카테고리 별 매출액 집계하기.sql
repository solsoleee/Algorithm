-- 코드를 입력하세요
SELECT b.AUTHOR_ID, b.AUTHOR_NAME, a.category, sum(c.SALES*a.PRICE) as TOTAL_SALES 
from book as a
join AUTHOR as b
on a.AUTHOR_ID=b.AUTHOR_ID
join BOOK_SALES as c
on a.BOOK_ID=c.book_id
where c.sales_date like '2022-01%'
group by a.AUTHOR_ID, a.category
order by b.AUTHOR_ID , a.category desc

-- select * from BOOK_SALES