%global theme1 Arc
%global theme2 Arc-Darker
%global theme3 Arc-Dark

Name:		arc-theme
Version: 20160923
Release:	1%{?dist}
Summary:	A flat theme for GTK based DEs

License:	GPLv3
URL:		https://github.com/horst3180/%{name}
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gtk3-devel
BuildRequires:	autoconf
BuildRequires:	automake

Requires:	gnome-themes-standard

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell 
which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, 
Budgie, Pantheon, XFCE, Mate, etc.

%package cinnamon
Summary:	Arc theme for cinnamon DE
Requires:	%{name}

%description cinnamon
Arc theme elements for cinnamon DE

%package gnome-shell
Summary:	Arc theme for GNOME DE
Requires:	%{name}

%description gnome-shell
Arc theme elements for GNOME shell

%package gtk2
Summary:	Arc theme for GTK-2.x
Requires:	gtk-murrine-engine
Requires:	%{name}

%description gtk2
Arc theme for GTK-2.x environments

%package gtk3
Summary:	Arc theme for GTK-3.x
Requires:	%{name}

%description gtk3
Arc theme for GTK-3.x environments

%package metacity
Summary:	Metacity arc themes
Requires:	%{name}

%description metacity
Arc theme for metacity

%package xfwm4
Summary:	Arc theme for xfwm4
Requires:	%{name}

%description xfwm4
Arc theme for xfce4 window manager

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -vif
%configure --disable-unity --with-gnome=3.20
%{make_build}

%install
%make_install

%files
%license COPYING
%doc AUTHORS HACKING.md README.md
%{_datadir}/themes/%{theme1}/index.theme
%{_datadir}/themes/%{theme2}/index.theme
%{_datadir}/themes/%{theme3}/index.theme

%files cinnamon
%{_datadir}/themes/%{theme1}/cinnamon
%{_datadir}/themes/%{theme3}/cinnamon

%files gnome-shell
%{_datadir}/themes/%{theme1}/gnome-shell
%{_datadir}/themes/%{theme3}/gnome-shell

%files gtk2
%{_datadir}/themes/%{theme1}/gtk-2.0
%{_datadir}/themes/%{theme2}/gtk-2.0
%{_datadir}/themes/%{theme3}/gtk-2.0

%files gtk3
%{_datadir}/themes/%{theme1}/gtk-3.0
%{_datadir}/themes/%{theme2}/gtk-3.0
%{_datadir}/themes/%{theme3}/gtk-3.0

%files metacity
%{_datadir}/themes/%{theme1}/metacity-1
%{_datadir}/themes/%{theme2}/metacity-1
%{_datadir}/themes/%{theme3}/metacity-1

%files xfwm4
%{_datadir}/themes/%{theme1}/xfwm4
%{_datadir}/themes/%{theme2}/xfwm4
%{_datadir}/themes/%{theme3}/xfwm4

%changelog
* Mon Aug 08 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20160606-2
- add --with-gnome configure flag

* Sat Aug 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20160606-1
- Update theme to master branch (fixes some issues)

* Wed Aug 3 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20160605-2
- Fix file installations

* Wed Aug 3 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 20160605-1
- Initial build
