%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-cartesian-interface
Version:        0.1.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cartesian_interface package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosunit
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Defines a hardware interface to send Cartesian commands to a robot hardware and
read Cartesian states.

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
* Wed Jun 23 2021 Felix Exner <mauch@fzi.de> - 0.1.3-1
- Autogenerated by Bloom

* Tue Jun 15 2021 Felix Exner <mauch@fzi.de> - 0.1.2-2
- Autogenerated by Bloom

* Tue Jun 15 2021 Felix Exner <mauch@fzi.de> - 0.1.2-1
- Autogenerated by Bloom

