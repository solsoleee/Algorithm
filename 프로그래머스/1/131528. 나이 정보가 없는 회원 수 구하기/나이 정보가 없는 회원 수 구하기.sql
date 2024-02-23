-- 코드를 입력하세요
SELECT count(user_id) as users
from user_info
where age is null
# group by user_id
# having age is null