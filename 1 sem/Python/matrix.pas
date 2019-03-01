//����� �������� ��7-13
//������������ ���������� ������� � ������� ������� ���������� � ���������
//��� ���. ����� ������� �������������� � ������ ������ ������� � ����������
//�� ���

program matrix;
{$APPTYPE CONSOLE}

const
  M=5;

var
  A: array [1..M,1..M] of integer;  //������� �
  X: array [1..M] of real;  //������ ��� ������� �������������� �����
  size: integer;  //�������� ����� ����� � ��������
  i, j: integer;  //��������� ��� ������
  maxsr: real;  //������������ ������� ��������������
  k: integer;  //���������� ��� ������������ �������

begin
  repeat
    begin         // ���� ������� �������
      write('������� ���������� �����(��������) ������� X: ');
      read(size);
      readln;
    end;
  until (size > 0) and (size < M+1);

  k:=2;
  for i:=1 to size do //������������ �������
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
  writeln('������� X: '); // ����� �������� ������
  for i:=1 to size do
    begin
      for j:=1 to size do
        write(A[i,j],'  ');
      writeln;
    end;

  for i:=1 to size do  //���������� ������� �������������� � ������� ������� �
    begin
      X[i]:=0;
      for j:=1 to size do
        X[i]:=X[i]+A[i,j];
      X[i]:=X[i]/size;   //��������� �������� � ������� X
    end;

  maxsr:=X[0];
  for i:=2 to M do  //���������� ����������� �������� ���������������
    if X[i]>maxsr then
      maxsr:=X[i];

  writeln; 
  for i:=1 to size do  //����� ������� �������������� ����� � ������� ������� �
    begin
      write('������� �������������� ��������� � ',i,' ������: ',X[i,j]);
      writeln;
    end;
  
  writeln;  //����� ������������� �������� ��������������� �����
  writeln('������������ ������� ��������������: ',maxsr,'  ');

end.
