SELECT
  strftime('%Y-%m', ts) AS month,
  COUNT(DISTINCT user_id) AS users
FROM events
WHERE event='signup'
GROUP BY month
ORDER BY month;
