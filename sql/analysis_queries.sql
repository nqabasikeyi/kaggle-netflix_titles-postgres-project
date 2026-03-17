SELECT type, COUNT(*) AS total
FROM shows
GROUP BY type;

SELECT rating, COUNT(*) AS total
FROM shows
GROUP BY rating
ORDER BY total DESC;

SELECT g.name AS genre, COUNT(*) AS total_titles
FROM genres g
JOIN show_genres sg ON g.genre_id = sg.genre_id
GROUP BY g.name
ORDER BY total_titles DESC
LIMIT 10;