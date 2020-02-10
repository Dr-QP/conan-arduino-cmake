from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy
import os


username = os.getenv("CONAN_USERNAME", "conan")
channel = os.getenv("CONAN_CHANNEL", "testing")

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="missing")
    settings = {
        "os": "Arduino",
        "os.board": "uno",
        "compiler": "gcc",
        "compiler.version": "7.3",
        "compiler.libcxx": "libstdc++11",
        "arch": "avr"
    }
    build_requires = {
        "*": [f"arduino-sdk/1.8.11@{username}/{channel}",
        "cmake_installer/3.16.3@conan/stable"
        ]
    }
    if os_info.is_linux:
        builder.add(settings, options={"arduino-sdk:host_os": "linux32"}, build_requires=build_requires)
        builder.add(settings, options={"arduino-sdk:host_os": "linux64"}, build_requires=build_requires)
    else:
        builder.add(settings, build_requires=build_requires)

    builder.run()
