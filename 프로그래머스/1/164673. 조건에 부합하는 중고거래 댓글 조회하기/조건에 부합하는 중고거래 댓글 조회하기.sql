
-- 코드를 입력하세요
SELECT a.title, a.board_id, b.reply_id, b.WRITER_ID, b.contents, 
        date_format(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as a
join USED_GOODS_REPLY as b
on a.board_id=b.board_id 
where month(a.CREATED_DATE)="10"
order by CREATED_DATE asc, title asc