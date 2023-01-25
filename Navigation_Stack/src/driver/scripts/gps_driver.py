#!/usr/bin/env python3

import rospy
import serial
import utm
from std_msgs.msg import Float64, Header, Int32, String
from lab4.msg import gps_msg


if __name__ == "__main__":
	SENSOR_NAME = "GPS_PUCK"
	rospy.init_node("GPS_node")
	serial_port = rospy.get_param('~port', '/dev/ttyUSB1')
	serial_baud = rospy.get_param('~baudrate', 4800)
	
	port = serial.Serial(serial_port, serial_baud, timeout=3.)
	rospy.logdebug("Using GPS puck on port " + serial_port + " at " + str(serial_baud))
	
	pub = rospy.Publisher("GPS_data", gps_msg, queue_size=10)

	
	try:
		while not rospy.is_shutdown():
			line = port.readline()

			if line.startswith(b'$GPGGA'):
				line = str(line).split(",")
				msg = gps_msg()
				if (line[2] == ""):
					continue;
				lat = float(line[2]) / 100.0
				lon = -float(line[4]) / 100 # plz dont take marks off grader, imma be in the western hemisphere for a while
				alt = float(line[9])
				

				[easting, northing, zone, letter] = utm.from_latlon(lat, lon)

				msg.lat = lat
				msg.lon = lon
				msg.alt = alt
				msg.utm_easting = easting
				msg.utm_northing = northing
				msg.zone = zone
				msg.letter = letter
				
				pub.publish(msg)

				
				print(f"lat, long, alt: {lat}, {lon}, {alt}")
				print(f"easting, northing: {easting}, {northing}")
				print(f"zone and letter: {zone}{letter}")
				
	except rospy.ROSInterruptException:
		port.close()
		
		
		
		
