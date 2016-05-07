Name:           perl-WWW-Shorten
Version:        3.08
Release:        1%{?dist}
Summary:        Interface to URL shortening sites
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Shorten/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVECROSS/WWW-Shorten-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  glibc-common
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Auto)
BuildRequires:  perl(LWP) >= 5.75
BuildRequires:  perl(LWP::UserAgent) >= 2.023
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(URI) >= 1.27
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A unified interface to various URL shortening services on the web, such as
TinyURL or makeashorterlink.com.

%prep
%setup -q -n WWW-Shorten-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 LICENCE > LICENCE.conv && touch -r LICENCE LICENCE.conv && mv -f LICENCE.conv LICENCE

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test --test_files 't/0*.t'

%files
%doc Artistic AUTHORS ChangeLog.SPOON Changes CREDITS LICENCE README TODO
%{perl_vendorlib}/*
%{_bindir}/shorten
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 9 2016 Julian C. Dunn <jdunn@aquezada.com> - 3.08-1
- Upgrade to 3.08 (bz#1296197)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.06-2
- Perl 5.22 rebuild

* Fri Jan 23 2015 Julian C. Dunn <jdunn@aquezada.com> - 3.06-1
- Upgrade to 3.06 (bz#1142983)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.05-2
- Perl 5.20 rebuild

* Sat Jun 07 2014 Julian C. Dunn <jdunn@aquezada.com> - 3.05-1
- Upgrade to 3.05 (bz#1095263)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Julian C. Dunn <jdunn@aquezada.com> - 3.04-1
- Upgrade to 3.04 (bz#1000526)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 3.03-5
- Perl 5.18 rebuild
- Skip t/98pod-coverage.t test (CPAN RT#85418)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 3.03-2
- Perl 5.16 rebuild

* Sun Apr 08 2012 Julian C. Dunn <jdunn@aquezada.com> 3.03-1
- Update to 3.03
- Run only tests that do not require network access

* Thu Apr 05 2012 Julian C. Dunn <jdunn@aquezada.com> 3.02-2
- Changes per review in bz#810028

* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 3.02-1
- Initial packaging based on cpanspec 1.78 output
