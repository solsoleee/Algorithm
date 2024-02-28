-- 코드를 입력하세요
SELECT DATE_Format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, 
        PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where month(sales_date)=3
union
SELECT DATE_Format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, 
        PRODUCT_ID, 
        null as USER_ID, 
        SALES_AMOUNT
from OFFLINE_SALE
where month(sales_date)=3
order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc;

