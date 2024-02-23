-- 코드를 작성해주세요
select b.item_id, b.item_name
from ITEM_TREE as a
join item_info as b
on a.item_id=b.item_id
where parent_item_id is null