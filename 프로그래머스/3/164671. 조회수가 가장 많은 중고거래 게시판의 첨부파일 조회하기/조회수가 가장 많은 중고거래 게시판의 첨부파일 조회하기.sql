-- 코드를 입력하세요
SELECT concat('/home/grep/src/', a.BOARD_ID,'/', FILE_ID, FILE_NAME,FILE_EXT )
as FILE_PATH
from USED_GOODS_FILE as a
join USED_GOODS_BOARD as b
on a.BOARD_ID=b.BOARD_ID
where b.views=(select max(views) from USED_GOODS_BOARD limit 1)
order by a.FILE_ID desc



# /home/grep/src/B0001/IMG_000001photo1.jpg
# FILE_PATH