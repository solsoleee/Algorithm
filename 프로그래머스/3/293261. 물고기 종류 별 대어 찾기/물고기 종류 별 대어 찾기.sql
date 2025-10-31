-- 코드를 작성해주세요

# select fish_type, max(length) from fish_info
# where fish_type = 1 -- 1일때 2일 때 3일 때
# group by fish_type

select id,fish_name, length from fish_info as a
join fish_name_info as b
on a.fish_type = b.fish_type
where length = (
select max(length) from fish_info
where fish_type = a.fish_type -- 1일때 2일 때 3일 때
group by fish_type
)
order by id 