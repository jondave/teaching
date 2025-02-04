cmake_minimum_required(VERSION 3.5)
project(uol_turtlebot_simulator)

# Add support for C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()



find_package(ament_cmake REQUIRED)
set(INCLUDE_DIRS ${ament_cmake_INCLUDE_DIRS})
include_directories(${INCLUDE_DIRS})
set(LIBRARY_DIRS ${ament_cmake_LIBRARIES})
set(LIBS ${ament_cmake_LIBRARIES})

# if(CMAKE_HOST_UNIX)
#   catkin_add_env_hooks(90.gazebo_models_uol
#     SHELLS sh
#     DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/env-hooks)
# else()
#   message(FATAL_ERROR "Only UNIX builds supported.")
#   #  catkin_add_env_hooks(90.gazebo_models_oru SHELLS bat DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/env-hooks)
# endif()

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/90.gazebo_models_uol.dsv.in")

#############
## Install ##
#############

install(PROGRAMS
        scripts/twist_watchdog.py
        DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

install(DIRECTORY models DESTINATION share/${PROJECT_NAME})

install(DIRECTORY maps DESTINATION share/${PROJECT_NAME})

install(DIRECTORY meshes DESTINATION share/${PROJECT_NAME})

install(DIRECTORY param DESTINATION share/${PROJECT_NAME})

install(DIRECTORY urdf DESTINATION share/${PROJECT_NAME})

install(DIRECTORY worlds DESTINATION share/${PROJECT_NAME})

install(DIRECTORY
  DESTINATION share/${PROJECT_NAME}/worlds
  FILES_MATCHING
  PATTERN "*.world")
install(DIRECTORY
  DESTINATION share/${PROJECT_NAME}/worlds
  FILES_MATCHING
  PATTERN "*.mz")
# install(DIRECTORY ./models/color_wall_marker ./gzmaze/mouse ./gzmaze/maze_base
#   DESTINATION share/${PROJECT_NAME}/models/)

ament_export_dependencies(ament_cmake)
ament_export_include_directories(${INCLUDE_DIRS})

ament_package()
