from distutils.core import setup
try:
    from setuptools import find_packages
except ImportError:
    print ("Please install Distutils and setuptools"
           " before installing this package")
    raise

setup(
    name='relay.mesos',
    version='0.0.1',
    description=(
        'A plugin for Relay that lets you run Relay on Mesos to'
        ' auto-scale the number of concurrently running instances'
        ' of a bash command to minimize the difference between a'
        ' metric and a target timeseries.'
        ' Generally good for auto-scaling workers.  Similar to Marathon,'
        ' but designed for applications that fail often or need to be'
        " auto-scaled using Relay's algorithm"
    ),
    long_description="Check the project homepage for details",
    keywords=[
        'mesos', 'marathon', 'relay', 'relay.runner', 'framework',
        'pid', 'pid controller', 'thermostat', 'tuning',
        'oscilloscope', 'auto-scale'],

    author='Alex Gaudio',
    author_email='adgaudio@gmail.com',
    url='http://github.com/sailthru/relay.mesos',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'relay.runner', 'mesos.cli', 'mesos.interface', 'pyzmq'],

    extras_require={
        'mesos': ['mesos.native'],
    },
    tests_require=['nose'],
    test_suite="nose.main",

    entry_points = {
        'console_scripts': [
            'relay.mesos = relay_mesos.__main__:go',
        ],
        'setuptools.installation': [
            'eggsecutable = relay_mesos.__main__:go',
        ],
    },
    zip_safe=False
)
