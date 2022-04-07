--Домашнее задание «Работа с PostgreSQL. Создание БД»
create table if not exists Исполнители (
	id_artist serial primary key,
	Имя VARCHAR(50) not null unique,
	id_genre INTEGER not null unique
);
create table if not exists Альбомы (
	id_album serial primary key,
	Название_альбома VARCHAR(100) not null,
	Год_выпуска INTEGER not null,
	id_artist INTEGER references Исполнители(id_artist) not null
);
create table if not exists Треки (
	id_track serial primary key,
	Название_трека VARCHAR(100) not null,
	Длительность INTEGER not null,
	id_album INTEGER references Альбомы(id_album) not null
);
create table if not exists Жанры (
	id_genre serial primary key,
	Название_жанра VARCHAR(100) not null unique
);
alter table Исполнители add constraint id_genre foreign key (id_genre) references Жанры(id_genre);


--Домашнее задание «Проектирование БД. Связи. 3НФ»
alter table Исполнители drop column id_genre;
alter table Альбомы drop column id_artist;
create table if not exists Жанры_Исполнители (
	id_genre INTEGER references Жанры(id_genre) not null,
	id_artist INTEGER references Исполнители(id_artist) not null,
	primary key(id_genre, id_artist)
);
create table if not exists Альбомы_Исполнители (
	id_album INTEGER references Альбомы(id_album) not null,
	id_artist INTEGER references Исполнители(id_artist) not null,
	primary key(id_album, id_artist)
);
create table if not exists Сборники (
	id_collection serial primary key,
	Название_сборника VARCHAR(100) not null,
	Год_выпуска INTEGER not null
);
create table if not exists Сборники_Треки (
	id_collection INTEGER references Сборники(id_collection) not null,
	id_track INTEGER references Треки(id_track) not null,
	primary key(id_collection, id_track)
);
