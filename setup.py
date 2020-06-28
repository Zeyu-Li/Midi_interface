from setuptools import setup

setup(
    name='Midi',
    version='0.01',
    description='A interface to MIDIUtil',
    author='Zeyu Li',
    packages=['Midi'],              #same as name
    install_requires=['MIDIUtil'],  #external packages as dependencies
)