from conans import ConanFile, CMake, tools
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "anton-matosov")


class ConanarduinosdkTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "conan-arduino-toolchain/1.0.0@%s/%s" % (username, channel)
    default_options = "conan-arduino-toolchain:arduino_version=1.8.3"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        args = []
        if tools.os_info.is_windows:
            args = ["-DCMAKE_MAKE_PROGRAM=" + str(self.deps_env_info.CMAKE_MAKE_PROGRAM)]
        cmake.configure(args=args, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        self.output.success("Done")
