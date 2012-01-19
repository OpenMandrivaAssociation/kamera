Name: kamera
Summary: Kamera ioslave
Version: 4.8.0
Release: 1
Epoch:   2
Group:   Graphical desktop/KDE
License: GPLv2 GFDL
URL:     http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: gphoto2-devel

%description
Kamera ioslave.

%files
%_kde_libdir/kde4/kcm_kamera.so
%_kde_libdir/kde4/kio_kamera.so
%_kde_services/camera.protocol
%_kde_services/kamera.desktop
%_kde_appsdir/solid/actions/solid_camera.desktop
%doc %_kde_docdir/HTML/en/kcontrol/kamera
%doc  COPYING  COPYING.DOC

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

