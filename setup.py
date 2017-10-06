import os
import multiprocessing
import re
import sys
import subprocess
import importlib
import datetime

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.test import test


def ensure_dir_exists(path):
    """Checks whether the directory exists and creates it if not."""
    assert path is not None
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise IOError("Cannot create directory: " + path)
    except BaseException:
        raise IOError("Path " + path + " seems not valid")


if sys.version_info[0] == 2:
    sys.exit('Sorry, Python 2.x is not supported')


def check_carl_compatible(carl_dir, carl_major, carl_minor, carl_patch):
    """
    Check if the given carl lib is compatible with this pycarl version.
    :param carl_dir: Path of carl.
    :param carl_major: Major version of carl.
    :param carl_minor: Minor version of carl.
    :param carl_patch: Patch version of carl.
    """
    if carl_major < 17 or (carl_major == 17 and carl_minor < 8) or (
                        carl_major == 17 and carl_minor == 8 and carl_patch < 0):
        sys.exit(
            'Sorry, carl version {}.{}.{} from \'{}\' is not supported anymore!'.format(carl_major, carl_minor,
                                                                                        carl_patch, carl_dir))


def parse_carl_version(version_string):
    """
    Parses the version of carl.

    :param version_string: String containing version information.
    :return: Triple (major, minor, patch)
    """
    elems = version_string.split(".")
    if len(elems) == 2:
        elems.append(0)
    if len(elems) != 3:
        sys.exit('Carl version string is ill-formed: "{}"'.format(version_string))
    patch = elems[2].split('-')[0]
    return int(elems[0]), int(elems[1]), int(patch)


def obtain_version():
    """
    Obtains the version as specified in pycarl.

    :return:
    """
    verstr = "unknown"
    try:
        verstrline = open('lib/pycarl/_version.py', "rt").read()
    except EnvironmentError:
        pass  # Okay, there is no version file.
    else:
        VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
        mo = re.search(VSRE, verstrline, re.M)
        if mo:
            verstr = mo.group(1)
        else:
            raise RuntimeError("unable to find version in pycarl/_version.py")
    return verstr


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir='', subdir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)
        self.subdir = subdir


