# import libraries
import rospy
import ubxtranslator
import geometry_msgs
import std_msgs 
import sensor_msgs
import math


# For this to work, you need ubxtranslator package from pip
class HPPOSLLH_publisher:
    def __init__(self, topic_str, header_id_str ) :

        # Generate internal publisher and message object
        self.publisher = rospy.Publisher(topic_str, sensor_msgs.NatSatFix, queue_size=10)
        self.msg = sensor_msgs.NatSatFix()

        # Fill some details of the msg that will not change:
        self.msg.position_covariance_type = 3
        self.msg.status = sensor_msgs.NavSatStatus()
        self.msg.status.status = 0
        self.msg.status.service = 15

        self.msg.header = std_msgs.Header()
        self.msg.header.seq = -1
        self.msg.header.frame_id = header_id_str

    def pub(self, ubx_msg, timestamp):
        # Check that the message is valid
        if ubx_msg[1] == 'HPPOSLLH' :

            if ubx_msg[2][3] != 0 and ubx_msg[2][4] != 0:
                self.msg.header.seq += 1
                self.msg.header.stamp = timestamp

                # Populate the message and publish
                self.msg.longitude = float(ubx_msg[2][3])*1e-7 # Longituge
                self.msg.latitude = float(ubx_msg[2][4])*1e-7 # latitude
                self.msg.altitude = float(ubx_msg[2][5])*1e-3 # Height

                lat_err = float(ubx_msg[2][11])*1e-4
                lon_err = float(ubx_msg[2][11])*1e-4
                alt_err = float(ubx_msg[2][12])*1e-4

                self.msg.position_covariance = [lon_err, 0, 0, 0, lat_err, 0, 0, 0, alt_err]


                self.publisher.publish( self.msg )


class POSLLH_publisher:
    def __init__(self, topic_str, header_id_str ) :

        # Generate internal publisher and message object
        self.publisher = rospy.Publisher(topic_str, sensor_msgs.NatSatFix, queue_size=10)
        self.msg = sensor_msgs.NatSatFix()

        # Fill some details of the msg that will not change:
        self.msg.position_covariance_type = 3
        self.msg.status = sensor_msgs.NavSatStatus()
        self.msg.status.status = 0
        self.msg.status.service = 15

        self.msg.header = std_msgs.Header()
        self.msg.header.seq = -1
        self.msg.header.frame_id = header_id_str

    def pub(self, ubx_msg, timestamp):
        # Check that the message is valid
        if ubx_msg[1] == 'POSLLH' :
            self.msg.header.seq += 1
            self.msg.header.stamp = timestamp

            # Populate the message and publish
            self.msg.longitude = float(ubx_msg[2][1])*1e-7 # Longituge
            self.msg.latitude = float(ubx_msg[2][2])*1e-7 # latitude
            self.msg.altitude = float(ubx_msg[2][3])*1e-3 # Height

            lat_err = float(ubx_msg[2][5])*1e-4
            lon_err = float(ubx_msg[2][5])*1e-4
            alt_err = float(ubx_msg[2][6])*1e-4

            self.msg.position_covariance = [lon_err, 0, 0, 0, lat_err, 0, 0, 0, alt_err]


            self.publisher.publish( self.msg )

class RELPOS2D_publisher: # Convert to transform stamped message
    def __init__(self, topic_str, header_id_str):
        # Generate internal publisher and message object
        self.publisher = rospy.Publisher(topic_str, geometry_msgs.TransformStamped, queue_size=10)
        self.msg = geometry_msgs.TransformStamped()

        self.msg.header = std_msgs.Header()
        self.msg.header.seq = -1
        self.msg.header.frame_id = header_id_str
        self.msg.child_frame_id = 'null' # Since we are only using the transform to contain some random info as a default ros message

        
    def pub(self, ubx_msg, timestamp):

        if ubx_msg[1] == 'RELPOS2D' :

            # Write the message
            self.msg.header.seq += 1
            self.msg.header.stamp = timestamp
            self.msg.translation.x = float(ubx_msg[2][3])*1e-3
            self.msg.translation.y = float(ubx_msg[2][4])*1e-3
            self.msg.translation.z = float(ubx_msg[2][5])*1e-3
            
            self.msg.rotation.x = cos(float(msg[2][7])*1e-5 * math.pi / 180) 
            self.msg.rotation.y = 0 # y_hat * sin(ang/2)
            self.msg.rotation.z = 0 # z_hat * sin(ang/2)
            self.msg.rotation.w = sin(float(msg[2][7])*1e-5 * math.pi / 180) 

            self.publisher.publish( self.msg )

class DGPS_publisher:
    def __init__(self, topic_str, header_id_str):
        # Initialize the publisher
        self.publisher = rospy.Publisher(topic_str, geometry_msgs.PoseStamped, queue_size=10)
        self.msg = geometry_msgs.PoseStamped()
        
        self.msg.header.frame_id = header_id_str
        self.msg.header.seq = -1 

        self.msg.pose.quaternion.x = 0
        self.msg.pose.quaternion.y = 0
        self.msg.pose.quaternion.z = 0
        self.msg.pose.quaternion.w = 1

    def pub(self, ubx_msg, timestamp):

        # Write the message
        self.msg.header.stamp = timestamp

        # Check that the message is valid
        if ubx_msg[1] == 'HPPOSLLH' :

            if ubx_msg[2][3] != 0 and ubx_msg[2][4] != 0:
                self.msg.header.seq += 1
                self.msg.header.stamp = timestamp

                # Populate the message and publish
                self.msg.position.x = float(ubx_msg[2][3])*1e-7 # Longituge
                self.msg.position.y = float(ubx_msg[2][4])*1e-7 # latitude
                self.msg.position.z = float(ubx_msg[2][5])*1e-3 # Height

                self.publisher.publish( self.msg )

        elif ubx_msg[1] == 'RELPOS2D' :

            # Write the message
            
            self.msg.quaternion.x = cos(float(msg[2][7])*1e-5 * math.pi / 180) 
            self.msg.quaternion.y = 0 # y_hat * sin(ang/2)
            self.msg.quaternion.z = 0 # z_hat * sin(ang/2)
            self.msg.quaternion.w = sin(float(msg[2][7])*1e-5 * math.pi / 180) 

