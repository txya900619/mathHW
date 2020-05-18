first=2-3*5;
two=4.5/sqrt(2);
three=7^20;
four=cos(pi/3);
five=log(8);
fprintf('2-3*5=%d\n\n',first);
fprintf('4.5/(2^0.5)=%f\n\n',two);
fprintf('7^20=%d\n\n',three);
fprintf('cos(pi/3)=%f\n\n',four);
fprintf('ln8=%f\n\n',five);
A=[1 2;-3 -4;5 6;];
B=[1 -2 -3;-4 5 6;];
C=[2 -1;pi log10(2);-2 6;];
I=eye(3,3);
fprintf('A31=%d\n\n',A(2,1));
fprintf('C21=%f\n\n',C(2,1));
fprintf('second row of B=%d %d %d\n\n',B(2,:));
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
G=(B.')*(A.');
disp('G=');
disp(G)
H=(A*B).';
disp('H=');
disp(H);
fprintf('Is E equal to  F:');
if isequal(E,F)
    fprintf('true\n\n');
else
    fprintf('false\n\n');
end
fprintf('Is G equal to  H:');
if isequal(G,H)
    fprintf('true\n\n');
else
    fprintf('false\n\n');
end
res=E(1,1)*E(2,2)*E(3,3)+E(1,2)*E(2,3)*E(3,1)+E(1,3)*E(2,1)*E(3,2)-E(1,3)*E(2,2)*E(3,1)-E(1,2)*E(2,1)*E(3,3)-E(1,1)*E(2,3)*E(3,2);
if res==0
    fprintf('E is not invertible\n\n');
else
    disp('inverse of E=');
    disp(inv(E));
end
if det(F)==0
    fprintf('E is not invertible\n\n');
else
    disp('inverse of F=');
    disp(inv(F));
end
D=diag([2 1 -1 -2 -5]);
disp('D=');
disp(D);
x=-4:4/10:4;
y=0.6*(x.^2)-1;
plot(x,y);
