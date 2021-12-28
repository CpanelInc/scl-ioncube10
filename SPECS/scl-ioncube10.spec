%define debug_package %{nil}

# Package namespaces
%global ns_name ea
%global ns_dir /opt/cpanel
%global _scl_prefix %ns_dir

%scl_package %scl

# This makes the ea-php<ver>-build macro stuff work
%scl_package_override

%global inifile 01-ioncube.ini

Name:    %{?scl_prefix}php-ioncube10
Vendor:  cPanel, Inc.
Summary: v10 Loader for ionCube-encoded PHP files
Version: 10.4.5
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4572 for more details
%define release_prefix 4
Release: %{release_prefix}%{?dist}.cpanel
License: Redistributable
Group:   Development/Languages
URL:     http://www.ioncube.com/loaders.php

# 1. See `perldoc find-latest-version` for info on the tarball.
# 2. The archive contains the license file, so no need to have it as a
#    separate source file.
Source: http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz

BuildRequires: scl-utils-build
BuildRequires: %{?scl_prefix}scldevel
BuildRequires: %{?scl_prefix}build
BuildRequires: %{?scl_prefix}php-devel
Requires:      %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:      %{?scl_prefix}php(api) = %{php_core_api}
Requires:      %{?scl_prefix}php-cli
Provides:      %{?scl_prefix}ioncube = 10
Conflicts:     %{?scl_prefix}ioncube >= 11, %{?scl_prefix}ioncube < 10
Conflicts:     %{?scl_prefix}php-ioncube
Conflicts:     %{?scl_prefix}php-ioncube5
Conflicts:     %{?scl_prefix}php-ioncube6

# Don't provide extensions as shared library resources
%{?filter_provides_in: %filter_provides_in %{php_extdir}/.*\.so$}
%{?filter_setup}

%description
The v10 ionCube Loader enables use of ionCube-encoded PHP files running
under PHP %{php_version}.

%prep
%setup -q -n ioncube

%build
# Nothing to do here, since it's a binary distribution.

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf %{buildroot}

# The module itself
install -d -m 755 $RPM_BUILD_ROOT%{php_extdir}
install -m 755 ioncube_loader_lin_%{php_version}.so $RPM_BUILD_ROOT%{php_extdir}

# The ini snippet
install -d -m 755 $RPM_BUILD_ROOT%{php_inidir}
cat > $RPM_BUILD_ROOT%{php_inidir}/%{inifile} <<EOF
; Enable v10 IonCube Loader extension module
zend_extension="%{php_extdir}/ioncube_loader_lin_%{php_version}.so"
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%config(noreplace) %{php_inidir}/%{inifile}
%{php_extdir}/ioncube_loader_lin_%{php_version}.so

%changelog
* Tue Dec 28 2021 Dan Muey <dan@cpanel.net> - 10.4.5-4
- ZC-9589: Update DISABLE_BUILD to match OBS

* Wed Dec 22 2021 Julian Brown <julian.brown@cpanel.net> - 10.4.5-3
- ZC-9608: Fix build dependency for Ubuntu 21

* Thu Dec 03 2020 Daniel Muey <dan@cpanel.net> - 10.4.5-2
- ZC-7975: Drop 32-bit tar ball

* Sun Nov 29 2020 Cory McIntire <cory@cpanel.net> - 10.4.5-1
- EA-9450: Update scl-ioncube10 from v10.4.4 to v10.4.5

* Mon Nov 09 2020 Tim Mullin <tim@cpanel.net> - 10.4.4-1
- EA-9356: Update scl-ioncube10 from v10.4.3 to v10.4.4

* Fri Sep 18 2020 Tim Mullin <tim@cpanel.net> - 10.4.3-1
- EA-9307: Update scl-ioncube10 from v10.4.1 to v10.4.3

* Mon Aug 03 2020 Tim Mullin <tim@cpanel.net> - 10.4.1-1
- EA-9206: Update from 10.4.0 to 10.4.1

* Tue Jun 30 2020 Tim Mullin <tim@cpanel.net> - 10.4.0-1
- EA-9085: Update from 10.3.9 to 10.4.0

* Tue Feb 18 2020 Tim Mullin <tim@cpanel.net> - 10.3.9-2
- EA-8865: Add php-cli as a dependency

* Wed Oct 16 2019 Tim Mullin <tim@cpanel.net> - 10.3.9-1
- EA-8703: Update from 10.3.8 to 10.3.9

* Tue Aug 27 2019 Tim Mullin <tim@cpanel.net> - 10.3.8-1
- EA-8631: Update from 10.3.2 to 10.3.8

* Thu Feb 14 2019 Cory McIntire <cory@cpanel.net> - 10.3.2-2
- EA-8203: Add IonCube 10 support for PHP 7.3

* Thu Feb 07 2019 Cory McIntire <cory@cpanel.net> - 10.3.2-1
- EA-8106: Update from 10.2.4 to 10.3.2

* Tue Jul 31 2018 Tim Mullin <tim@cpanel.net> - 10.2.4-1
- EA-7753: Update from 10.2.2 to 10.2.4

* Fri Jul 06 2018 Tim Mullin <tim@cpanel.net> - 10.2.2-1
- EA-7609: Update from 10.2.0 to 10.2.2

* Wed Apr 25 2018 Daniel Muey <dan@cpanel.net> - 10.2.0-2
- EA-7374: Remove Experimental verbiage from verbiage

* Mon Apr 02 2018 Cory McIntire <cory@cpanel.net> - 10.2.0-1
- EA-7313: Update from 10.1.1 to 10.2.0

* Tue Feb 27 2018 Daniel Muey <dan@cpanel.net> - 10.1.1-1
- EA-7250: Update from 10.1.0 to 10.1.1

* Tue Dec 19 2017 Cory McIntire <cory@cpanel.net> - 10.1.0-2
- EA-7026: Add IonCube 10 support for PHP 7.2

* Thu Dec 14 2017 Cory McIntire <cory@cpanel.net> - 10.1.0-1
- EA-7024: Update from 10.0.3 to 10.1.0

* Thu Oct 12 2017 Dan Muey <dan@cpanel.net> - 10.0.3-2
- EA-6734: add 5.4, 5.5, 5.6, and 7.0 packages (7.2 support is still beta ATM)

* Wed Oct 11 2017 Dan Muey <dan@cpanel.net> - 10.0.3-1
- EA-6820: Update from 10.0.0 to 10.0.3

* Mon Aug 28 2017 Dan Muey <dan@cpanel.net> - 10.0.0-1
- EA-6684: initial version 10
