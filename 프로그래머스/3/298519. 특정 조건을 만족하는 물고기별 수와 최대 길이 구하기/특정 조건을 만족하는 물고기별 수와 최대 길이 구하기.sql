-- 코드를 작성해주세요
select count(*) as FISH_COUNT, max(length) as MAX_LENGTH , fish_type from fish_info
where fish_type in
(select fish_type  from FISH_INFO
group by fish_type
having avg(ifnull(length, 10))>=33)
group by fish_type
order by fish_type
