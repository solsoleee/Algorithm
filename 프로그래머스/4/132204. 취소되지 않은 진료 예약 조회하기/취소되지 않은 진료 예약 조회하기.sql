-- 코드를 입력하세요
SELECT a.APNT_NO, b.PT_NAME, b.PT_NO, a.MCDP_CD, c.DR_NAME, 
a.APNT_YMD
from APPOINTMENT as a
join PATIENT as b
on a.PT_NO = b.PT_NO
join DOCTOR as c
on a.MDDR_ID = c.DR_ID
where date_format(a.APNT_YMD, '%Y-%m-%d')='2022-04-13' 
and a.MCDP_CD='CS'
and a.APNT_CNCL_YN='N'
and a.APNT_CNCL_YMD is null
order by APNT_YMD