%% Load Data
clear; clc;

% Bag 0
bag0 = rosbag('allan_var_0.bag');
bSel0 = select(bag0,'Topic','/IMU')
msgStructs0 = readMessages(bSel0,'DataFormat','struct');
gyroX0 = cellfun(@(m) double(m.AngularVelocity.X),msgStructs0);
gyroY0 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs0);
gyroZ0 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs0);
accelX0 = cellfun(@(m) double(m.LinearAcceleration.X),msgStructs0);
accelY0 = cellfun(@(m) double(m.LinearAcceleration.Y),msgStructs0);
accelZ0 = cellfun(@(m) double(m.LinearAcceleration.Z),msgStructs0);

% Bag 1
bag1 = rosbag('allan_var_1.bag');
bSel1 = select(bag1,'Topic','/IMU')
msgStructs1 = readMessages(bSel1,'DataFormat','struct');
gyroX1 = cellfun(@(m) double(m.AngularVelocity.X),msgStructs1);
gyroY1 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs1);
gyroZ1 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs1);
accelX1 = cellfun(@(m) double(m.LinearAcceleration.X),msgStructs1);
accelY1 = cellfun(@(m) double(m.LinearAcceleration.Y),msgStructs1);
accelZ1 = cellfun(@(m) double(m.LinearAcceleration.Z),msgStructs1);

% Bag 2
bag2 = rosbag('allan_var_2.bag');
bSel2 = select(bag2,'Topic','/IMU')
msgStructs2 = readMessages(bSel2,'DataFormat','struct');
gyroX2 = cellfun(@(m) double(m.AngularVelocity.X),msgStructs2);
gyroY2 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs2);
gyroZ2 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs2);
accelX2 = cellfun(@(m) double(m.LinearAcceleration.X),msgStructs2);
accelY2 = cellfun(@(m) double(m.LinearAcceleration.Y),msgStructs2);
accelZ2 = cellfun(@(m) double(m.LinearAcceleration.Z),msgStructs2);

% Bag 3
bag3 = rosbag('allan_var_3.bag');
bSel3 = select(bag3,'Topic','/IMU')
msgStructs3 = readMessages(bSel3,'DataFormat','struct');
gyroX3 = cellfun(@(m) double(m.AngularVelocity.X),msgStructs3);
gyroY3 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs3);
gyroZ3 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs3);
accelX3 = cellfun(@(m) double(m.LinearAcceleration.X),msgStructs3);
accelY3 = cellfun(@(m) double(m.LinearAcceleration.Y),msgStructs3);
accelZ3 = cellfun(@(m) double(m.LinearAcceleration.Z),msgStructs3);

% Bag 4
bag4 = rosbag('allan_var_4.bag');
bSel4 = select(bag4,'Topic','/IMU')
msgStructs4 = readMessages(bSel4,'DataFormat','struct');
gyroX4 = cellfun(@(m) double(m.AngularVelocity.X),msgStructs4);
gyroY4 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs4);
gyroZ4 = cellfun(@(m) double(m.AngularVelocity.Y),msgStructs4);
accelX4 = cellfun(@(m) double(m.LinearAcceleration.X),msgStructs4);
accelY4 = cellfun(@(m) double(m.LinearAcceleration.Y),msgStructs4);
accelZ4 = cellfun(@(m) double(m.LinearAcceleration.Z),msgStructs4);

% Bag 5

% Bag 6

% Bag 7

% Bag 8

% Bag 9

omega_ax = cat(1, accelX0, accelX1, accelX2, accelX3, accelX4);
omega_ay = cat(1, accelY0, accelY1, accelY2, accelY3, accelY4);
omega_az = cat(1, accelZ0, accelZ1, accelZ2, accelZ3, accelZ4);

Fs = 40;
t0 = 1/Fs;

%% Obtain Allan Deviation
theta_ax = cumsum(omega_ax, 1)*t0;
theta_ay = cumsum(omega_ay, 1)*t0;
theta_az = cumsum(omega_az, 1)*t0;


maxNumM = 100;
L = size(theta_ax, 1);
maxM = 2.^floor(log2(L/2));
m = logspace(log10(1), log10(maxM), maxNumM).';
m = ceil(m); % m must be an integer.
m = unique(m); % Remove duplicates.

