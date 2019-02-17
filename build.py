from conan.packager import ConanMultiPackager
from conans.tools import os_info
import copy


class ArduinoPackager(ConanMultiPackager):

    def add(self, options={}):
        super().add(settings={
            "os": "Arduino",
            "os.board": "uno",
            "compiler": "gcc",
            "compiler.version": "5.4",
            "compiler.libcxx": "libstdc++11",
            "arch": "avr"
        }, options=options
        , env_vars={
            "CC": "gcc"
        })

if __name__ == "__main__":
    builder = ArduinoPackager(build_policy = "outdated")
    builder.add()

    if os_info.is_linux:
        filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            filtered_builds.append(
                [settings, options, env_vars, build_requires])
            new_options = copy.copy(options)
            new_options["arduino-sdk:host_os"] = "linux32"
            filtered_builds.append(
                [settings, new_options, env_vars, build_requires])
        builder.builds = filtered_builds

    builder.run()
