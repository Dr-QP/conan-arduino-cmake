from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="anton-matosov", channel="stable")
    builder.add_common_builds()
    builder.run()
