Name:           amanda-server-bedroomlan-labels
Version:        1.0
Release:        2%{?dist}
Summary:        Improved PostScript tape labels for Amanda
License:        GPLv2
Group:          Applications/System
URL:            http://www.bedroomlan.org/postscript/
Source0:	http://files.bedroomlan.org/amanda/EXB-8500.ps
Source1:	http://files.bedroomlan.org/amanda/DLT.ps
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       amanda-server

%description
A set of Postscript labels by Alexios (www.bedroomlan.org) for Amanda.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/amanda/DailySet1/label-templates
install -m 644 %{S:0} $RPM_BUILD_ROOT%{_sysconfdir}/amanda/DailySet1/label-templates/bedroomlan-EXB-8500.ps
install -m 644 %{S:1} $RPM_BUILD_ROOT%{_sysconfdir}/amanda/DailySet1/label-templates/bedroomlan-DLT.ps

%{_fixperms} $RPM_BUILD_ROOT/*

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,amandabackup,disk,-)
%{_sysconfdir}/amanda/DailySet1/label-templates/bedroomlan-*


%changelog
* Sun Nov 21 2010 Julian C. Dunn <jdunn@aquezada.com> - 1.0-1
- Initial build


