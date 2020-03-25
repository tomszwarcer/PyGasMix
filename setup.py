import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import Cython
import numpy
from io import open
def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in (".pyx", ".py"):
                if extension.language == "c++":
                    ext = ".cpp"
                else:
                    ext = ".c"
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions
extensions = [
    Extension("*",["PyGasMix/*.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/']),
    Extension("*",["PyGasMix/Gases/*.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/']),
]
setup(
    setup_requires=[
        'cython>=0.2',
    ],
    zip_safe=False,
    name='PyGasMix',  # Required
    packages=['PyGasMix','PyGasMix/Gases'],

    version='1.0.0',  # Required
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    install_requires=['numpy==1.16.1','cython'],  # Optional
    package_data={  # Optional
        'src': ['./PyGasMix/*.pxd'],
        'src/Gases':['./PyGasMix/Gases/gases.npy','./PyGasMix/Gases/*.pxd','./PyGasMix/*.pxd']
    },
    ext_modules = extensions,
    cmdclass={'build_ext': Cython.Build.build_ext},
)