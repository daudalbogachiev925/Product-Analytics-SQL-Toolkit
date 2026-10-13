SELECT
  'signup' AS step, COUNT(DISTINCT user_id) AS users FROM events WHERE event='signup'
UNION ALL
SELECT 'activate', COUNT(DISTINCT user_id) FROM events WHERE event='activate'
UNION ALL
SELECT 'purchase', COUNT(DISTINCT user_id) FROM events WHERE event='purchase';
