%define debug_package %{nil}

Summary:	A Nagios plugin to check APC devices
Name:		nagios-okplugin-apc
Version:	2.1.0
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/System
URL:		http://opensource.ok.is/trac/wiki/Nagios-OKPlugin-APC
Source0:	http://opensource.ok.is/trac/browser/nagios-plugins/check_apcext.pl/releases/nagios-okplugin-apc-%{version}.tar.gz
Requires:	nagios-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Tomas Edwardsson <tommi@ok.is>
BuildArch:	noarch


%description
Checks APC devices, both netbotz and UPS

%prep
%setup -q
#perl -pi -e "s|/usr/lib|%{_libdir}|g" check_sip

%build


%install
rm -rf %{buildroot}
install -D -p -m 0755 check_apcext.pl %{buildroot}%{_libdir}/nagios/plugins/check_apcext.pl
install -D -p -m 0755 check_snmp_apc_ups %{buildroot}%{_libdir}/nagios/plugins/check_snmp_apc_ups

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/nagios/plugins/*

%changelog
* Thu Aug 23 2012 Pall Sigurdsson <palli@opensource.is> 2.1.0-1
- Version number bumped to 2.1.0 (palli@opensource.is)
- Added noarch buildarch (tommi@tommi.org)

* Mon Mar 12 2012 Pall Sigurdsson <palli@opensource.is> 0.0.3-1
- new package built with tito

* Mon Mar  1 2010  Tomas Edwardsson <tommi@ok.is> 0.1-1
- Initial packaging
