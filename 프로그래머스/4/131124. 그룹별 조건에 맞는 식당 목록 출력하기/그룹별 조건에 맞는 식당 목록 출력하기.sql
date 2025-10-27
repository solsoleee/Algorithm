-- 코드를 입력하세요
SELECT a.MEMBER_NAME, b.REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE 
from MEMBER_PROFILE as a
join REST_REVIEW as b
on a.MEMBER_ID=b.MEMBER_ID
where a.member_id = (
    select MEMBER_ID from REST_REVIEW
    group by MEMBER_ID	
    order by count(MEMBER_ID) desc
    limit 1
)
order by REVIEW_DATE  asc, b.REVIEW_TEXT asc
