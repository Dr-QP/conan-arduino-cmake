![CI](https://github.com/Dr-QP/conan-arduino-cmake/workflows/CI/badge.svg)

# conan-arduino-cmake

Arduino-CMake toolchain bundled as Conan package

* Toolchain includes slight modifications and fixes to work with latest IDE versions
* For Arduino IDE use `arduino-sdk` package https://bintray.com/anton-matosov/general/arduino-sdk%3Aconan


# Usage

Add remote `https://api.bintray.com/conan/anton-matosov/general`
Add these lines to your profile

```
[build_requires]
arduino-sdk/1.8.11@conan/testing
arduino-cmake/1.0.0@conan/testing
```