Summary:	Kamera ioslave
Name:		kamera
Version:	21.12.2
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	pkgconfig(libgphoto2)

%description
Kamera ioslave.

%files -f kcmkamera.lang
%doc COPYING  COPYING.DOC
%{_qt5_plugindir}/*.so
%{_qt5_plugindir}/kf5/kio/kio_kamera.so
%{_datadir}/kservices5/kamera.desktop
%{_datadir}/solid/actions/solid_camera.desktop
%{_datadir}/metainfo/org.kde.kamera.metainfo.xml

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcmkamera --all-name --with-html
