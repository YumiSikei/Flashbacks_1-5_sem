USE master
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'RK2')
  DROP DATABASE RK2
GO
CREATE DATABASE RK2
GO

USE RK2
GO

CREATE TABLE dbo.Driver
(
    DriverID INT NOT NULL,
    LicenseNumber INT NOT NULL,
    FullName NVARCHAR(85) NOT NULL,
    Car NVARCHAR(85) NOT NULL
);
GO

CREATE TABLE dbo.Car
(
    CarID INT NOT NULL,
    Brand NVARCHAR(50) NOT NULL,
    Model NVARCHAR(50),
    ReleaseDate DATE,
    RegistrationDate DATE
);
GO

CREATE TABLE dbo.Fee
(
    FeeID INT NOT NULL,
    FeeType NVARCHAR(85) NOT NULL
    FeeAmount INT,
    Warning INT
);
GO

--Drivers, add car info--
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (1, 94987429, 'Claire Cornillot');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (2, 73860953, 'Bride Hiscoe');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (3, 22591738, 'Josefa Hartness');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (4, 59135425, 'Emelina Rosenstein');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (5, 57798630, 'Gordie Shambrook');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (6, 21257052, 'Marcelle McLucky');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (7, 42147004, 'Byron Blundon');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (8, 15219326, 'Saleem Skyme');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (9, 38325932, 'Allene Fromont');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (10, 80109420, 'Cosimo Szepe');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (11, 45557629, 'Flemming Skill');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (12, 12182331, 'Falito Ambrus');
INSERT dbo.Driver (id, LicenseNumber, FullName) VALUES (13, 90081873, 'Witty Fulton');

--Cars--
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (1, 'Chevrolet', 'Corvette', '23/07/1973', '09/12/1999');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (2, 'Chevrolet', 'Sportvan G20', '07/12/1977', '22/03/1980');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (3, 'Chevrolet', 'Corsica', '14/06/1967', '16/02/1971');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (4, 'Mercury', 'Capri', '21/08/1997', '08/09/2009');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (5, 'Ford', 'E250', '13/09/2003', '29/05/1981');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (6, 'Kia', 'Optima', '07/08/1967', '21/06/1978');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (7, 'Chevrolet', 'Caprice', '03/09/1978', '25/07/1968');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (8, 'Buick', 'LaCrosse', '01/10/1991', '15/10/2004');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (9, 'Dodge', 'Ram Van 3500', '07/01/1989', '15/12/1999');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (10, 'Daewoo', 'Lanos', '14/02/1970', '22/05/2017');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (11, 'Audi', 'riolet', '08/04/1986', '07/06/1993');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (12, 'BMW', '7 Series', '27/07/1984', '20/07/1967');
INSERT dbo.Car (id, Brand, Model, ReleaseDate, RegistrationDate) VALUES (13, 'Buick', 'Lucerne', '27/01/1990', '21/01/2006');

--Fee--
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (1, 'j1LpEkCW3', 843, 1);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (2, 'pNLbdCLAjMF', 359, 1);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (3, 'gPg88JqZB1', 258, 2);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (4, '6QfLe6HWTc', 101, 1);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (5, 'hwMnjwlBx1C', 120, 3);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (6, '7mRriIsWBLrP', 595, 3);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (7, 'Z7vCqo1T7n', 650, 3);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (8, 'NA3JFe0umknL', 198, 1);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (9, 'hEkFex', 249, 2);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (10, 'KvZHia', 151, 2);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (11, 'A0eViTIIO7v', 244, 1);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (12, '9bF2vCjP2y3g', 364, 2);
INSERT dbo.Fee (id, FeeType, FeeAmount, Warning) VALUES (13, 'zHbYNwfqTFZ', 364, 3);

--Primary Keys(?????)--
ALTER TABLE dbo.Driver
ADD CONSTRAINT PK_Driver PRIMARY KEY (DriverID)
GO

ALTER TABLE dbo.Car
ADD CONSTRAINT PK_Car PRIMARY KEY (CarID)
GO

ALTER TABLE dbo.Fee
ADD CONSTRAINT PK_Fee PRIMARY KEY (FeeID)