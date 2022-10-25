#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-rpm_py_installer
Version  : 1.2.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/30/b8/ddb7509bdad54417fc2d2139aa925c1fd2ac5def4bd9093c0878c17f5d3f/rpm-py-installer-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/b8/ddb7509bdad54417fc2d2139aa925c1fd2ac5def4bd9093c0878c17f5d3f/rpm-py-installer-1.2.0.tar.gz
Summary  : RPM Python binding Installer
Group    : Development/Tools
License  : MIT
Requires: pypi-rpm_py_installer-bin = %{version}-%{release}
Requires: pypi-rpm_py_installer-license = %{version}-%{release}
Requires: pypi-rpm_py_installer-python = %{version}-%{release}
Requires: pypi-rpm_py_installer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# RPM Python binding Installer
[![PyPI](https://img.shields.io/pypi/v/rpm-py-installer.svg)](https://pypi.python.org/pypi/rpm-py-installer)
[![GitHub Actions Build Status](https://github.com/junaruga/rpm-py-installer/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/junaruga/rpm-py-installer/actions/workflows/build-and-test.yml)

%package bin
Summary: bin components for the pypi-rpm_py_installer package.
Group: Binaries
Requires: pypi-rpm_py_installer-license = %{version}-%{release}

%description bin
bin components for the pypi-rpm_py_installer package.


%package license
Summary: license components for the pypi-rpm_py_installer package.
Group: Default

%description license
license components for the pypi-rpm_py_installer package.


%package python
Summary: python components for the pypi-rpm_py_installer package.
Group: Default
Requires: pypi-rpm_py_installer-python3 = %{version}-%{release}

%description python
python components for the pypi-rpm_py_installer package.


%package python3
Summary: python3 components for the pypi-rpm_py_installer package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pypi-rpm_py_installer package.


%prep
%setup -q -n rpm-py-installer-1.2.0
cd %{_builddir}/rpm-py-installer-1.2.0
pushd ..
cp -a rpm-py-installer-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659393264
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-rpm_py_installer
cp %{_builddir}/rpm-py-installer-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-rpm_py_installer/56f55d6d6651181134722362475574c0a0963dd1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/install.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-rpm_py_installer/56f55d6d6651181134722362475574c0a0963dd1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
