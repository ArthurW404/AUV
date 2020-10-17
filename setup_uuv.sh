#!/bin/bash 
# ./setup_uuv file world_name

if ! test $# -eq 2
then
  echo "Usage: $0 <model_files> <world_name>"
  exit 1
fi

catkin_src=~/catkin_ws/src
model_files="$1"

if echo $model_files | egrep -v '^/' 
then
    model_files="`pwd`/$model_files"
fi

new_world="$2"
echo $new_world
# 5. Create mew catkin package
mkdir -p $catkin_src
cd $catkin_src
catkin_create_pkg $new_world

cd $new_world
mkdir models worlds launch

# 6. setup directories for a model called world
cd models
mkdir test_model
cd test_model
mkdir -p meshes materials/textures

# 7. place .dae files into meshes 
cp -r $model_files/*.dae meshes/
# place textures into materials textures
cp -r $model_files/*.png materials/textures/

# 8.
cat > model.sdf << EOF
<?xml version="1.0" ?>  
<sdf version="1.5">  
<model name="test_model">  
<static>true</static>  
<link name="test_model_link">  

<visual name="test_model">  
<pose>0 0 0 0 0 0</pose>  
<geometry>  
<mesh><uri>model://test_model/meshes/test_model.dae</uri> 
<scale>1 1 1</scale></mesh>  
</geometry>  
</visual>  

<collision name="test_model_collision">  
<pose>0 0 0 0 0 0</pose>  
<geometry>  
<mesh><uri>model://test_model/meshes/test_model.dae</uri>  
<scale>1 1 1</scale></mesh>  
</geometry>  
</collision>  

</link>  
</model>  
</sdf> 
EOF

cat > model.config << EOF

<?xml version="1.0"?>  
<model>  
<name>Test Model</name>  
<version>1.0</version>  
<sdf version="1.5">model.sdf</sdf>  

<author>  
<name>Your Name</name>  
<email>your.name@example.com</email>  
</author>  

<description>  
A Gazebo model  
</description>  

</model> 

EOF

# 9.

# 10 return to base directory
cd $catkin_src
cd $new_world

cat >> CMakeLists.txt << EOF
install(DIRECTORY launch worlds models 
        DESTINATION \${CATKIN_PACKAGE_SHARE_DESTINATION} 
        PATTERN "*~" EXCLUDE) 
EOF

cat > package.xml << EOF
<?xml version="1.0"?> 
<package format="2"> 
  <name>${new_world}</name> 
  <version>0.1.0</version> 
  <description>A test world</description> 

  <maintainer email="your.name@example.com">Your Name</maintainer> 

  <author email="your.name@example.com">Your Name</author> 

  <license>TODO</license> 

  <buildtool_depend>catkin</buildtool_depend> 

  <exec_depend>gazebo_ros</exec_depend> 

  <export> 
    <gazebo_ros gazebo_media_path="\${prefix}" 
                gazebo_model_path="\${prefix}/models"/> 
  </export> 
</package> 
EOF

# 11.
cd ~/catkin_ws
catkin_make

#12.
source devel/setup.bash

roscd ${new_world} 

cd worlds 

cat > ${new_world}.world << EOF
<?xml version="1.0" ?> 
<sdf version="1.5"> 
  <world name="${new_world}"> 
    <physics name="default_physics" default="true" type="ode"> 
      <max_step_size>0.002</max_step_size> 
      <real_time_factor>1</real_time_factor> 
      <real_time_update_rate>500</real_time_update_rate> 
      <ode> 
        <solver> 
          <type>quick</type> 
          <iters>50</iters> 
          <sor>0.5</sor> 
        </solver> 
      </ode> 
    </physics> 
    <scene> 
      <ambient>0.01 0.01 0.01 1.0</ambient> 
      <sky> 
        <clouds> 
          <speed>12</speed> 
        </clouds> 
      </sky> 
      <shadows>1</shadows> 
    </scene> 

    <!-- Global light source --> 
    <include> 
      <uri>model://sun</uri> 
    </include> 

    <include> 
      <uri>model://test_model</uri> 
      <pose>0 0 0 0 0 0</pose> 
    </include> 

    <plugin name="underwater_current_plugin" filename="libuuv_underwater_current_ros_plugin.so"> 
      <namespace>hydrodynamics</namespace> 
      <constant_current> 
        <topic>current_velocity</topic> 
        <velocity> 
          <mean>0</mean> 
          <min>0</min> 
          <max>5</max> 
          <mu>0.0</mu> 
          <noiseAmp>0.0</noiseAmp> 
        </velocity> 
        <horizontal_angle> 
          <mean>0</mean> 
          <min>-3.141592653589793238</min> 
          <max>3.141592653589793238</max> 
          <mu>0.0</mu> 
          <noiseAmp>0.0</noiseAmp> 
        </horizontal_angle> 

        <vertical_angle> 
          <mean>0</mean> 
          <min>-3.141592653589793238</min> 
          <max>3.141592653589793238</max> 
          <mu>0.0</mu> 
          <noiseAmp>0.0</noiseAmp> 
        </vertical_angle> 
      </constant_current> 
    </plugin> 

    <plugin name="sc_interface" filename="libuuv_sc_ros_interface_plugin.so"/> 

  </world> 
</sdf> 
EOF

# 13. 

cd ../launch

cat > ${new_world}.launch  << EOF
<launch> 
    <arg name="gui" default="true"/> 
    <arg name="paused" default="false"/> 
    <include file="\$(find gazebo_ros)/launch/empty_world.launch"> 
        <arg name="world_name" value="/home/${USER}/catkin_ws/src/${new_world}/worlds/${new_world}.world"/> 
        <arg name="paused" value="\$(arg paused)"/> 
        <arg name="use_sim_time" value="true"/> 
        <arg name="gui" value="\$(arg gui)"/> 
        <arg name="headless" value="false"/> 
        <arg name="debug" value="false"/> 
        <arg name="verbose" value="true"/> 
    </include> 
</launch> 
EOF

# 14.
roslaunch ${new_world} ${new_world}.launch