
# WARNING: SETUP.PY MODIFIED FOR USE WITH CATKIN BUILD
# DO NOT RUN PYTHON SETUP.PY INSTALL ON THIS FILE

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

def readme():
    with open('README.md') as f:
        return f.read()


setup_args = generate_distutils_setup(
    name='UBX_ROS_DRIVER',
    version='0.1.0',
    description='A lightweight python library for translating UBX packets',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Communications'
    ],
    url='http://github.com/gchustz/UBX_ROS_DRIVER',
    author='George Chustz',
    author_email='gchustz@tamu.edu',
    license='GNU GPL v3',
    packages=[ 'UBX_ROS_DRIVER'],
    package_dir={'' : 'src'},
    test_suite='nose.collector',
    tests_require=['nose'],
    )

setup(**setup_args)