% tau = m*t0;
% 
% avar_ax = zeros(numel(m), 1);
% avar_ay = zeros(numel(m), 1);
% avar_az = zeros(numel(m), 1);
% for i = 1:numel(m)
%     mi = m(i);
%     avar_ax(i,:) = sum( ...
%         (theta_ax(1+2*mi:L) - 2*theta_ax(1+mi:L-mi) + theta_ax(1:L-2*mi)).^2, 1);
%     avar_ay(i,:) = sum( ...
%         (theta_ay(1+2*mi:L) - 2*theta_ay(1+mi:L-mi) + theta_ay(1:L-2*mi)).^2, 1);
%     avar_az(i,:) = sum( ...
%         (theta_az(1+2*mi:L) - 2*theta_az(1+mi:L-mi) + theta_az(1:L-2*mi)).^2, 1);
% end
% avar_ax = avar_ax ./ (2*tau.^2 .* (L - 2*m));
% avar_ay = avar_ay ./ (2*tau.^2 .* (L - 2*m));
% avar_az = avar_az ./ (2*tau.^2 .* (L - 2*m));
% 
% 
% adev_ax = sqrt(avar_ax);
% adev_ay = sqrt(avar_ay);
% adev_az = sqrt(avar_az);


%% Plot Allan Deviation
% figure
% hold on
% loglog(tau, adev_ax)
% loglog(tau, adev_ay)
% loglog(tau, adev_az)
% 
% title('Allan Deviation')
% xlabel('\tau');
% ylabel('\sigma(\tau)')
% grid on
% axis equal

[avarFromFunc_ax, tauFromFunc_ax] = allanvar(omega_ax, m, Fs);
[avarFromFunc_ay, tauFromFunc_ay] = allanvar(omega_ay, m, Fs);
[avarFromFunc_az, tauFromFunc_az] = allanvar(omega_az, m, Fs);

adevFromFunc_ax = sqrt(avarFromFunc_ax);
adevFromFunc_ay = sqrt(avarFromFunc_ay);
adevFromFunc_az = sqrt(avarFromFunc_az);


figure
loglog(tauFromFunc_ax, adevFromFunc_ax, tauFromFunc_ay, adevFromFunc_ay, tauFromFunc_az, adevFromFunc_az);
title('Allan Deviations')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('Accel X', 'Accel Y', 'Accel Z')
grid on
% axis equal

%% Angle Random Walk

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slope = -0.5;
logtau = log10(tauFromFunc_ax);
logadev_ax = log10(adevFromFunc_ax);
logadev_ay = log10(adevFromFunc_ay);
logadev_az = log10(adevFromFunc_az);

dlogadev_ax = diff(logadev_ax) ./ diff(logtau);
dlogadev_ay = diff(logadev_ay) ./ diff(logtau);
dlogadev_az = diff(logadev_az) ./ diff(logtau);

[~, i_ax] = min(abs(dlogadev_ax - slope));
[~, i_ay] = min(abs(dlogadev_ay - slope));
[~, i_az] = min(abs(dlogadev_az - slope));


% Find the y-intercept of the line.
b_ax = logadev_ax(i_ax) - slope*logtau(i_ax);
b_ay = logadev_ay(i_ay) - slope*logtau(i_ay);
b_az = logadev_az(i_az) - slope*logtau(i_az);

% Determine the angle random walk coefficient from the line.
logN_ax = slope*log(1) + b_ax;
N_ax = 10^logN_ax

logN_ay = slope*log(1) + b_ay;
N_ay = 10^logN_ay

logN_az = slope*log(1) + b_az;
N_az = 10^logN_az

% Plot the results.
tauN = 1;
lineN_ax = N_ax ./ sqrt(tauFromFunc_ax);
lineN_ay = N_ay ./ sqrt(tauFromFunc_ax);
lineN_az = N_az ./ sqrt(tauFromFunc_ax);

