from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os

available_options = ['master', 'v0.6.1', 'v0.6', ]

class ArduinoConan(ConanFile):
    name = "arduino-toolchain"
    version = "3.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino-toolchain"
    description = "Arduino build toolchain. Use it with build_requires"
    
    settings = "os"
    options = {
        "version": 'ANY'
    }
    default_options = {
        "version": available_options[0]
    }

    def configure(self):
        import sys
        is_64bits = sys.maxsize > 2 ** 32

        if str(self.settings.os) != "Arduino":
            raise ConanInvalidConfiguration(f"OS '{self.settings.os}' is not supported, only `Arduino` is supported.")

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/arduino-cmake/Arduino-CMake-NG.git", self.options.version)

    def package_id(self):
        # Toolchain is settings agnostic
        self.info.header_only()

    def package(self):
        self.copy("cmake/*")

    def package_info(self):
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "Arduino-Toolchain.cmake")
