cmake_minimum_required(VERSION 2.8.3)
project(vigir_template_library)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES vigir_template_library
#  CATKIN_DEPENDS roscpp rospy
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
    src/graspit_mm_to_m.py
    src/right_to_left.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY debris
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


install(DIRECTORY door
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


install(DIRECTORY hose
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY standpipe
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY tools
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY valve
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY vehicle
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(FILES
	ghost_poses.csv
	grasp_ids.txt
	grasp_library.grasp
	grasp_library_hook.grasp
	grasp_library_irobot.grasp
	grasp_library_robotiq.grasp
	grasp_templates.txt
	hand_poses.csv
	sandia_left_hand.urdf
	sandia_right_hand.urdf
	template_library.yaml
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
	
)

