SELECT COUNT(*) FISH_COUNT, FISH_NAME
FROM FISH_INFO F NATURAL JOIN FISH_NAME_INFO N
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC