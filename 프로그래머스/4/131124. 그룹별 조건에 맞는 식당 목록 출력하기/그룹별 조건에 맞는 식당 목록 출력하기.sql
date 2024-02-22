-- 코드를 입력하세요
SELECT a.MEMBER_NAME, b.REVIEW_TEXT, date_format(b.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE as a
join REST_REVIEW as b
on a.MEMBER_ID=b.MEMBER_ID
where a.member_id=(
select member_id
from rest_review
group by member_id
order by count(*) desc
limit 1
)
order by review_date, review_text


