clc
clear all
close all
format long;

file_path ="individual2.bag"

bag = rosbag(file_path);
bagInfo = rosbag('info',file_path);
bSel = select(bag,'Topic','MagneticField');
msgStructs = readMessages(bSel,'DataFormat','struct');
msgStructs{1};
% Orientation_X = cellfun(@(m) double(m.Orientation.X), msgStructs);
% Orientation_Y = cellfun(@(m) double(m.Orientation.Y), msgStructs);
% Orientation_Z = cellfun(@(m) double(m.Orientation.Z), msgStructs);
% LinearAcceleration_x = cellfun(@(m) double(m.LinearAcceleration.X), msgStructs);
% LinearAcceleration_y = cellfun(@(m) double(m.LinearAcceleration.Y), msgStructs);
% LinearAcceleration_z = cellfun(@(m) double(m.LinearAcceleration.Z), msgStructs);
% AngularVelocity_x = cellfun(@(m) double(m.AngularVelocity.X), msgStructs);
% AngularVelocity_y = cellfun(@(m) double(m.AngularVelocity.Y), msgStructs);
% AngularVelocity_z = cellfun(@(m) double(m.AngularVelocity.Z), msgStructs);
Magx= cellfun(@(m) double(m.MagneticField_.X), msgStructs);
Magy= cellfun(@(m) double(m.MagneticField_.Y), msgStructs);
Magz= cellfun(@(m) double(m.MagneticField_.Z), msgStructs);
timePoints_index = cellfun(@(m) int64(m.Header.Seq),msgStructs);
timePoints_index = timePoints_index - min(timePoints_index);

% lin_x_mean = mean(LinearAcceleration_x)
% lin_x_std = std(LinearAcceleration_x)
% lin_x = normpdf(LinearAcceleration_x,lin_x_mean,lin_x_std);
% 
% figure
% hold on
% plot(timePoints_index, LinearAcceleration_x)
% title('Linear Acceleration in X vs Time')
% xlabel('Time');
% ylabel('Linear Acceleration X')
% grid on
% hold off
% % 
% figure
% plot(LinearAcceleration_x, lin_x)
% title('Linear Acceleration Gaussian Noise Plot')
% xlabel('Linear Acceleration X');
% ylabel('')
% grid on
% % 
% lin_y_mean = mean(LinearAcceleration_y)
% lin_y_std = std(LinearAcceleration_y)
% lin_y= normpdf(LinearAcceleration_y,lin_y_mean,lin_y_std);
% % 
% figure
% hold on
% plot(timePoints_index, LinearAcceleration_y)
% title('Linear Acceleration in Y vs Time')
% xlabel('Time');
% ylabel('Linear Acceleration Y')
% grid on
% hold off
% % 
% figure
% plot(LinearAcceleration_y, lin_y)
% title('Linear Acceleration Gaussian Noise Plot')
% xlabel('Linear Acceleration Y');
% ylabel('')
% grid on
% % 
% lin_z_mean = mean(LinearAcceleration_z)
% lin_z_std = std(LinearAcceleration_z)
% lin_z= normpdf(LinearAcceleration_z,lin_z_mean,lin_z_std);
% % 
% figure
% hold on
% plot(timePoints_index, LinearAcceleration_y)
% title('Linear Acceleration in Z vs Time')
% xlabel('Time');
% ylabel('Linear Acceleration Z')
% grid on
% hold off
% % 
% figure
% plot(LinearAcceleration_z, lin_z)
% title('Linear Acceleration Gaussian Noise Plot')
% xlabel('Linear Acceleration Z');
% ylabel('')
% grid on
% 
% 
% ang_x_mean = mean(AngularVelocity_x)
% ang_x_std = std(AngularVelocity_x)
% ang_x = normpdf(AngularVelocity_x,ang_x_mean,ang_x_std);
% 
% % figure
% hold on
% plot(timePoints_index, AngularVelocity_x)
% title('Angular Velocity X vs Time')
% xlabel('Time');
% ylabel('Angular Velocity X')
% grid on
% hold off
% 
% figure
% plot(AngularVelocity_x, ang_x)
% title('Angular Velocity Gaussian Noise')
% xlabel('AngularVelocity X');
% ylabel("")
% grid on
% 
% 
% ang_y_mean = mean(AngularVelocity_y)
% ang_y_std = std(AngularVelocity_y)
% ang_y = normpdf(AngularVelocity_y,ang_y_mean,ang_y_std);
% 
% figure
% plot(timePoints_index, AngularVelocity_y)
% title('AngularVelocity Y vs Time')
% xlabel('Time');
% ylabel('AngularVelocity Y')
% grid on 
% 
% figure
% plot(AngularVelocity_y, ang_y)
% title('Angular Velocity Gaussian Noise')
% xlabel('AngularVelocity Y');
% ylabel("")
% grid on
% 
% ang_z_mean = mean(AngularVelocity_z)
% ang_z_std = std(AngularVelocity_z)
% ang_z = normpdf(AngularVelocity_z,ang_z_mean,ang_z_std);
% 
% 
% figure
% plot(timePoints_index, AngularVelocity_z)
% title('Angular Velocity Z vs Time')
% xlabel('Time');
% ylabel('Angular Velocity Z')
% grid on
% 
% figure
% plot(AngularVelocity_z, ang_z)
% title('Angular Velocity Gaussian Noise')
% xlabel('AngularVelocity Z');
% ylabel("")
% grid on
% 
% figure 
% plot3(AngularVelocity_x,AngularVelocity_y,AngularVelocity_z, ".")
% title('Angular Velocity Point Cloud')
% xlabel('AngularVelocity X');
% ylabel('AngularVelocity Y')
% zlabel("AngularVelocity Z")
% axis equal 
% grid on

mag_x_mean = mean(Magx)
mag_x_std = std(Magx)
mag_x = normpdf(Magx,mag_x_mean,mag_x_std);

% 
% figure
% plot(timePoints_index, Magx)
% title('Magnetic Field vs Time')
% xlabel('Time');
% ylabel('Magnetic Field X')
% grid on
% 
% figure
% plot(Magx, mag_x)
% title('Magnetic Field Gaussian Noise')
% xlabel('Magnetic Field X');
% ylabel("")
% grid on

mag_y_mean = mean(Magy)
mag_y_std = std(Magy)
mag_y = normpdf(Magy,mag_y_mean,mag_y_std);

% 
% figure
% plot(timePoints_index, Magy)
% title('Magnetic Field vs Time')
% xlabel('Time');
% ylabel('Magnetic Field Y')
% grid on
% 
% figure
% plot(Magy, mag_y)
% title('Magnetic Field Gaussian Noise')
% xlabel('Magnetic Field Y');
% ylabel("")
% grid on
% 
mag_z_mean = mean(Magz)
mag_z_std = std(Magz)
mag_z = normpdf(Magz,mag_z_mean,mag_z_std);
% 
% 
% figure
% plot(timePoints_index, Magz)
% title('Magnetic Field vs Time')
% xlabel('Time');
% ylabel('Magnetic Field Z')
% grid on
% 
% figure
% plot(Magz, mag_z)
% title('Magnetic Field Gaussian Noise')
% xlabel('Magnetic Field Z');
% ylabel("")
% grid on

% figure 
plot3(Magx, Magy, Magz, '.')
title('Magnetic Field Point Cloud')
xlabel('Magnetic Field X');
ylabel('Magnetic Field Y')
zlabel("Magnetic Field Z")
axis equal 
grid on