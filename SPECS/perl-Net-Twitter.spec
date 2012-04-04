Name:           perl-Net-Twitter
Version:        3.18001
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
BuildRequires:  perl(Crypt::SSLeay) >= 0.5
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(DateTime) >= 0.51
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.09
BuildRequires:  perl(Devel::StackTrace) >= 1.21
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent) >= 5.819
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
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny) >= 0.03
BuildRequires:  perl(URI) >= 1.4
BuildRequires:  perl(URI::Escape)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Net::Netrc)

%description
This module provides a perl interface to the Twitter APIs. See
http://dev.twitter.com/doc for a full description of the Twitter APIs.

%prep
%setup -q -n Net-Twitter-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
env TEST_POD=1 make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 27 2012 Julian C. Dunn <jdunn@aquezada.com> 3.18001-1
- Initial release.
