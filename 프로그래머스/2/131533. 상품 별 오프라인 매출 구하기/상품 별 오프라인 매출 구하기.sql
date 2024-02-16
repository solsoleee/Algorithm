-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, a.price*sum(b.SALES_AMOUNT) as SALES
from product as a
inner join OFFLINE_SALE as b
on a.product_id = b.product_id
group by a.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC;

