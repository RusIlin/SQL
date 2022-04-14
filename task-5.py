from pprint import pprint

import sqlalchemy

db = 'postgresql://test_user:password@localhost:5432/test_db'
engine = sqlalchemy.create_engine(db)

connection = engine.connect()

# количество исполнителей в каждом жанре
pprint(connection.execute('''SELECT Название_жанра, COUNT(id_artist) from Жанры_Исполнители ag
LEFT JOIN Жанры g ON ag.id_genre = g.id_genre
GROUP BY Название_жанра;
''').fetchall())

# количество треков, вошедших в альбомы 2019-2020 годов
pprint(connection.execute('''SELECT Название_альбома, Год_выпуска, COUNT(id_track) from Треки t
LEFT JOIN Альбомы a ON t.id_album = a.id_album
WHERE Год_выпуска = 2019 OR Год_выпуска = 2020
GROUP BY Название_альбома, Год_выпуска;
''').fetchall())

# средняя продолжительность треков по каждому альбому
pprint(connection.execute('''SELECT Название_альбома, AVG(Длительность) from Треки t
LEFT JOIN Альбомы a ON t.id_album = a.id_album
GROUP BY Название_альбома;
''').fetchall())

# все исполнители, которые не выпустили альбомы в 2020 году
pprint(connection.execute('''SELECT Имя from Исполнители ar
JOIN Альбомы_Исполнители aa ON ar.id_artist = aa.id_artist
JOIN Альбомы al ON aa.id_album = al.id_album
WHERE Год_выпуска != 2020
GROUP BY Имя;
''').fetchall())

# названия сборников, в которых присутствует конкретный исполнитель
pprint(connection.execute('''SELECT Имя, Название_сборника from Сборники c
LEFT JOIN Сборники_Треки tc ON c.id_collection = tc.id_collection
LEFT JOIN Треки t ON tc.id_track = t.id_track
JOIN Альбомы al ON al.id_album = t.id_album
LEFT JOIN Альбомы_Исполнители aa ON al.id_album = aa.id_album
LEFT JOIN Исполнители ar ON aa.id_artist = ar.id_artist
WHERE Имя = 'Ozzy Osbourne'
GROUP BY Имя, Название_сборника;
''').fetchall())

# название альбомов, в которых присутствуют исполнители более 1 жанра
pprint(connection.execute('''SELECT Название_альбома, COUNT(id_genre) from Жанры_Исполнители ag
LEFT JOIN Исполнители ar ON ag.id_artist = ar.id_artist
LEFT JOIN Альбомы_Исполнители aa ON ar.id_artist = aa.id_artist
LEFT JOIN Альбомы al ON aa.id_album = al.id_album
GROUP BY Название_альбома
HAVING COUNT(ag.id_genre) > 1;
''').fetchall())

# наименование треков, которые не входят в сборники
pprint(connection.execute('''SELECT Название_трека from Треки t
LEFT JOIN Сборники_Треки tc ON t.id_track = tc.id_track
GROUP BY Название_трека
HAVING COUNT(tc.id_track) < 1;
''').fetchall())

# исполнителя(-ей), написавшего самый короткий по продолжительности трек
pprint(connection.execute('''SELECT ar.Имя, Название_трека, Длительность from Треки t
LEFT JOIN Альбомы al ON t.id_album = al.id_album
LEFT JOIN Альбомы_Исполнители aa ON al.id_album = aa.id_album
LEFT JOIN Исполнители ar ON aa.id_artist = ar.id_artist
WHERE Длительность = (SELECT MIN(Длительность) FROM Треки)
GROUP BY ar.Имя, Название_трека, Длительность;
''').fetchall())

# название альбомов, содержащих наименьшее количество треков
pprint(connection.execute('''SELECT Название_альбома, MIN(COUNT(t.id_album)) OVER() from Треки t
LEFT JOIN Альбомы al ON t.id_album = al.id_album
GROUP BY Название_альбома
''').fetchall())
