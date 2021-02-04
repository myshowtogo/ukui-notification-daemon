%define debug_package %{nil}

Name:           ukui-notification-daemon
Version:        1.0.1
Release:        2
Summary:        daemon to display passive popup notifications
License:        GPL-3+
URL:            https://github.com/ukui/ukui-notification-daemon
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  dconf-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  libX11-devel

Requires:  gsettings-qt
Requires:  libX11
Requires:  dconf

%description
daemon to display passive popup notifications
ukui-notification-daemon displays passive popup notifications, as per
the Desktop Notifications Specification.

The Desktop Notifications Specification provides a standard way of
doing passive popup notifications on the Linux desktop. These are
designed to notify the user of something without interrupting their
work with a dialog box that they must close.  Passive popups can
automatically disappear after a short period of time, as per the
Desktop Notifications spec.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

%files
%doc debian/changelog
%license  debian/copyright
%{_prefix}/lib/ukui-notification-daemon/ukui-notification-daemon
%{_datadir}/dbus-1/services/org.ukui.freedesktop.Notification.service
%{_datadir}/glib-2.0/schemas/org.ukui.notification.gschema.xml

%changelog
* Thu Feb 4 2021 lvhan <lvhan@kylinos.cn> - 1.0.1-2
- update to upstream version 1.0.1-1

* Wed Nov 11 2020 douyan <douyan@kylinos.cn> - 1.0.1-1
- update to upstream version 1.0.0-1+1031