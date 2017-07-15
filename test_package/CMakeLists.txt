project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

generate_arduino_firmware(${PROJECT_NAME}
        SKETCH example.ino
#        ARDLIBS StandardCplusplus
        )
