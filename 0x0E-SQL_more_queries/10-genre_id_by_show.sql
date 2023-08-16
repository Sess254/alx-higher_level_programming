-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_shows_genres.genre.id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv.shows.id = tv_show_genres.shows.id
ORDER BY tv_shows.title, tv_shows_genre_id
