-- 코드를 입력하세요
SELECT distinct b.car_id from CAR_RENTAL_COMPANY_CAR as a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
on a.car_id = b.car_id
where a.CAR_TYPE = '세단'
and month(b.start_date) = 10
order by b.car_id desc