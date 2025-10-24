select count(*) as COUNT from ecoli_Data
where (genotype & 2 = 0) and
((genotype & 4 >=1) or (genotype & 1 >=1));