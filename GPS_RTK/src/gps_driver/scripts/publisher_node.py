#!/usr/bin/env python
import rospy
import serial
import utm
import math
from std_msgs.msg import String
from gps_driver.msg import gps_data_msg


if __name__ == '__main__':
    SENSOR_NAME = "gps_puck"
    rospy.init_node('gps_data')
    serial_port = rospy.get_param('~port','/dev/ttyACM0')
    serial_baud = rospy.get_param('~baudrate',4800)
    sampling_rate = rospy.get_param('~sampling_rate',5.0)
    port = serial.Serial(serial_port, serial_baud, timeout=3.)
    
    rospy.logdebug("Using gps puck on port "+serial_port+" at "+str(serial_baud))
    
    sampling_count = int(round(1/(sampling_rate*0.007913)))
    
    #rospy.logdebug("Initializing sensor with *0100P4\\r\\n ...")
	
    rospy.logdebug("Initialization complete")
    
    rospy.loginfo("Reading data")
    
    #sleep_time = 1/sampling_rate-0.025
    
    pub = rospy.Publisher("gps_puck_data",gps_data_msg,queue_size=10)
    
    	
    try:
        while not rospy.is_shutdown():
            line = port.readline()
            #line1 = line.decode()
            
            if line == '':
                rospy.logwarn("GPS: No data")
            else:
                if line.startswith(b'$GNGGA'):
                    
                    x=line.split(b',')
                    msg = gps_data_msg()
                    msg.header.stamp = rospy.get_rostime()
                    m = 1
                    n = 1
                        
                    #latitude
                    lat = x[2]
         
                    lat_dir = (x[3])
                    lat_dd = float(lat[:2])
                    lat_mm = float(lat[2:])
                    
                        
                    #longitude
                    longit = x[4]
                    long_dir = (x[5])
                    #print(long_dir)
                    long_dd = float(longit[:3])
                    long_mm = float(longit[3:])
                        
                    if(lat_dir == 'S'):
                        m=-1
                        
                    if(long_dir == 'W'):
                        n=-1
                   
                    msg.latitude = m*(lat_dd+(lat_mm/60))
                    #print("Latitude: ",msg.latitude)
                    msg.longitude = n*(long_dd+(long_mm/60))
                    #print("Longitude",msg.longitude)
                        
                    #altitude
                    msg.altitude = float(x[9])
                    #print("Altitude",msg.altitude)
                    
                    msg.gps_quality = x[6]
                        
                    msg.utm_easting, msg.utm_northing, msg.zone, msg.letter =  utm.from_latlon(msg.latitude,msg.longitude) 
                    #print("Others",msg.utm_easting,msg.utm_northing,msg.zone,msg.letter)
                    pub.publish(msg)
                        
            
    except rospy.ROSInterruptException: 
        port.close()
        
        	