class CMakeBuild(build_ext):
    user_options = build_ext.user_options + [
        ('carl-dir=', None, 'Path to carl root (binary) location'),
        ('jobs=', 'j', 'Number of jobs to use for compiling'),
        ('debug', None, 'Build in Debug mode'),
    ]

    def _extdir(self, extname):
        return os.path.abspath(os.path.dirname(self.get_ext_fullpath(extname)))

    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        # Build cmake version info

        build_temp_version = self.build_temp + "-version"
        if not os.path.exists(build_temp_version):
            os.makedirs(build_temp_version)

        cmake_args = []
        if self.carl_dir:
            cmake_args = ['-Dcarl_DIR=' + self.carl_dir]
        output = subprocess.check_output(['cmake', os.path.abspath("cmake")] + cmake_args, cwd=build_temp_version)
        if sys.version_info[1] >= 5:
            # Method for Python >= 3.5
            spec = importlib.util.spec_from_file_location("genconfig",
                                                          os.path.join(build_temp_version, 'generated/config.py'))
            self.conf = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.conf)
        else:
            # Deprecated method for Python <= 3.4
            from importlib.machinery import SourceFileLoader
            self.conf = SourceFileLoader("genconfig",
                                         os.path.join(build_temp_version, "generated/config.py")).load_module()

        # check version
        major, minor, patch = parse_carl_version(self.conf.CARL_VERSION)
        check_carl_compatible(self.conf.CARL_DIR, major, minor, patch)

        print("Pycarl - Using carl {} from {}".format(self.conf.CARL_VERSION, self.conf.CARL_DIR))
        if self.conf.CARL_PARSER:
            print("Pycarl - Carl parser extension found and included.")
        else:
            print("Pycarl - Warning: No parser support!")
        if self.conf.CARL_WITH_CLN:
            print("Pycarl - Support for CLN found and included.")
        else:
            print("Pycarl - Warning: No support for CLN!")

        for ext in self.extensions:
            ensure_dir_exists(os.path.join(self._extdir(ext.name), ext.subdir))
            if "core" in ext.name:
                with open(os.path.join(self._extdir(ext.name), ext.subdir, "_config.py"), "w") as f:
                    f.write("# Generated from setup.py at {}\n".format(datetime.datetime.now()))
                    f.write('CARL_VERSION = "{}.{}.{}"\n'.format(major, minor, patch))
                    f.write("CARL_PARSER = {}\n".format(self.conf.CARL_PARSER))
                    f.write("CARL_WITH_CLN = {}\n".format(self.conf.CARL_WITH_CLN))
            if "cln" in ext.name:
                with open(os.path.join(self._extdir(ext.name), ext.subdir, "_config.py"), "w") as f:
                    f.write("# Generated from setup.py at {}\n".format(datetime.datetime.now()))
                    f.write("CARL_WITH_CLN = {}\n".format(self.conf.CARL_WITH_CLN))
                if not self.conf.CARL_WITH_CLN:
                    print("Pycarl - CLN bindings skipped")
                    continue
            if "parse" in ext.name:
                with open(os.path.join(self._extdir(ext.name), ext.subdir, "_config.py"), "w") as f:
                    f.write("# Generated from setup.py at {}\n".format(datetime.datetime.now()))
                    f.write("CARL_PARSER = {}\n".format(self.conf.CARL_PARSER))
                if not self.conf.CARL_PARSER:
                    print("Pycarl - Parser bindings skipped")
                    continue
            self.build_extension(ext)

    def initialize_options(self):
        build_ext.initialize_options(self)
        self.carl_dir = None
        self.debug = False
        try:
            self.jobs = multiprocessing.cpu_count() if multiprocessing.cpu_count() is not None else 1
        except NotImplementedError:
            self.jobs = 1

    def finalize_options(self):
        if self.carl_dir:
            print('Pycarl - The custom carl directory', self.carl_dir)
        build_ext.finalize_options(self)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + os.path.join(extdir, ext.subdir),
                      '-DPYTHON_EXECUTABLE=' + sys.executable]

        build_type = 'Debug' if self.debug else 'Release'
        build_args = ['--config', build_type]
        build_args += ['--', '-j{}'.format(self.jobs)]
        cmake_args += ['-DCMAKE_BUILD_TYPE=' + build_type]
        if self.carl_dir:
            cmake_args += ['-Dcarl_DIR=' + self.carl_dir]

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        print("Pycarl - CMake args={}".format(cmake_args))
        # Call cmake
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.', '--target', ext.name] + build_args, cwd=self.build_temp)


class PyTest(test):
    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(['tests'])
        sys.exit(errno)


setup(
    name='pycarl',
    version=obtain_version(),
    author="H. Bruintjes",
    author_email="h.bruintjes@cs.rwth-aachen.de",
    maintainer="S. Junges",
    maintainer_email="sebastian.junges@cs.rwth-aachen.de",
    url="http://moves.rwth-aachen.de",
    description="pycarl - Python Bindings for CArL",
    packages=['pycarl',
              'pycarl.cln',
              'pycarl.gmp',
              'pycarl.formula',
              'pycarl.cln.formula',
              'pycarl.gmp.formula',
              'pycarl.parse',
              'pycarl.gmp.parse',
              'pycarl.cln.parse'],
    package_dir={'': 'lib'},
    long_description='',
    ext_package='pycarl',
    ext_modules=[CMakeExtension('core', subdir=''),
                 CMakeExtension('cln', subdir='cln'),
                 CMakeExtension('gmp', subdir='gmp'),
                 CMakeExtension('formula', subdir='formula'),
                 CMakeExtension('formula-cln', subdir='cln/formula'),
                 CMakeExtension('formula-gmp', subdir='gmp/formula'),
                 CMakeExtension('parse', subdir='parse'),
                 CMakeExtension('parse-gmp', subdir='gmp/parse'),
                 CMakeExtension('parse-cln', subdir='cln/parse')],

    cmdclass={'build_ext': CMakeBuild, 'test': PyTest},
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
