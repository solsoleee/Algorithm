-- 코드를 입력하세요
SELECT BOARD_ID,	WRITER_ID,	TITLE,	PRICE, 
(CASE WHEN STATUS = 'SALE' THEN '판매중'
    WHEN STATUS = 'RESERVED' THEN '예약중'
    ELSE '거래완료'
    END) AS STATUS
from USED_GOODS_BOARD
where date_format(CREATED_DATE, '%Y-%m-%d') like '%2022-10-05%'
order by board_id desc