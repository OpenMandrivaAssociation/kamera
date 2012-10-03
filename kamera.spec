Name:		kamera
Summary:	Kamera ioslave
Version: 4.9.2
Release: 1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libgphoto2)

%description
Kamera ioslave.

%files
%doc %{_kde_docdir}/HTML/en/kcontrol/kamera
%doc COPYING  COPYING.DOC
%{_kde_libdir}/kde4/kcm_kamera.so
%{_kde_libdir}/kde4/kio_kamera.so
%{_kde_services}/camera.protocol
%{_kde_services}/kamera.desktop
%{_kde_appsdir}/solid/actions/solid_camera.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

