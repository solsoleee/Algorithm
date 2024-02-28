set @hour = -1;
select (@hour:=@hour+1) as hour,
( select count(hour(datetime))
    from ANIMAL_OUTS
    where hour(datetime)=@hour
) as count
from ANIMAL_OUTS
where @hour<23
order by hour