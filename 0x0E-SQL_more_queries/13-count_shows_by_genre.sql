-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.name, COUNT(*) AS number_of_shows
FROM tv_show_genres
RIGHT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows;
