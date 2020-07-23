from conans import ConanFile, CMake, tools


class gtsam(ConanFile):
    name = "gtsam"
    version = "4.0.2"
    license = "BSD"
    url = "https://github.com/borglab/gtsam.git"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake_paths"
    scm = {
        "type": "git",
        "url": "auto",
        "subfolder": "gtsam",
        "revision": "auto"
    }

    # def source(self):
    #     self.run("git clone https://github.com/borglab/gtsam.git")

    def build(self):
        # cmake = CMake(self)
        # cmake.configure(source_folder="hello")
        # cmake.build()
        cmake = CMake(self)
        cmake.definitions['CMAKE_VERBOSE_MAKEFILE'] = True
        cmake.definitions['CMAKE_TOOLCHAIN_FILE'] = self.build_folder + '/conan_paths.cmake'
        cmake.configure(source_folder="gtsam")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    # def package(self):
    #     self.copy("*.h", dst="include", src="hello")
    #     self.copy("*hello.lib", dst="lib", keep_path=False)
    #     self.copy("*.dll", dst="bin", keep_path=False)
    #     self.copy("*.so", dst="lib", keep_path=False)
    #     self.copy("*.dylib", dst="lib", keep_path=False)
    #     self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = []