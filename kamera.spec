Summary:	Kamera ioslave
Name:		kamera
Version:	16.04.1
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%files
%doc %{_docdir}/HTML/en/kcontrol/kamera
%doc COPYING  COPYING.DOC
%{_qt5_plugindir}/*.so
%{_datadir}/kservices5/camera.protocol
%{_datadir}/kservices5/kamera.desktop
%{_datadir}/solid/actions/solid_camera.desktop

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
