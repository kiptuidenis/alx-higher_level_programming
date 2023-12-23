-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- lists all rows of a database meeting a condition
SELECT tv_genres.name, count(*) AS number_of_shows
FROM tv_show_genres 
RIGHT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
