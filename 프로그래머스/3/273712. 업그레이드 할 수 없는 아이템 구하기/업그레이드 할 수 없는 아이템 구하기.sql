-- 코드를 작성해주세요
select item_id, item_name, rarity from item_info
where item_id not in (
## 이거에 없는거
select distinct a.item_id from item_info as a
join item_tree as b
on a.item_id = b.parent_item_id
)
order by item_id desc

