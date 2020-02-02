#=============================================================================#
# Author: Tomasz Bogdal (QueezyTheGreat)
# Home:   https://github.com/queezythegreat/arduino-cmake
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#=============================================================================#
set(CMAKE_SYSTEM_NAME Arduino)

set(CMAKE_C_COMPILER   avr-gcc CACHE STRING "Arduino C compiler")
set(CMAKE_CXX_COMPILER avr-g++ CACHE STRING "Arduino C++ compiler")

# Add current directory to CMake Module path automatically
if(EXISTS  ${CMAKE_CURRENT_LIST_DIR}/Platform/Arduino.cmake)
    set(CMAKE_MODULE_PATH  ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR})
endif()

set(CONAN_ARDUINO_SDK_PATH $ENV{CONAN_ARDUINO_SDK_PATH})

#=============================================================================#
#                         System Paths                                        #
#=============================================================================#
if(UNIX)
    include(Platform/UnixPaths)
    if(APPLE)
        list(APPEND CMAKE_SYSTEM_PREFIX_PATH $CONAN_ARDUINO_SDK_PATH)
    endif()
elseif(WIN32)
    include(Platform/WindowsPaths)
endif()

find_path(ARDUINO_SDK_PATH
          NAMES lib/version.txt
          PATH_SUFFIXES share/arduino
                        Contents/Java
          HINTS ${CONAN_ARDUINO_SDK_PATH}
          DOC "Arduino SDK path.")

if(ARDUINO_SDK_PATH)
    list(APPEND CMAKE_SYSTEM_PREFIX_PATH ${ARDUINO_SDK_PATH}/hardware/tools/avr)
    list(APPEND CMAKE_SYSTEM_PREFIX_PATH ${ARDUINO_SDK_PATH}/hardware/tools/avr/utils)
    set(CMAKE_SYSTEM_PREFIX_PATH ${CMAKE_SYSTEM_PREFIX_PATH} CACHE STRING "Updated CMAKE_SYSTEM_PREFIX_PATH with arduino toolchain")
else()
    message(FATAL_ERROR "Could not find Arduino SDK (set ARDUINO_SDK_PATH)!")
endif()

set(ARDUINO_CPUMENU)
if(ARDUINO_CPU)
    set(ARDUINO_CPUMENU ".menu.cpu.${ARDUINO_CPU}")
endif(ARDUINO_CPU)

