SELECT CATEGORY, SUM(SALES) TOTAL_SALES
FROM BOOK NATURAL JOIN BOOK_SALES
WHERE SALES_DATE LIKE '%2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY