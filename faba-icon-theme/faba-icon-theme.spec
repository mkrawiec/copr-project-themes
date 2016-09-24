# Spec file for package faba-icon-theme
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

%define debug_package %{nil}

Name: faba-icon-theme
Version: 4.1.2
Release: 1%{dist}

Summary: Faba Icon theme
Group: System/GUI/Other
License: LGPL-3.0+ or CC-BY-SA-4.0
Group: System/GUI/GNOME
Url: https://snwh.org/moka
Source0: %{name}-%{version}.tar.gz
Requires: hicolor-icon-theme, gnome-icon-theme
BuildArch: noarch

%description
Faba is a sexy and modern icon theme with Tango influences.

%prep
%setup -q

# Delete dead icon symlinks
# find -L . -type l -delete

%build

%install
install -dpm 0755 %{buildroot}/%{_datadir}/icons/
cp -a Faba/ %{buildroot}/%{_datadir}/icons/

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE
%{_datadir}/icons/Faba/
