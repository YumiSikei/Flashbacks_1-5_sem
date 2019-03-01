program binvstavka;

const
  max = 100;

var 
  i, n : integer;
  A: array[1..max] of integer;
  
procedure sort(n: integer); 
  var i, j, x, L, R, m: integer;
  begin
    for i:=2 to n do 
    begin 
      x:= A[i]; 
      L:= 1; 
      R:= i-1; 
      While L <= R do 
      begin 
        m:= (L + R) div 2; 
        if x < A[m] then 
          R:= m - 1
        else
          L:= m + 1
      end; 
      for j:=i-1 downto L do A[j+1]:= A[j];
      A[L]:=x 
    end;
  end;
  
begin
  write('¬ведиет размер массива (< 100): ');
  readln(n);
  write('¬ведите массив из ', n, ' чисел: ');
  for i:= 1 to N do read(A[i]);
  sort(n);
  write('ќтсортированный массив: ');
  for i:= 1 to N do write(A[i], ' ');
end.