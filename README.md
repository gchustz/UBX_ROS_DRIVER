# UBX_ROS_DRIVER (v0.1.0)
A ros implementation of the ubxtranslator python package from [Daly Mople](https://github.com/dalymople/ubxtranslator).

# Install
Navigate your desired workspace's src directory.

Run:
```
git clone https://github.com/gchustz/UBX_ROS_DRIVER.git
cd ..
catkin_make
source devel/setup.bash
```

Dependencies and the udev serial rules can be added by running
```
cd UBX_ROS_DRIVER/scripts/
sudo ./setup.sh
```

# Dependencies
* [Python3](https://www.python.org/downloads/)
* [PySerial](https://pypi.org/project/pyserial/)
* [ubxtranslator](https://github.com/dalymople/ubxtranslator)

# Credit
This work is adapted from:
* https://github.com/dalymople/ubxtranslator
* https://github.com/unmannedlab/ubxtranslator

# License
GPL v3.0
