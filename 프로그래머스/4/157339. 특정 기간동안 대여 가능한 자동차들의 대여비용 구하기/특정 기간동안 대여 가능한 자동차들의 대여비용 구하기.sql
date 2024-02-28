-- 코드를 입력하세요 FEE  
SELECT distinct a.CAR_ID, a.CAR_TYPE, round(a.DAILY_FEE*30*(1-c.DISCOUNT_RATE/100)) as Fee
from CAR_RENTAL_COMPANY_CAR as a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
on a.car_id = b.car_id
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as c
on a.car_type = c.car_type
where (a.CAR_TYPE='세단' or a.CAR_TYPE ='SUV')
and a.car_id not in
( select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE < '2022-12-01' and END_DATE > '2022-11-01')                       
and c.DURATION_TYPE='30일 이상'
and round(a.DAILY_FEE*30*(1-c.DISCOUNT_RATE/100)) >= 500000 and round(a.DAILY_FEE*30*(1-c.DISCOUNT_RATE/100))<=2000000
order by fee desc, a.car_type, a.car_id desc