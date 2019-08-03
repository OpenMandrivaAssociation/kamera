Summary:	Kamera ioslave
Name:		kamera
Version:	19.07.90
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
%{_datadir}/kservices5/camera.protocol
%{_datadir}/kservices5/kamera.desktop
%{_datadir}/solid/actions/solid_camera.desktop
%doc %{_docdir}/HTML/en/kcontrol/kamera
%lang(ca) %{_docdir}/HTML/ca/kcontrol/kamera
%lang(cs) %{_docdir}/HTML/cs/kcontrol/kamera
%lang(de) %{_docdir}/HTML/de/kcontrol/kamera
%lang(es) %{_docdir}/HTML/es/kcontrol/kamera
%lang(et) %{_docdir}/HTML/et/kcontrol/kamera
%lang(fr) %{_docdir}/HTML/fr/kcontrol/kamera
%lang(gl) %{_docdir}/HTML/gl/kcontrol/kamera
%lang(it) %{_docdir}/HTML/it/kcontrol/kamera
%lang(nl) %{_docdir}/HTML/nl/kcontrol/kamera
%lang(pl) %{_docdir}/HTML/pl/kcontrol/kamera
%lang(pt) %{_docdir}/HTML/pt/kcontrol/kamera
%lang(pt_BR) %{_docdir}/HTML/pt_BR/kcontrol/kamera
%lang(ru) %{_docdir}/HTML/ru/kcontrol/kamera
%lang(sv) %{_docdir}/HTML/sv/kcontrol/kamera
%lang(uk) %{_docdir}/HTML/uk/kcontrol/kamera

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcmkamera --all-name --with-html
