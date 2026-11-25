-- Write your query below
SELECT
    c.customer_id,
    c.name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN product p
ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING SUM(CASE WHEN TO_CHAR(o.order_date, 'YYYY-MM') = '2020-06' THEN p.price*o.quantity ELSE 0 END) >= 100 AND SUM(CASE WHEN TO_CHAR(o.order_date, 'YYYY-MM') = '2020-07' THEN p.price*o.quantity ELSE 0 END) >= 100;