figure
% loglog(tauFromFunc_ax, adevFromFunc_ax, tauFromFunc_ax, lineN_ax, '--', tauN, N_ax, 'o')
% hold on
% loglog(tauFromFunc_ay, adevFromFunc_ay, tauFromFunc_ay, lineN_ay, '--', tauN, N_ay, 'o')
% loglog(tauFromFunc_az, adevFromFunc_az, tauFromFunc_az, lineN_az, '--', tauN, N_az, 'o')
loglog(tauFromFunc_ax, adevFromFunc_ax, 'r', tauFromFunc_ay, adevFromFunc_ay, 'g', tauFromFunc_az, adevFromFunc_az, 'b')
hold on
loglog(tauFromFunc_ax, lineN_ax, '--r', tauFromFunc_ay, lineN_ay, '--g', tauFromFunc_az, lineN_az, '--b')
loglog(tauN, N_ax, 'or', tauN, N_ay, 'og', tauN, N_az, 'ob')
hold off

title('Allan Deviation with Angle Random Walk')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('\sigma_a_x', '\sigma_a_y', '\sigma_a_z', '\sigma_N_a_x', '\sigma_N_a_y', '\sigma_N_a_z')

text(tauN, N_ax, 'N_a_x')
text(tauN, N_ay, 'N_a_y')
text(tauN, N_az, 'N_a_z')

grid on
% axis equal

%% Rate Random Walk

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slope = 0.5;
logtau = log10(tauFromFunc_ax);
logadev_ax = log10(adevFromFunc_ax);
logadev_ay = log10(adevFromFunc_ay);
logadev_az = log10(adevFromFunc_az);

dlogadev_ax = diff(logadev_ax) ./ diff(logtau);
dlogadev_ay = diff(logadev_ay) ./ diff(logtau);
dlogadev_az = diff(logadev_az) ./ diff(logtau);

[~, i_ax] = min(abs(dlogadev_ax - slope));
[~, i_ay] = min(abs(dlogadev_ay - slope));
[~, i_az] = min(abs(dlogadev_az - slope));

% Find the y-intercept of the line.
b_ax = logadev_ax(i_ax) - slope*logtau(i_ax);
b_ay = logadev_ay(i_ay) - slope*logtau(i_ay);
b_az = logadev_az(i_az) - slope*logtau(i_az);

% Determine the rate random walk coefficient from the line.
logK_ax = slope*log10(3) + b_ax;
K_ax = 10^logK_ax
logK_ay = slope*log10(3) + b_ay;
K_ay = 10^logK_ay
logK_az = slope*log10(3) + b_az;
K_az = 10^logK_az

% Plot the results.
tauK = 3;
lineK_ax = K_ax .* sqrt(tauFromFunc_ax/3);
lineK_ay = K_ay .* sqrt(tauFromFunc_ax/3);
lineK_az = K_az .* sqrt(tauFromFunc_ax/3);

figure
loglog(tauFromFunc_ax, adevFromFunc_ax, 'r', tauFromFunc_ay, adevFromFunc_ay, 'g', tauFromFunc_az, adevFromFunc_az, 'b')
hold on 
loglog(tauFromFunc_ax, lineK_ax,  '--r', tauFromFunc_ay, lineK_ay, '--g', tauFromFunc_az, lineK_az, '--b')
loglog(tauK, K_ax, 'or', tauK, K_ay, 'og', tauK, K_az, 'ob')
hold off

title('Allan Deviation with Rate Random Walk')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('\sigma_a_x', '\sigma_a_y', '\sigma_a_z', '\sigma_K_a_x', '\sigma_K_a_y', '\sigma_K_a_z')

text(tauK, K_ax, 'K_a_x')
text(tauK, K_ay, 'K_a_y')
text(tauK, K_az, 'K_a_z')

grid on
% axis equal

%% Bias Instability

% Find the index where the slope of the log-scaled Allan deviation is equal
% to the slope specified.
slope = 0;
logtau = log10(tauFromFunc_ax);
logadev_ax = log10(adevFromFunc_ax);
dlogadev_ax = diff(logadev_ax) ./ diff(logtau);

[~, i_ax] = min(abs(dlogadev_ax - slope));
[~, i_ay] = min(abs(dlogadev_ay - slope));
[~, i_az] = min(abs(dlogadev_az - slope));


