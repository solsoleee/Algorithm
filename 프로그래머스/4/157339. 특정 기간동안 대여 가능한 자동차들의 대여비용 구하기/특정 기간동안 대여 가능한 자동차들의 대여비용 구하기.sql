SELECT t.car_id, t.car_type, t.fee
FROM (
  SELECT
    c.car_id,
    c.car_type,
    ROUND(c.daily_fee * 30 * (1 - dp.discount_rate / 100.0), 0) AS fee
  FROM CAR_RENTAL_COMPANY_CAR AS c
  JOIN CAR_Rental_Company_Discount_Plan AS dp
    ON dp.car_type = c.car_type
   AND dp.duration_type = '30일 이상'
  WHERE c.car_type IN ('세단', 'SUV')
    AND NOT EXISTS (
      SELECT 1
      FROM CAR_Rental_Company_Rental_History AS rh
      WHERE rh.car_id = c.car_id
        -- 11월과 "겹치는" 이력이 있으면 제외
        AND rh.start_date <= '2022-11-30'
        AND rh.end_date   >= '2022-11-01'
    )
) AS t
-- 50만 이상, 200만 미만
WHERE t.fee >= 500000 AND t.fee < 2000000
ORDER BY t.fee DESC, t.car_type ASC, t.car_id DESC;
