from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy

extensions = [
    Extension("PyGasMix.Gases.GasUtil",["PyGasMix/Gases/GasUtil.pyx","PyGasMix/Gases/GasUtil.pxd"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gasmix",["PyGasMix/Gasmix.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.ARGON",["PyGasMix/Gases/ARGON.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.CF4",["PyGasMix/Gases/CF4.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.CH4",["PyGasMix/Gases/CH4.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.CO2",["PyGasMix/Gases/CO2.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.DEUTERIUM",["PyGasMix/Gases/DEUTERIUM.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.DME",["PyGasMix/Gases/DME.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.ETHANE",["PyGasMix/Gases/ETHANE.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.H2O",["PyGasMix/Gases/H2O.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.HELIUM3",["PyGasMix/Gases/HELIUM3.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.HELIUM4",["PyGasMix/Gases/HELIUM4.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.HYDROGEN",["PyGasMix/Gases/HYDROGEN.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.ISOBUTANE",["PyGasMix/Gases/ISOBUTANE.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.KRYPTON",["PyGasMix/Gases/KRYPTON.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.NEON",["PyGasMix/Gases/NEON.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.NITROGEN",["PyGasMix/Gases/NITROGEN.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.OXYGEN",["PyGasMix/Gases/OXYGEN.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.PROPANE",["PyGasMix/Gases/PROPANE.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.XENON",["PyGasMix/Gases/XENON.pyx"],include_dirs=[numpy.get_include()]),
    Extension("PyGasMix.Gases.XENONMERT",["PyGasMix/Gases/XENONMERT.pyx"],include_dirs=[numpy.get_include()])

]
setup(
    ext_modules = extensions,
    cmdclass={'build_ext': build_ext},
)
