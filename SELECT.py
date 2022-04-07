from pprint import pprint

import sqlalchemy

db = 'postgresql://test_user:password@localhost:5432/test_db'
engine = sqlalchemy.create_engine(db)

connection = engine.connect()

pprint(connection.execute('''SELECT Название_альбома, Год_выпуска FROM Альбомы
WHERE Год_выпуска = 2018;
''').fetchall())

pprint(connection.execute('''SELECT Название_трека, Длительность FROM Треки
ORDER BY Длительность DESC;
''').fetchone())

pprint(connection.execute('''SELECT Название_трека FROM Треки
WHERE Длительность >= 3.5;
''').fetchall())

pprint(connection.execute('''SELECT Название_сборника FROM Сборники
WHERE Год_выпуска BETWEEN 2018 AND 2020;
''').fetchall())

pprint(connection.execute('''SELECT Имя FROM Исполнители
WHERE Имя NOT LIKE '%% %%';
''').fetchall())

pprint(connection.execute('''SELECT Название_трека FROM Треки
WHERE Название_трека LIKE '%%My%%';
''').fetchall())
