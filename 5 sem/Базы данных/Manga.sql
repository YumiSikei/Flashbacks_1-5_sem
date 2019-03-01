-- phpMyAdmin SQL Dump
-- version 4.0.10
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 17 2014 г., 13:12
-- Версия сервера: 5.5.38-log
-- Версия PHP: 5.3.28

--SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
--SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: "Манга"
--

-- --------------------------------------------------------

--
-- Структура таблицы "Выпуск манги"
--

CREATE TABLE "Выпуск манги" (
  "Id" int(11) NOT NULL AUTO_INCREMENT,
  "Id манги" int(11) NOT NULL,
  "id мангаки" int(11) NOT NULL,
  "id издательства" int(11) NOT NULL,
  "Статус" text CHARACTER SET utf8 NOT NULL,
  "Начало выпуска" date NOT NULL,
  "Конец выпуска" date NOT NULL,
  "Рейтинг" int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY ("Id")
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы "Манга"
--

CREATE TABLE "Манга" (
  "Id" int(100) NOT NULL AUTO_INCREMENT,
  "Название" text CHARACTER SET utf8 NOT NULL,
  "Описание" text CHARACTER SET utf8 NOT NULL,
  "Кол-во глав" int(100) NOT NULL,
  "Кол-во продаж" int(100) NOT NULL,
  "Формат выпуска глав" text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY ("Id")
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Структура таблицы "Мангака"
--

CREATE TABLE IF NOT EXISTS "Мангака" (
  "Id" int(100) NOT NULL AUTO_INCREMENT,
  "ФИО" text CHARACTER SET utf8 NOT NULL,
  "Псевдоним" text CHARACTER SET utf8 NOT NULL,
  "Дата рождения" date NOT NULL,
  "Кол-во работ" int(255) NOT NULL,
  PRIMARY KEY ("Id")
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы "content"
--

--INSERT INTO "content" ("Id", "content", "title", "category", "Date create", "Date edite", "author") VALUES
--(1, 'delphi', 'Delphi', 1, '2014-12-17', '0000-00-00', 1);

-- --------------------------------------------------------

--
-- Структура таблицы "Издательство"
--

CREATE TABLE IF NOT EXISTS "Издательство" (
  "Id" int(11) NOT NULL AUTO_INCREMENT,
  "Название" text CHARACTER SET utf8 NOT NULL,
  "Год создания" date NOT NULL,
  "Кол-во выпущенных работ" int(255) NOT NULL,
  "Адрес гл. офиса" text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY ("Id")
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
