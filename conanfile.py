from conans import ConanFile
from conans.tools import os_info, SystemPackageTool
from conans.errors import ConanInvalidConfiguration
import os

class ArduinoConan(ConanFile):
    name = "arduino-toolchain"
    version = "2.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino-toolchain"
    description = "Arduino build toolchain. Use it with build_requires"
    settings = "os"
    exports_sources = "cmake/*"
    options = {
        "arduino_path": "ANY"	
    }
    default_options = "arduino_path=None"

    @property	
    def arduino_path(self):
        path = self.options.arduino_path
        return os.path.expanduser(str(path)) if path else None

    def configure(self):
        import sys
        is_64bits = sys.maxsize > 2 ** 32

        if str(self.settings.os) != "Arduino":
            raise ConanInvalidConfiguration(f"OS '{self.settings.os}' is not supported, only `Arduino` is supported.")

        if self.arduino_path and not os.path.exists(self.arduino_path):
            raise ConanInvalidConfiguration(f"arduino_path option is invalid. path {self.arduino_path} does not exist %s")

    def package_id(self):
        # Toolchain doesn't really depend on any of these settings, so package id should be platform agnostic
        self.info.header_only()

    def package(self):
        self.copy("cmake/*", dst="", src=".")

    def package_info(self):
        self.env_info.CMAKE_HOST_SYSTEM_NAME = "Arduino"
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "ArduinoToolchain.cmake")
        self.env_info.ARDUINO_DEFAULT_BOARD = str(self.settings.os.board)

        if self.arduino_path:	
            self.env_info.ARDUINO_SDK_PATH = str(self.arduino_path)
