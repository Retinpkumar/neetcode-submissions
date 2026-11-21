-- Write your query below
-- SELECT
--     s.name
-- FROM sales_person s
-- LEFT JOIN 
--     (SELECT *
--     FROM company c
--     JOIN orders o
--     ON c.com_id = o.com_id AND c.name = 'CRIMSON') d
-- ON s.sales_id = d.sales_id
-- WHERE d.order_id IS NULL;
SELECT sp.name
FROM sales_person sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
);