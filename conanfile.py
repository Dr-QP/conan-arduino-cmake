from conans import ConanFile
import os


class ArduinoConan(ConanFile):
    name = "arduino"
    version = "1.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino"

    settings = "os", "compiler", "arch"
    exports_sources = "cmake/*", "!build/*", "!test_package/*", "!**/.DS_Store"

    def configure(self):
        archs = ("armv6", "armv7", "armv7hf", "avr")
        gcc_versions = ("4.5", "4.8", "4.9")
        if str(self.settings.os) != "Arduino":
            raise Exception("Only 'os' Arduino supported")
        elif str(self.settings.compiler) not in ("gcc"):
            raise Exception("Not supported compiler, only gcc is available")
        elif str(self.settings.compiler.version) not in gcc_versions:
            raise Exception("Not supported gcc compiler version, %s available" % ', '.join(gcc_versions))
        elif str(self.settings.arch) not in archs:
            raise Exception("Not supported architecture, %s available" % ', '.join(archs))

    def package(self):
        self.copy("cmake/*", dst="", src=".")

    def package_info(self):
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "ArduinoToolchain.cmake")

        self.env_info.ARDUINO_DEFAULT_BOARD = str(self.settings.os.board)
        # ARDUINO_DEFAULT_PORT
        # ARDUINO_DEFAULT_SERIAL
        # ARDUINO_DEFAULT_PROGRAMMER

