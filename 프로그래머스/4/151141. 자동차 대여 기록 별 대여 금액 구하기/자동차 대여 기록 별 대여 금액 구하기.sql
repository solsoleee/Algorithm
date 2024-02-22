with HISTORY as (
select a.HISTORY_id, b.DAILY_FEE, b.car_type,
    datediff(end_date, start_date)+1 as period,
    case 
    when datediff(end_date, start_date)+1 >=90 then '90일 이상'
    when datediff(end_date, start_date)+1 >=30 then '30일 이상'
    when datediff(end_date, start_date)+1 >=7 then '7일 이상'
    else 'None'
    end as DURATION_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
join cAR_RENTAL_COMPANY_CAR as b
on a.car_id=b.car_id
where b.car_type='트럭'
)

SELECT a.history_id, round(a.DAILY_FEE* a.period * (1-ifnull(b.DISCOUNT_RATE, 0)/100)) as FEE
from HISTORY as a
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as b
on a.DURATION_TYPE=b.DURATION_TYPE and a.CAR_TYPE=b.CAR_TYPE
order by fee desc, a.HISTORY_id desc



