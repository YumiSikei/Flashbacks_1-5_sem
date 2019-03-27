USE master
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'RK2')
  DROP DATABASE RK2
GO
CREATE DATABASE RK2
GO

SET DATEFORMAT dmy;
GO

USE RK2
GO

CREATE TABLE dbo.Florist
(
    FloristID INT NOT NULL,
    FullName NVARCHAR(85) NOT NULL,
    PassportNumber INT NOT NULL,
    PhoneNumber INT
);
GO

CREATE TABLE dbo.Customer
(
    CustomerID INT NOT NULL,
    FullName NVARCHAR(85) NOT NULL,
    BirthDate DATE,
    City NVARCHAR(50),
    PhoneNumber INT
);
GO

CREATE TABLE dbo.Bouquet
(
    BouquetID INT NOT NULL,
    Author NVARCHAR(85),
    Name NVARCHAR(85)
);
GO

--Florists--
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (1, 'Rana Bendik', 437821, '3653655226');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (2, 'Shalne Swett', 922721, '3106470325');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (3, 'Redd Tague', 856891, '2413566086');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (4, 'Latrina Duffitt', 137328, '5673254696');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (5, 'Stesha Olsen', 904152, '8127438123');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (6, 'Dyann Synder', 876372, '2267328660');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (7, 'Aldon Kelleway', 465075, '4024015305');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (8, 'Ortensia Smieton', 863736, '4899627245');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (9, 'Rhonda Teaz', 543152, '7438099737');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (10, 'Alejandrina Luttger', 125154, '8161361369');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (11, 'Nadiya Grube', 797475, '3736761262');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (12, 'Evangeline Spelling', 368760, '3821616275');
INSERT dbo.Florist (FloristID, FullName, PassportNumber, PhoneNumber) values (13, 'Catlaina Dowles', 410577, '6109966840');
--Customers--
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (1, 'Guillermo Nance', '29/10/1989', 'Batugede Kulon', '518-404-9044');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (2, 'Barty Pawle', '01/08/1990', 'Kuala Belait', '541-276-1278');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (3, 'Elfie Parrot', '13/05/1990', 'Wuhu', '226-291-3994');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (4, 'Ralina Brian', '08/10/1990', 'Falköping', '773-501-7625');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (5, 'Ulla Dulling', '29/09/1990', 'As Sulayyil', '146-429-9989');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (6, 'Ives Etuck', '11/10/1987', 'Oakland', '510-283-8208');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (7, 'Hy Lingfoot', '21/09/1988', 'N’dalatando', '199-758-5963');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (8, 'Helene Oneile', '13/11/1987', 'Vällingby', '795-449-7755');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (9, 'Richmond Planke', '18/03/1986', 'Wieczfnia Kościelna', '631-127-2848');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (10, 'Jaime Ashlee', '13/10/1989', 'Surgut', '882-953-5676');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (11, 'Lorianna Paterno', '23/09/1988', 'Vinica', '282-511-1065');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (12, 'Leodora Ansell', '05/01/1990', 'Sukatani', '399-345-0540');
INSERT dbo.Customer (CustomerID, FullName, BirthDate, City, PhoneNumber) values (13, 'Randi Blackall', '17/03/1988', 'Älvängen', '178-375-5591');
--Bouquets--
INSERT dbo.Bouquet (BouquetID, Author, Name) values (1, 'Edgardo Mulroy', 'Joséphine');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (2, 'Jedediah Veness', 'Garçon');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (3, 'Candace Addekin', 'Andréanne');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (4, 'Junette Haskett', 'Réservés');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (5, 'Jillian Thurlow', 'Léone');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (6, 'Elinore Lashmore', 'Maëlla');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (7, 'Clevey Sandall', 'Mélys');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (8, 'Munroe Sellen', 'Hélène');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (9, 'Brice Farquharson', 'Géraldine');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (10, 'Lezley Rubinivitz', 'Daphnée');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (11, 'Juieta Turfrey', 'André');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (12, 'Elene Blazy', 'Laïla');
INSERT dbo.Bouquet (BouquetID, Author, Name) values (13, 'Paxon Bricham', 'Dà');