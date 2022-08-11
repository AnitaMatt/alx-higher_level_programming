-- list all genres and display number of shows link
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY COUNT(tv_genres.id) DESC
