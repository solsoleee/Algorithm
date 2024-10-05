select count(b.FISH_NAME) as FISH_COUNT
from fish_info as a
join fish_name_info as b
on a.fish_type = b.fish_type
where b.FISH_NAME in ('BASS', 'SNAPPER');