-- Displays the max temperature of each state
SELECT state, MAX(temp) AS max_temp
FROM states
GROUP BY state
ORDER BY state;
