from conans import ConanFile
from conans.tools import os_info, SystemPackageTool
import os


class ArduinoConan(ConanFile):
    name = "conan-arduino-toolchain"
    version = "1.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino-toolchain"
    description = "Arduino build toolchain. Use it with build_requires"
    settings = "os", "compiler", "arch"
    exports_sources = "cmake/*", "!build/*", "!test_package/*", "!**/.DS_Store"
    options = {
        "arduino_version": ["1.8.3", "ANY", "none"],
        "arduino_path": "ANY"
    }
    default_options = "arduino_version=none", "arduino_path=none"
    requires = "conan-arduino-sdk/%s@anton-matosov/stable" % options["arduino_version"]

    arduino_path = ""

    def configure(self):
        archs = ("armv6", "armv7", "armv7hf", "avr")
        gcc_versions = ("4.5", "4.8", "4.9")
        if str(self.settings.os) != "Arduino":
            raise Exception("OS '%s' is not supported. Only 'os' Arduino supported.", str(self.settings.os))
        elif str(self.settings.compiler) not in ("gcc"):
            raise Exception("Not supported compiler, only gcc is available")
        elif str(self.settings.compiler.version) not in gcc_versions:
            raise Exception("Not supported gcc compiler version, %s available" % ', '.join(gcc_versions))
        elif str(self.settings.arch) not in archs:
            raise Exception("Not supported architecture, %s available" % ', '.join(archs))

    def requirements(self):
        if os_info.is_windows:
            self.requires("mingw-installer/0.1@anton-matosov/testing")

    def package_id(self):
        # Toolchain doesn't really depend on any of these settings, so package id should be platform agnostic
        self.info.settings.os = ""
        self.info.settings.os.board = ""
        self.info.settings.arch = ""
        self.info.settings.compiler = ""
        self.info.settings.compiler.version = ""

    def build(self):
        self.arduino_path = str(self.options.arduino_path)

    def package(self):
        self.copy("cmake/*", dst="", src=".")

    def package_info(self):
        self.env_info.CMAKE_HOST_SYSTEM_NAME = "Arduino"
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "ArduinoToolchain.cmake")

        self.env_info.ARDUINO_DEFAULT_BOARD = str(self.settings.os.board)
        if os_info.is_windows:
            self.env_info.CMAKE_MAKE_PROGRAM = os.path.join(self.deps_env_info.MINGW_PATH, "bin", "make.exe")
        # Add to the System Path:  ${ARDUINO_SDK_PATH}/hardware/tools/avr/utils/bin

        # ARDUINO_DEFAULT_PORT
        # ARDUINO_DEFAULT_SERIAL
        # ARDUINO_DEFAULT_PROGRAMMER

