from conans import ConanFile, CMake


class XtlConan(ConanFile):
    name = "xtl"
    version = "0.6.4"
    license = "BSD 3-Clause"
    homepage = "https://github.com/QuantStack/xtl/"
    url = "https://github.com/torshind/conan-xtl/"
    description = "The x template library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        self.run("git clone --branch "
                 + self.version
                 + " https://github.com/QuantStack/xtl.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xtl")
        cmake.install()

    def package_info(self):
        self.info.header_only()
