with appointment as (
    select a.APNT_NO, c.MCDP_CD, c.DR_NAME, a.APNT_YMD, a.PT_NO
    from APPOINTMENT as a
    inner join DOCTOR as c on a.MDDR_ID=c.DR_ID
    where c.mcdp_cd='CS' and a.APNT_CNCL_YN='N' and APNT_CNCL_YMD is null
    and a.APNT_YMD like '2022-04-13%'
)

select a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, a.DR_NAME, a.APNT_YMD
from appointment as a
inner join PATIENT as p on a.PT_NO=p.PT_NO
order by APNT_YMD
