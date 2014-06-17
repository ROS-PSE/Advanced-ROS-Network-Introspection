"""Only concepts so far, no usable code!!!"""

import rospy
import threading

rospy.wait_for_service('/chat_cam/set_image_scale')
image_scale_proxy = rospy.ServiceProxy('/chat_cam/set_image_scale', SetImageScale)

# for logging use this:
rospy.loginfo("warped size: (%s, %s)" % self.iw.x.T.shape)
# loglevel can be set individually when calling init_node(...)

#multiple subscribers
rospy.Subscriber('image', sensor_msgs.msg.Image, self.image_cb)
rospy.Subscriber('camera_info', sensor_msgs.msg.CameraInfo, self.info_cb)
# no need for the rospy.spin() if the programm enters another loop -> the thread will do sensor_msgs

# !!! Use locks to prevent unwanted side effects
info_lock  = threading.Lock()
info = None

 def info_cb(self, info):
 	#important to lock the info method. is simultaneous entrance in the method possible at all?
                with self.info_lock:
                        self.info = info