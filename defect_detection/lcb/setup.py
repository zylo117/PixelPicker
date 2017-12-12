from distutils.core import setup,Extension
from Cython.Build import cythonize 
import numpy
setup(ext_modules = cythonize(Extension(
    'lcb_function_cython',
    sources=['lcb_function_cython.pyx'],
    language='c++',
    include_dirs=[numpy.get_include()],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]
)))