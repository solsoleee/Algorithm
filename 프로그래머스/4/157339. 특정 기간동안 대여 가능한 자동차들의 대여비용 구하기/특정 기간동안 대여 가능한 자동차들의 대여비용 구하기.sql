-- 코드를 입력하세요
SELECT a.CAR_ID,a.CAR_TYPE, round((a.DAILY_FEE *(1-c.DISCOUNT_RATE/100)* 30),0) as Fee
from CAR_RENTAL_COMPANY_CAR as a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
on a.CAR_ID=b.CAR_ID
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as c
on a.CAR_TYPE=c.CAR_TYPE
where b.car_id not in
    ( select car_id
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY
      where end_date > '2022-11-1' and start_date < '2022-12-1')
and (a.CAR_TYPE='세단' or  a.CAR_TYPE='SUV')
and c.DURATION_TYPE='30일 이상'
and ((a.DAILY_FEE *(1-c.DISCOUNT_RATE/100)* 30) >=500000 
and ((a.DAILY_FEE *(1-c.DISCOUNT_RATE/100)* 30) ) <=2000000)
group by a.car_id, a.car_type
order by fee desc, a.car_type, a.car_id desc 
# 


# and (date_format(b.end_date, '%Y-%m-%d') < '2022-11-1') 
# and (date_format(b.start_date, '%Y-%m-%d') >'2022-11-30')



 # a.CAR_ID,a.CAR_TYPE, fee

