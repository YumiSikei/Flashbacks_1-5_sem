//Янова Даниэлла ИУ7-13
//Сформировать квадратную матрицу с нулевой главной диагональю и единицами
//под ней. Найти средние арифметические в каждой строке матрицы и наибольшее
//из них

program matrix;
{$APPTYPE CONSOLE}

const
  M=5;

var
  A: array [1..M,1..M] of integer;  //Матрица А
  X: array [1..M] of real;  //Массив для средних арифметических чисел
  size: integer;  //Реальное число строк и столбцов
  i, j: integer;  //Параметры для циклов
  maxsr: real;  //Максимальное среднее арифметическое
  k: integer;  //Переменная для формирования матрицы

begin
  repeat
    begin         // Ввод размера матрицы
      write('Введите количество строк(столбцов) матрицы X: ');
      read(size);
      readln;
    end;
  until (size > 0) and (size < M+1);

  k:=2;
  for i:=1 to size do //Формирование матрицы
    begin
      for j:=1 to size do
        if i=j then
          A[i,j]:=0
        else
          if i>j then
            A[i,j]:=1
        else
          A[i,j]:=k;
          k:=k+1
        
    end;

  writeln;
  writeln('Матрица X: '); // Вывод исходных данных
  for i:=1 to size do
    begin
      for j:=1 to size do
        write(A[i,j],'  ');
      writeln;
    end;

  for i:=1 to size do  //Вычисление средних арифметических в строках матрицы А
    begin
      X[i]:=0;
      for j:=1 to size do
        X[i]:=X[i]+A[i,j];
      X[i]:=X[i]/size;   //Сохраняем значения в массиве X
    end;

  maxsr:=X[0];
  for i:=2 to M do  //Вычисление наибольшего среднего арифметического
    if X[i]>maxsr then
      maxsr:=X[i];

  writeln; 
  for i:=1 to size do  //Вывод средних арифметических чисел в строках матрицы А
    begin
      write('Среднее арифметическое элементов в ',i,' строке: ',X[i,j]);
      writeln;
    end;
  
  writeln;  //Вывод максимального среднего арифметического числа
  writeln('Максимальное среднее арифметическое: ',maxsr,'  ');

end.
