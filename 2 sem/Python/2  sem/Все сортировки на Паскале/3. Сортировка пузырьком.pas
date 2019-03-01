program obmen;

const
  max = 100;

var 
  i, n : integer;
  A: array[1..max] of integer;
  
procedure sort(L, R : integer); 
var i, j, x, d : integer;
begin
  for i:=1 to n-1 do 
  for j:=i+1 to n do 
    if a[i] > a[j] then 
      begin
        x:= a[i]; 
        a[i]:= a[j]; 
        a[j]:= x;
      end;
end; 
  
begin
  write('¬ведиет размер массива (< 100): ');
  readln(n);
  write('¬ведите массив из ', n, ' чисел: ');
  for i:= 1 to N do read(A[i]);
  sort(1, n);
  write('ќтсортированный массив: ');
  for i:= 1 to N do write(A[i], ' ');
end.