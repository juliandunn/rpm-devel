Name:           perl-Net-Twitter
Version:        4.01004
Release:        1%{?dist}
Summary:        Perl interface to the Twitter API
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-Twitter/
Source0:        http://www.cpan.org/authors/id/M/MM/MMIMS/Net-Twitter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Crypt::SSLeay) >= 0.5
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(DateTime) >= 0.51
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.09
BuildRequires:  perl(Devel::StackTrace) >= 1.21
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent) >= 5.819
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 0.9
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Net::Netrc)
BuildRequires:  perl(Net::OAuth) >= 0.25
BuildRequires:  perl(Pod::Coverage) >= 0.19
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Spelling) >= 0.11
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny) >= 0.03
BuildRequires:  perl(URI) >= 1.4
BuildRequires:  perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Net::Netrc)

%description
This module provides a Perl interface to the Twitter APIs. See
http://dev.twitter.com/doc for a full description of the Twitter APIs.

%prep
%setup -q -n Net-Twitter-%{version}

%build
%{__perl} Build.PL --installdirs vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Apr 14 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01004-1
- Upgrade to 4.01004 (bz#1087334)

* Sat Mar 15 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01003-1
- Upgrade to 4.01003 (bz#1076563)

* Sun Jan 19 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01002-1
- Upgrade to 4.01002 (bz#1055295)

* Thu Nov 21 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.01000-1
- Upgrade to 4.01000 (bz#1032571)

* Thu Aug 22 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00007-1
- Upgrade to 4.00007 (bz#996455)

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 4.00006-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.00006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00006-1
- Upgrade to 4.00006 (bz#914316)

* Wed Mar 13 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00004-1
- Upgrade to 4.00004 (bz#914316)

* Fri Mar 08 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00003-1
- Upgrade to 4.00003 (bz#914316)

* Sun Feb 24 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00002-1
- Upgrade to 4.00002 (bz#914316)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Julian C. Dunn <jdunn@aquezada.com> - 3.18004-1
- Upgrade to 3.18004 (bz#866878)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 3.18003-2
- Perl 5.16 rebuild

* Mon Jul 02 2012 Julian C. Dunn <jdunn@aquezada.com> - 3.18003-1
- Upgrade to 3.18003

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 3.18002-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Julian C. Dunn <jdunn@aquezada.com> 3.18002-1
- Upgrade to 3.18002

* Tue Mar 27 2012 Julian C. Dunn <jdunn@aquezada.com> 3.18001-1
- Initial release.
