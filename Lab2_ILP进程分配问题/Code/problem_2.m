clear;
clc;
time = load("time.mat").time;

% 创建问题的线性整数规划模型

f = -time'; % 目标函数，最大化时间
f = f(:); % 将f转换为列向量

A = zeros(11, 11 * 18); % 不等式约束矩阵
for i = 1:11
    A(i, (i-1) * 18 + 1 : i * 18) = ones(1, 18);
end
b = 2 * ones(11, 1);

Aeq = repmat(eye(18, 18), 1, 11); % 等式约束矩阵
beq = ones(18, 1);

lb = zeros(11 * 18, 1); % 变量下界，所有元素都为0
ub = ones(11 * 18, 1); % 变量上界，所有元素都为1

% 使用intlinprog函数求解线性整数规划问题
[x, fval] = intlinprog(f, 1:11 * 18, A, b, Aeq, beq, lb, ub);

% 将结果转换为矩阵形式
allocation_matrix = reshape(x, 11, 18);

% 输出最小功耗和分配方案
disp(['最大时间：', num2str(-fval)]);
disp('分配方案：');
disp(allocation_matrix);
save("allocation_1.mat", "allocation_matrix");

