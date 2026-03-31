-- Top 5 most expensive products
SELECT title, price
FROM products
ORDER BY price DESC
LIMIT 5;

-- Average price by category
SELECT category, ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- Best rated products
SELECT title, rate, cnt
FROM products
WHERE rate >= 4.5
ORDER BY cnt DESC;

-- Total products per category
SELECT category,
COUNT(*) AS total
FROM products
GROUP BY category;
