-- 코드를 입력하세요
SELECT a.USER_ID, a.NICKNAME, concat(a.CITY, ' ', a.STREET_ADDRESS1, ' ' ,a.STREET_ADDRESS2) as 전체주소, concat(substring(a.TLNO, 1, 3), '-', substring(a.TLNO, 4, 4), '-', substring(a.TLNO, 8, 4)) as 전화번호
from USED_GOODS_USER as a
join USED_GOODS_BOARD as b
on a.user_id =b.WRITER_ID
group by 1
having count(*) >=3
order by 1 desc