USE master
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'RK2')
  DROP DATABASE RK2
GO
CREATE DATABASE RK2
GO

USE RK2
GO

CREATE TABLE dbo.Employee
(
    EmployeeID INT NOT NULL,
    Department NVARCHAR(85) NOT NULL,
    Status NVARCHAR(50) NOT NULL,
    FullName NVARCHAR(85) NOT NULL,
    Salary INT NOT NULL
);
GO

CREATE TABLE dbo.Medicine
(
    MedicineID INT NOT NULL,
    Name NVARCHAR(50) NOT NULL,
    Instruction NVARCHAR(85),
    Price INT NOT NULL
);
GO

CREATE TABLE dbo.Department
(
    DepartmentID INT NOT NULL,
    DepartmentName NVARCHAR(50) NOT NULL,
    DepartmentPhone INT,
    Chief NVARCHAR(85)
);
GO

ALTER TABLE dbo.Employee
ADD CONSTRAINT PK_Employees PRIMARY KEY (EmployeeID);
GO

ALTER TABLE dbo.Medicine
ADD CONSTRAINT PK_Medicine PRIMARY KEY (MedicineID);
GO

ALTER TABLE dbo.Department
ADD CONSTRAINT PK_Departments PRIMARY KEY (DepartmentID);
GO

ALTER TABLE dbo.Employee
ADD CONSTRAINT PK_ED FOREIGN KEY Department REFERENCES dbo.Department(DepartmentID);
GO

ALTER TABLE dbo.Employee
ADD CONSTRAINT PK_EC FOREIGN KEY EmployeeID REFERENCES dbo.Department(Chief);
GO


--Employees--
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (1, 'Support', 'Senior Financial Analyst', 'Rey Schimon', 389);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (2, 'Training', 'Software Consultant', 'Amargo Karle', 950);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (3, 'Engineering', 'Community Outreach Specialist', 'Benedetta Reinbach', 203);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (4, 'Legal', 'Community Outreach Specialist', 'Carlos Gheorghie', 929);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (5, 'Business Development', 'Analog Circuit Design manager', 'Jo Reah', 487);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (6, 'Support', 'Developer II', 'Leelah Werendell', 657);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (7, 'Business Development', 'Technical Writer', 'Borg Neasham', 158);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (8, 'Training', 'Senior Quality Engineer', 'Stephi Domenc', 473);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (9, 'Product Management', 'Administrative Officer', 'Cody Allso', 315);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (10, 'Training', 'General Manager', 'Tomasine Goddman', 733);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (11, 'Product Management', 'Nurse Practicioner', 'Vasili Morratt', 623);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (12, 'Research and Development', 'Programmer Analyst IV', 'Sonya Curryer', 273);
insert dbo.Employees (EmployeeID, Department, Status, FullName, Salary) values (13, 'Marketing', 'Database Administrator IV', 'Silvio Jedrasik', 398);

--Medicine--
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (1, 'Para Grass Pollen', 'Bzkpzvpdyjmzrnfndfju', 338);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (2, 'Candesartan cilexetil', 'Vcbixoyrjkfvmttiskgg', 634);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (3, 'suboxone', 'Lwbukyenvghnykcsjatk', 139);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (4, 'GRAPHITES', 'Ovycvickjfluhqvwwotb', 215);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (5, 'KINERASE', 'Ufzyreayqllluxhsyelb', 432);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (6, 'Kaletra', 'Jiwpgoyoxetjqtzdhumh', 725);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (7, 'SUMATRIPTAN', 'Oxrcwbsqonenmfonwkoe', 323);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (8, 'Cefprozil', 'Tvgmnegdsuvmmsytttab', 687);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (9, 'Lobelia Quercus', 'Dppxfvhkecaqkavfkgpk', 292);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (10, 'Bisoprolol Fumarate', 'Puijrfycenjoajxoqsic', 131);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (11, 'Carbinoxamine Maleate', 'Hwxksodcphloupdrmlgm', 545);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (12, 'CAFFEINE CITRATE', 'Uumqvwpalwqwwdhmptdi', 554);
insert dbo.Medicine (MedicineID, Name, Instruction, Price) values (13, 'Suave', 'Etzalbknhpyjbsbgkpnb', 745);

--Department--
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (1, 'Product Management', '255-192-3041', 'Christoph Carleton');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (2, 'Research and Development', '884-784-8612', 'Eydie Olyff');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (3, 'Marketing', '456-883-8742', 'Emmerich Dives');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (4, 'Human Resources', '151-163-1433', 'Ailbert McDermDepartmentID');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (5, 'Business Development', '284-368-9914', 'Jacquie Petric');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (6, 'Human Resources', '626-869-4425', 'Robby Gemson');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (7, 'Legal', '221-942-4557', 'Courtney Patkin');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (8, 'Training', '414-460-9507', 'Valma Dowty');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (9, 'Training', '591-380-7127', 'Jephthah Pepall');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (10, 'Engineering', '698-219-5022', 'Benedetto Geeves');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (11, 'Accounting', '718-685-5736', 'Flossie Meneer');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (12, 'Sales', '872-569-9756', 'Lynde Winterbourne');
insert dbo.Department (DepartmentID, DepartmentName, DepartmentPhone, Chief) values (13, 'Product Management', '361-183-7292', 'Jarrad Ramsbottom');