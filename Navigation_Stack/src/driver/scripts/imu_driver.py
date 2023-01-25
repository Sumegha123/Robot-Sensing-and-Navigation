#!/usr/bin/env python3

import rospy
import serial
import math
from std_msgs.msg import Header, Float64
from sensor_msgs.msg import Imu, MagneticField


if __name__ == "__main__":
	SENSOR_NAME = "IMU"
	rospy.init_node("IMU_node")
	serial_port = rospy.get_param('~port', '/dev/ttyUSB0')
	serial_baud = rospy.get_param('~baudrate', 115200)
	
	port = serial.Serial(serial_port, serial_baud, timeout=3.)
	port.write(b'VNWRG,07,40*XX')
	rospy.logdebug("Using IMU on port " + serial_port + " at " + str(serial_baud))
	
	pub_imu = rospy.Publisher("IMU", Imu, queue_size=10)
	pub_mag = rospy.Publisher("MagneticField", MagneticField, queue_size=10)

	
	try:
		while not rospy.is_shutdown():
			line = port.readline()


			if (len(line) > 20) and line.startswith(b'$VNYMR'):

				line = str(line).split(",")
				print()
				# Initialize messages
				msg_imu = Imu()
				msg_mag = MagneticField()
				
				
				# Obtain RPY, Accel, Gyro, and Mag data
				try:
					roll_deg = float(line[3])
					pitch_deg = float(line[2])
					yaw_deg = float(line[1])
				
					ax = float(line[7])
					ay = float(line[8])
					az = float(line[9])
				
					gx = float(line[10])
					gy = float(line[11])
					
					#Remove extra data from end of VNYMR string to isolate gz string
					gyroZ = line[12].split('*')
					
					gz = float(gyroZ[0])
				
					mx = float(line[4])
					my = float(line[5])
					mz = float(line[6])
				except: 
					pass
				
				#Convert to radians for quaternion calcs
				roll = math.radians(roll_deg)
				pitch = math.radians(pitch_deg)
				yaw = math.radians(yaw_deg)
				
				#Abreviations for simpler calculations
				cy = math.cos(yaw * 0.5)
				sy = math.sin(yaw * 0.5)
				cp = math.cos(pitch * 0.5)
				sp = math.sin(pitch * 0.5)
				cr = math.cos(roll * 0.5)
				sr = math.sin(roll * 0.5)
				
				#Quaternion Calculations
				qw = cr * cp * cy + sr * sp * sy
				qx = sr * cp * cy - cr * sp * sy
				qy = cr * sp * cy + sr * cp * sy
				qz = cr * cp * sy - sr * sp * cy
				
				
				#Publish imu message
				msg_imu.linear_acceleration.x = ax
				msg_imu.linear_acceleration.y = ay
				msg_imu.linear_acceleration.z = az
				msg_imu.angular_velocity.x = gx
				msg_imu.angular_velocity.y = gy
				msg_imu.angular_velocity.z = gz
				
				#msg_imu.roll = roll_deg
				#msg_imu.pitch = pitch_deg
				#msg_imu.yaw = yaw_deg
				msg_imu.orientation.w = qw
				msg_imu.orientation.x = qx
				msg_imu.orientation.y = qy
				msg_imu.orientation.z = qz
				
				#msg docs ask for tesla (gauss/10000), but I'll send gauss instead for easier plotting
				msg_mag.magnetic_field.x = mx
				msg_mag.magnetic_field.y = my
				msg_mag.magnetic_field.z = mz
				
				
				pub_imu.publish(msg_imu)
				pub_mag.publish(msg_mag)

				
				print(f"accelX, accelY, accelZ: {line[7]}, {line[8]}, {line[9]}")
				print(f"gyroX, gyroY, gyroZ: {line[10]}, {line[11]}, {gyroZ[0]}")
				print(f"roll, pitch, yaw: {roll_deg}, {pitch_deg}, {yaw_deg}")
				print(f"magX, magY, magZ: {line[4]}, {line[5]}, {line[6]}")
				print(f"quat(wxyz): {qw}, {qx}, {qy}, {qz}")
				
	except rospy.ROSInterruptException:
		port.close()
		
		
		
		
