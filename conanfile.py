from conans import ConanFile
import os


class ArduinoConan(ConanFile):
    name = "arduino"
    version = "1.0.0"
    license = "Mozilla Public License, v. 2.0 http://mozilla.org/MPL/2.0/"
    url = "https://github.com/Dr-QP/conan-arduino"

    settings = {
        "os": ["Arduino"],
        "compiler": {
            "gcc": {
                "version": ["4.5", "4.8", "4.9"],
                "libcxx": ["libstdc++", "libstdc++11"]
            }
        },
        "arch": ["armv6", "armv7", "armv7hf", "avr"]
    }
    exports_sources = "cmake/*", "!build/*", "!test_package/*", "!**/.DS_Store"

    def package(self):
        self.copy("cmake/*", dst="", src=".")

    def package_info(self):
        self.env_info.CONAN_CMAKE_TOOLCHAIN_FILE = os.path.join(
            self.package_folder, "cmake", "ArduinoToolchain.cmake")
