import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import Cython
import numpy
from io import open


extensions = [
    Extension("*",["src/*.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/src/']),
    Extension("*",["src/Gases/*.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/src/']),
]
#setup(ext_modules=cythonize(extensions))
extensions = cythonize(extensions)

setup(
    setup_requires=[
        'cython>=0.2x',
    ],

    name='PyGasMix',  # Required
    packages=['src'],

    version='1.0.0',  # Required
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    install_requires=['numpy==1.16.1','cython'],  # Optional
    package_data={  # Optional
        'src': ['/src/Gases/gases.npy','/src/*.pxd','/src/Gases/*.pxd'],
    },
    extensions=extensions,
    cmdclass={'build_ext': Cython.Build.build_ext},
)