% Find the y-intercept of the line.
b_ax = logadev_ax(i_ax) - slope*logtau(i_ax);
b_ay = logadev_ay(i_ay) - slope*logtau(i_ay);
b_az = logadev_az(i_az) - slope*logtau(i_az);


% Determine the bias instability coefficient from the line.
scfB = sqrt(2*log(2)/pi);

logB_ax = b_ax - log10(scfB);
B_ax = 10^logB_ax
logB_ay = b_ay - log10(scfB);
B_ay = 10^logB_ay
logB_az = b_az - log10(scfB);
B_az = 10^logB_az

% Plot the results.
tauB_ax = tauFromFunc_ax(i_ax);
tauB_ay = tauFromFunc_ax(i_ay);
tauB_az = tauFromFunc_ax(i_az);

lineB_ax = B_ax * scfB * ones(size(tauFromFunc_ax));
lineB_ay = B_ay * scfB * ones(size(tauFromFunc_ax));
lineB_az = B_az * scfB * ones(size(tauFromFunc_ax));

figure
% loglog(tau, adev, tau, lineB, '--', tauB, scfB*B, 'o')
loglog(tauFromFunc_ax, adevFromFunc_ax, 'r', tauFromFunc_ay, adevFromFunc_ay, 'g', tauFromFunc_az, adevFromFunc_az, 'b')
hold on 
loglog(tauFromFunc_ax, lineB_ax,  '--r', tauFromFunc_ay, lineB_ay, '--g', tauFromFunc_az, lineB_az, '--b')
loglog(tauB_ax, scfB*B_ax, 'or', tauB_ay, scfB*B_ay, 'og', tauB_az, scfB*B_az, 'ob')
hold off

title('Allan Deviation with Bias Instability')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('\sigma_a_x', '\sigma_a_y', '\sigma_a_z', '\sigma_B_a_x', '\sigma_B_a_y', '\sigma_B_a_z')

text(tauB_ax, scfB*B_ax, '0.664B_a_x')
text(tauB_ay, scfB*B_ay, '0.664B_a_y')
text(tauB_az, scfB*B_az, '0.664B_a_z')

grid on
% axis equal

%% All Noise Parameters

tauParams = [tauN, tauN, tauN, tauK, tauK, tauK, tauB_ax, tauB_ay, tauB_az];
params = [N_ax, N_ay, N_az, K_ax, K_ay, K_az, scfB*B_ax, scfB*B_ay, scfB*B_az];

set(0,'DefaultLineLineWidth',0.7)
figure
loglog(tauFromFunc_ax, adevFromFunc_ax, 'r', 'LineWidth', 2)
hold on
loglog(tauFromFunc_ay, adevFromFunc_ay, 'g', 'LineWidth', 2)
loglog(tauFromFunc_az, adevFromFunc_az, 'b', 'LineWidth', 2)
loglog(tauFromFunc_ax, [lineN_ax, lineN_ay, lineN_az, lineK_ax, lineK_ay, lineK_az, lineB_ax, lineB_ay, lineB_az], '--', tauParams, params, 'o')
hold off

title('Allan Deviation with Noise Parameters')
xlabel('\tau')
ylabel('\sigma(\tau)')
legend('$\sigma_{ax} (rad/s)$', '$\sigma_{ay} (rad/s)$', '$\sigma_{az} (rad/s)$', ...
    '$\sigma_{Nax} ((rad/s)/\sqrt{Hz})$', '$\sigma_{Nay} ((rad/s)/\sqrt{Hz})$', '$\sigma_{Naz} ((rad/s)/\sqrt{Hz})$', ...
    '$\sigma_{Kax} ((rad/s)\sqrt{Hz})$', '$\sigma_{Kay} ((rad/s)\sqrt{Hz})$', '$\sigma_{Kaz} ((rad/s)\sqrt{Hz})$', ...
    '$\sigma_{Bax} (rad/s)$', '$\sigma_{Bay} (rad/s)$', '$\sigma_{Baz} (rad/s)$', 'Interpreter', 'latex')

text(tauParams, params, {'N_a_x', 'N_a_y', 'N_a_z', 'K_a_x', 'K_a_y', 'K_a_z', '0.664B_a_x', '0.664B_a_y', '0.664B_a_z'})
grid on
% axis equal