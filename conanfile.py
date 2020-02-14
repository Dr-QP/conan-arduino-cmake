from conans import ConanFile
from conans.tools import os_info, SystemPackageTool
from conans.errors import ConanInvalidConfiguration
import os

class ArduinoConan(ConanFile):
    name = "arduino-cmake"
    version = "1.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino-cmake"
    description = "Arduino cmake toolchain. Use it with build_requires"
    settings = "os"
    exports_sources = "cmake/*"

    def configure(self):
        import sys
        is_64bits = sys.maxsize > 2 ** 32


        if str(self.settings.os) != "Arduino":
            raise ConanInvalidConfiguration(f"OS '{self.settings.os}' is not supported, only `Arduino` is supported.")

    def package_id(self):
        # Toolchain doesn't really depend on any of these settings, so package id should be platform agnostic
        self.info.header_only()

    def package(self):
        self.copy("cmake/*", dst="", src=".")

    def package_info(self):
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "ArduinoToolchain.cmake")
        self.env_info.ARDUINO_DEFAULT_BOARD = str(self.settings.os.board) # TODO: remote in future updates
