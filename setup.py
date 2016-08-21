from distutils.core import setup, Extension

module1 = Extension('great_module',
                    sources = ['great_module.c'])

setup (name = 'ABC',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])