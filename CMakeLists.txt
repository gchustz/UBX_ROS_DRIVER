cmake_minimum_required(VERSION 2.8.3)
project(UBX_ROS_DRIVEr)

## Find catkin macros and libraries
find_package( catkin REQUIRED COMPONENTS  
              std_msgs 
              geometry_msgs)

##################
## Run setup.py ##
##################
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

# Generate messages in the 'msg' folder
#add_message_files(
#  DIRECTORY msg
#  FILES
#)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)


###################################
## catkin specific configuration ##
###################################

# Declare things to be passed to dependent projects
catkin_package(
  CATKIN_DEPENDS 
  #message_runtime
  std_msgs
  geometry_msgs
  sensor_msgs
)

###########
## Build ##
###########

# Specify additional locations of header files
include_directories()