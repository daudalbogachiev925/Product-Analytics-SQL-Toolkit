WITH first_seen AS (
  SELECT user_id, MIN(date(ts)) AS first_day
  FROM events GROUP BY user_id
),
activity AS (
  SELECT DISTINCT user_id, date(ts) AS day FROM events
)
SELECT
  f.first_day,
  CAST(julianday(a.day) - julianday(f.first_day) AS INT) AS day_n,
  COUNT(DISTINCT a.user_id) AS users
FROM first_seen f
JOIN activity a ON a.user_id = f.user_id
GROUP BY f.first_day, day_n
ORDER BY f.first_day, day_n;
