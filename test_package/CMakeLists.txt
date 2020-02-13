# Define CMake's minimum version (must-do) and the project's name and supported languages
cmake_minimum_required(VERSION 3.8.2)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Call a framework utility function, passing it information about the hardware board that will be used - This function returns a structure known only to the framework
# get_board_id(board_id uno)

# Create an executable suitable for Arduino using CMake-style target-creation
# add_arduino_executable(Hello_Arduino ${board_id} example.cpp)
# Upload the created target through a connected Serial Port (Where your board is connected to)
# upload_arduino_target(Hello_Arduino "${board_id}" COM3) # disabled for test packages


arduino_cmake_project(Sketch BOARD_NAME nano BOARD_CPU atmega328)

add_arduino_executable(Sketch)
target_sketches(Sketch example.ino)
