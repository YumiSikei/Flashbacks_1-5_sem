program prostvstavka;

const
  max = 100;

var 
  i, n : integer;
  A: array[1..max] of integer;
  
procedure sort(n: integer); 
  var i, j, x: integer;
  begin
  for i:= 2 to n do
    begin
      x:= a[i];
      j:= i-1;
      while (j > 0) and (x < a[j]) do
        begin
        a[j+1]:= a[j];
        j:= j-1;
        end;
      a[j+1]:= x;
    end;
  end;
  
begin
  write('Ââåäèåò ğàçìåğ ìàññèâà (< 100): ');
  readln(n);
  write('Ââåäèòå ìàññèâ èç ', n, ' ÷èñåë: ');
  for i:= 1 to N do read(A[i]);
  sort(n);
  write('Îòñîğòèğîâàííûé ìàññèâ: ');
  for i:= 1 to N do write(A[i], ' ');
end.