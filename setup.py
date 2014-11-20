from distutils.core import setup
try:
    from setuptools import find_packages
except ImportError:
    print ("Please install Distutils and setuptools"
           " before installing this package")
    raise

setup(
    name='relay.marathon',
    version='0.0.1',
    description=(
        'Run an arbitrary bash command as a mesos framework.'
        ' Scale up number of concurrently running instances based on a metric.'
        ' Generally good for auto-scaling workers.  Similar to Marathon,'
        ' but designed for applications that fail often or need to be'
        " autoscaled using relay's algorithm"
    ),
    long_description="Check the project homepage for details",
    keywords=['mesos', 'marathon', 'relay', 'framework'],

    author='Alex Gaudio',
    author_email='adgaudio@gmail.com',
    url='http://github.com/sailthru/relay.marathon',

    packages=find_packages(),
    include_package_data=True,
    install_requires=['argparse_tools', 'colorlog'],

    extras_require={
        'webui': ['pyzmq'],
        'mesos': ['mesos.native', 'mesos.cli', 'mesos.interface'],
    },
    tests_require=['nose'],
    test_suite="nose.main",

    entry_points = {
        'console_scripts': [
            'relay = relay.__main__:go',
        ],
        'setuptools.installation': [
            'eggsecutable = relay.__main__:go',
        ],
    },
)
