first=2-3*5;
two=4.5/sqrt(2);
three=7^20;
four=cos(pi/3);
five=log(8);
fprintf('2-3*5=%d\n',first);
fprintf('4.5/(2^0.5)=%f\n',two);
fprintf('7^20=%d\n',three);
fprintf('cos(pi/3)=%f\n',four);
fprintf('ln8=%f\n',five);
A=[1 2;-3 -4;5 6;];
B=[1 -2 -3;-4 5 6;];
C=[2 -1;pi log10(2);-2 6;];
I=eye(3,3);
fprintf('A31=%d\n',A(2,1));
fprintf('C21=%f\n',C(2,1));
fprintf('second row of B=%d %d %d\n',B(2,:));
disp('row reduced echelon from A=');
disp(rref(A));
disp('row reduced echelon from B=');
disp(rref(B));
disp('A+2C=');
disp(A+2*C);
disp('A transpose');
disp(A.');
E=A*B;
disp('E=');
disp(E);
F=B*A;
disp('F=');
disp(F);
G=(A.')*(B.');
disp('G=');
disp(G)
H=(A*B).';
disp('H=');
disp(H)