-- 코드를 입력하세요
SELECT a.APNT_NO, c.PT_NAME,	a.PT_NO,	a.MCDP_CD,	b.DR_NAME,	a.APNT_YMD
from APPOINTMENT as a
join DOCTOR as b
on b.DR_ID = a.MDDR_ID
join PATIENT as c
on a.PT_NO=c.PT_NO
where date_format(a.APNT_YMD,'%Y-%m-%d')='2022-04-13' and a.MCDP_CD='CS' and APNT_CNCL_YN='N'
order by a.APNT_YMD 

# 