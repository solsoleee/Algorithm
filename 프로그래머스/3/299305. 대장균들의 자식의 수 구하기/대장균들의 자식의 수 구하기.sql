select a.id, count(b.parent_id) as CHILD_COUNT from ECOLI_DATA as a
left join ECOLI_DATA as b
on a.id = b.parent_id
group by a.id
order by a.id;