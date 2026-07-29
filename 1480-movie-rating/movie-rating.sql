# Write your MySQL query statement below
(
SELECT name AS results
FROM (
    SELECT COUNT(*) AS c, name
    FROM Users u
    JOIN MovieRating m
        ON u.user_id = m.user_id
    GROUP BY u.user_id, name
) t
ORDER BY c DESC, name
LIMIT 1
)

UNION all

(
SELECT title AS results
FROM (
    SELECT AVG(rating) AS r, title
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.movie_id, title
) tt
ORDER BY r DESC, title
LIMIT 1
);