# Umic_Team_2_Project

Im My_gazebo files, open terminal

To launch Gazebo,
roslaunch mybot_gazebo umic_world.launch

To launch script,
rosrun mybot_gazebo my_initals.py

Run a node to view the camera data.

rosrun image_view image_view image:=/mybot/camera1/image_raw

Use rostopic to find the topics for sonar AND ir

lane detection : https://colab.research.google.com/drive/1lBtdTxG8yV2cEVfABYT7wbiNkgvwloQc?authuser=2
