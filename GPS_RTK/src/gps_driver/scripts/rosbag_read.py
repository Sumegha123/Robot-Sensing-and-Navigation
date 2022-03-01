#!/usr/bin/env python
import rosbag

if __name__ == '__main__':
    bag = rosbag.Bag('rosbag_files/2022-02-06-17-59-50.bag')
    
    for(topic,msg,t) in bag.read_messages():
        print(topic,msg,t)
        
      
