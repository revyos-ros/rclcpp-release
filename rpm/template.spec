%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rclcpp
Version:        27.0.0
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS rclcpp package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-ament-index-cpp
Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-libstatistics-collector
Requires:       ros-rolling-rcl
Requires:       ros-rolling-rcl-interfaces
Requires:       ros-rolling-rcl-logging-interface
Requires:       ros-rolling-rcl-yaml-param-parser
Requires:       ros-rolling-rcpputils
Requires:       ros-rolling-rcutils
Requires:       ros-rolling-rmw
Requires:       ros-rolling-rosgraph-msgs
Requires:       ros-rolling-rosidl-dynamic-typesupport
Requires:       ros-rolling-rosidl-runtime-c
Requires:       ros-rolling-rosidl-runtime-cpp
Requires:       ros-rolling-rosidl-typesupport-c
Requires:       ros-rolling-rosidl-typesupport-cpp
Requires:       ros-rolling-statistics-msgs
Requires:       ros-rolling-tracetools
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ament-cmake-gen-version-h
BuildRequires:  ros-rolling-ament-cmake-ros
BuildRequires:  ros-rolling-ament-index-cpp
BuildRequires:  ros-rolling-builtin-interfaces
BuildRequires:  ros-rolling-libstatistics-collector
BuildRequires:  ros-rolling-rcl
BuildRequires:  ros-rolling-rcl-interfaces
BuildRequires:  ros-rolling-rcl-logging-interface
BuildRequires:  ros-rolling-rcl-yaml-param-parser
BuildRequires:  ros-rolling-rcpputils
BuildRequires:  ros-rolling-rcutils
BuildRequires:  ros-rolling-rmw
BuildRequires:  ros-rolling-rosgraph-msgs
BuildRequires:  ros-rolling-rosidl-dynamic-typesupport
BuildRequires:  ros-rolling-rosidl-runtime-c
BuildRequires:  ros-rolling-rosidl-runtime-cpp
BuildRequires:  ros-rolling-rosidl-typesupport-c
BuildRequires:  ros-rolling-rosidl-typesupport-cpp
BuildRequires:  ros-rolling-statistics-msgs
BuildRequires:  ros-rolling-tracetools
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-google-benchmark
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
BuildRequires:  ros-rolling-mimick-vendor
BuildRequires:  ros-rolling-performance-test-fixture
BuildRequires:  ros-rolling-rmw-implementation-cmake
BuildRequires:  ros-rolling-rosidl-default-generators
BuildRequires:  ros-rolling-test-msgs
%endif

%description
The ROS client library in C++.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Mar 28 2024 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 27.0.0-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Ivan Paunovic <ivanpauno@ekumenlabs.com> - 27.0.0-2
- Autogenerated by Bloom

