Name: meego-panel-networks
Summary: Connection management panel
Version: 1.2.15
Release: %mkrel 1
Group: Applications/Internet
License: GPL 2
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/builds/1.0.90/1.0.90.0.20100831.1/core/repos/source/%{name}-%{version}.tar.gz
Patch0: 0001-list-Fix-fallback-information-text-MBC-7544-MBC-5632.patch
Requires: mobile-broadband-provider-info
Requires: iso-codes
BuildRequires: libgtk+2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libGConf2-devel
BuildRequires: libnotify-devel
BuildRequires: mx-devel
BuildRequires: meego-panel-devel >= 0.49.0
BuildRequires: librest-devel >= 0.7
BuildRequires: mobile-broadband-provider-info
BuildRequires: iso-codes
BuildRequires: intltool
BuildRequires: gnome-common
Obsoletes: gconnman <= 0.1.13
Obsoletes: carrick <= 0.0.6

%description
A connection management panel for Mutter-Meego.

%prep
%setup -q -n %{name}-%{version}
# 0001-list-Fix-fallback-information-text-MBC-7544-MBC-5632.patch
%patch0 -p1

%build
autoreconf --install
%configure --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang meego-panel-networks

%post
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 

%postun
/bin/touch --no-create %{_datadir}/icons/hicolor || : 
%{_bindir}/gtk-update-icon-cache \
  --quiet %{_datadir}/icons/hicolor 2> /dev/null|| : 


%files -f meego-panel-networks.lang
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/xdg/autostart/carrick.desktop
%{_libexecdir}/carrick-connection-panel
%{_libexecdir}/carrick-3g-wizard
%{_datadir}/meego-panel-networks/icons/*
%{_datadir}/meego-panel-networks/theme/*
%{_datadir}/dbus-1/services/com.meego.UX.Shell.Panels.network.service
%{_datadir}/mutter-meego/panels/carrick.desktop
