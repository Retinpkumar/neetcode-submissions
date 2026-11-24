-- Write your query below
SELECT 
    DISTINCT w.name AS warehouse_name,
    SUM(p.width*p.length*p.height*w.units) AS volume
FROM warehouse w
LEFT JOIN products p
ON w.product_id = p.product_id
GROUP BY warehouse_name
ORDER BY warehouse_name;