# Write your MySQL query statement below
select w2.id
from Weather w1, Weather w2
where date_add(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
and w2.temperature > w1.temperature
