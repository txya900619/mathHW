A = [1 4 0 2 -1;3 12 1 5 5;2 8 1 3 2;5 20 2 8 8];
c = [-2 ;-1; 0; -1];
x = A\c;
disp('x:');
disp(x);
B = [-2 1 3 1;-5 3 11 7;8 -5 -19 -13;0 1 7 5;-17 5 1 -3];
d = [1;2;3;4;5];
y = B\d;
disp('y');
disp(y);
fprintf('rank of A : %d\n', rank(A));
fprintf('rank of A transpose : %d\n', rank(A.'));
fprintf('rank of A*A transpose : %d\n', rank(A.'*A));
fprintf('rank of B : %d\n', rank(B));
fprintf('rank of B transpose : %d\n', rank(B.'));
fprintf('rank of B*B transpose : %d\n', rank(B.'*B));
fprintf('nullity of A : %d\n', 5-rank(A));
fprintf('nullity of A transpose : %d\n', 4-rank(A.'));
fprintf('nullity of A*A transpose : %d\n', 5-rank(A.'*A));
fprintf('nullity of B : %d\n', 4-rank(B));
fprintf('nullity of B transpose : %d\n', 5-rank(B.'));
fprintf('nullity of B*B transpose : %d\n', 4-rank(B.'*B));
disp('rank 都一樣');
disp('nullity t*原本跟原本一樣');