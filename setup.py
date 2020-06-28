from setuptools import setup, find_packages

setup(
    name='Midi_interface',
    version='0.1',
    description='A interface to MIDIUtil',
    author='Zeyu Li',
    packages=find_packages(where="src"),
    package_dir = {'': 'src'},
    url='https://github.com/Zeyu-Li/Midi_interface',
    license='MIT',
    install_requires=['MIDIUtil'],  #external packages as dependencies
    keywords = 'Music MIDI',
    zip=False
)