# CHallENge-WritingRobot
# HKPC 2022 Inno-Canival
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome#readme)


## Prerequisites
Build and test on Ubuntu 20.04.

## Installation

Please install:
[ros-Noetic Desktop-Full Install](http://wiki.ros.org/noetic/Installation/Ubuntu)
[moveit! (Moveit! 1 Noetic)](https://ros-planning.github.io/moveit_tutorials/) 
[franka_ros (franka_ros)](https://frankaemika.github.io/docs/installation_linux.html) 
[libfranka (libfranka)](https://frankaemika.github.io/docs/installation_linux.html) 
in advance.  


## Building

Building workspace requires the following tools:

- Git (obviously)
- ROS Noetic (Desktop-Full Install)
- Moveit! (Moveit! 1 for Noetic)
- franka_ros
- libfranka

Get the source code:

```shell
git clone git@github.com:SheldanChen/CHallENge-WritingRobot.git
```

Download chinese traditional dataset
```shell
https://hkpc-my.sharepoint.com/:f:/g/personal/sheldanchen_hkpc_org/EidJW0VXRvVOkX4ZaPxlU-sBEF4qeUrajWKhBR6doo3hTQ?e=Ut1pOz
```
Download chinese simplified dataset
```shell
https://hkpc-my.sharepoint.com/:f:/g/personal/sheldanchen_hkpc_org/EkmKRlLvOzVKqGi1jFAeMsUBEt-5rDTCv1ZIFvnkp0wtxw?e=7w3O8n
```
and put these two dataset folders under the root folder.


## Launch 
cd to workspace
```shell
cd Path/to/ROS
```
then source:
```shell
source ./devel/setup.bash
```
Launch moveit! :
```shell
roslaunch panda_moveit_config franka_control.launch robot_ip:= @ur_franka_address load_gripper:=true controller:=position
```

Open in another terminal for launching the GUI program:
cd to the git root folder then
```shell
cd WritingRobot
```
```shell
python gui.py
```


## Launch Simplified (Optional)
To launch the control program:
```shell
./launch1.txt
```
and then open another terminal:
```shell
./launch2.txt
```




<!-- CONTACT -->
### Contact

Sheldan Chen - email@hkpc.org

Project Link: [https://github.com/SheldanChen/CHallENge-WritingRobot.git](https://github.com/SheldanChen/CHallENge-WritingRobot.git)

<p align="right">(<a href="#top">back to top</a>)</p>

