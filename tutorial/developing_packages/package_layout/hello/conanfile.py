from conan import ConanFile
from conan.tools.cmake import cmake_layout


class HelloConan(ConanFile):
    name = "hello"
    version = "1.0"

    settings = "os", "compiler", "build_type", "arch"

    generators = "CMakeToolchain", "CMakeDeps"
    requires = "say/1.0"

    def layout(self):
        cmake_layout(self)
