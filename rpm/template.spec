%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-twist-controller
Version:        0.1.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS twist_controller package

License:        Apache-2.0
URL:            http://wiki.ros.org/twist_controller
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-cartesian-interface
Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-realtime-tools
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-cartesian-interface
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-realtime-tools
BuildRequires:  ros-noetic-roscpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A ros_control controller accepting Cartesian twist messages in order to move a
robot manipulator. It uses a Cartesian interface to the robot, so that the robot
hardware takes care about doing the inverse kinematics. This could be used e.g.
for visual servoing applications.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Aug 05 2021 Stefan Scherzinger <scherzin@fzi.de> - 0.1.4-1
- Autogenerated by Bloom

* Wed Jun 23 2021 Stefan Scherzinger <scherzin@fzi.de> - 0.1.3-1
- Autogenerated by Bloom

* Tue Jun 15 2021 Stefan Scherzinger <scherzin@fzi.de> - 0.1.2-2
- Autogenerated by Bloom

* Tue Jun 15 2021 Stefan Scherzinger <scherzin@fzi.de> - 0.1.2-1
- Autogenerated by Bloom

