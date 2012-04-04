Name:           perl-WWW-Shorten
Version:        3.02
Release:        1%{?dist}
Summary:        Interface to URL shortening sites
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/WWW-Shorten/
Source0:        http://www.cpan.org/authors/id/D/DA/DAVECROSS/WWW-Shorten-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Config::Auto)
BuildRequires:  perl(LWP) >= 5.75
BuildRequires:  perl(LWP::UserAgent) >= 2.023
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(URI) >= 1.27
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A unified interface to various URL shortening services on the web, such as
TinyURL or makeashorterlink.com.

%prep
%setup -q -n WWW-Shorten-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Artistic AUTHORS ChangeLog.SPOON Changes COPYING CREDITS LICENCE README TODO
%{perl_vendorlib}/*
%{_bindir}/shorten
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 3.02-1
- Initial packaging based on cpanspec 1.78 output
