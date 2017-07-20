from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy


class ArduinoPackager(ConanMultiPackager):

    def add(self, options):
        new_options = copy.copy(options)
        new_options["conan-arduino-toolchain:arduino_version"] = "1.8.3"

        super(self.__class__, self).add(settings={
            "os": "Arduino",
            "os.board": "uno",
            "compiler": "gcc",
            "compiler.version": "4.9",
            "compiler.libcxx": "libstdc++11",
            "arch": "avr"
        }, options=new_options
        , env_vars={
            "CC": "gcc"
        })

if __name__ == "__main__":
    builder = ArduinoPackager(args="--build missing",
                              reference="arduino-toolchain/1.0.0")
    builder.add(options={
        "ardiono-sdk:use_bundled_java": False
    })
    if os_info.is_linux or os_info.is_windows:
        builder.add(options={
            "ardiono-sdk:use_bundled_java": True
        })

    if os_info.is_linux:
        filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            filtered_builds.append(
                [settings, options, env_vars, build_requires])
            new_options = copy.copy(options)
            new_options["ardiono-sdk:host_os"] = "linux32"
            filtered_builds.append(
                [settings, new_options, env_vars, build_requires])
        builder.builds = filtered_builds

    builder.run()
