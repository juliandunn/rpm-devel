Name:		ttytter
Version:	1.2.05
Release:	1%{?dist}
Summary:	TTYTTer is a command line Twitter client in Perl.
License:	Floodgap Free Software Licence
Group:		Applications/Communications
URL:		http://www.floodgap.com/software/ttytter/
Source0:	http://www.floodgap.com/software/ttytter/dist1/%{version}.txt
BuildArch:	noarch
Requires:	curl
Requires:	perl(Date::Parse)
Requires:	perl(Date::Format)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
TTYtter is a 100% Perl Twitter client.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/ttytter

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/ttytter

%changelog
* Tue May 12 2012 Julian C. Dunn <jdunn@aquezada.com> 1.2.05-1
- Update to 1.2.05

* Tue May 05 2011 Julian C. Dunn <jdunn@aquezada.com> 1.1.11-1
- Update to 1.1.11

* Sun Nov 21 2010 Julian C. Dunn <jdunn@aquezada.com> 1.1.9-1
- Initial revision
