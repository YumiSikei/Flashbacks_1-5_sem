program quicksort;

const
  max = 100;

var 
  i, n : integer;
  A: array[1..max] of integer;
  
procedure sort(L, R : integer); 
var i, j, x, d : integer;
begin
  i := L; 
  j := R;
  x := a[(L + R) div 2];
  repeat
    while (A[i] < x) do i := i + 1;
    while (A[j] > x) do j := j - 1;
    if i <= j then
    begin
      d := A[i];
      a[i] := a[j]; 
      a[j] := d;
      i := i + 1; 
      j := j - 1;
    end;
  until (i > j);
  if (L < j) then sort(L, j);
  if (i < R) then sort(i, R);
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