from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy


class ArduinoPackager(ConanMultiPackager):

    def add(self, options={}):
        super(self.__class__, self).add(settings={
            "os": "Arduino",
            "os.board": "uno",
            "compiler": "gcc",
            "compiler.version": "4.9",
            "compiler.libcxx": "libstdc++11",
            "arch": "avr"
        }, options=options
        , env_vars={
            "CC": "gcc"
        })

if __name__ == "__main__":
    builder = ArduinoPackager(reference="arduino-toolchain/1.8.3")
    builder.add()
    builder.build_policy = "missing"

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
