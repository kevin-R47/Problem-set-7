SELECT title
FROM movies JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE (name = 'Johnny Depp' and movie_id IN (
    SELECT movie_id 
    FROM stars JOIN people ON people.id = stars.person_id
    where name = 'Helena Bonham Carter'))