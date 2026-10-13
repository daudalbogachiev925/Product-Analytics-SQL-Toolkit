SELECT
  date(ts) AS day,
  COUNT(DISTINCT user_id) AS dau
FROM events
WHERE event != 'churn'
GROUP BY date(ts)
ORDER BY day;
