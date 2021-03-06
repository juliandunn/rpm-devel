Name:           perl-Net-Trac
Version:        0.16
Release:        1%{?dist}
Summary:        Interact with a remote Trac instance
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-Trac/
Source0:        http://www.cpan.org/authors/id/S/SP/SPANG/Net-Trac-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Mechanize) >= 1.52
Requires:       perl(Any::Moose)
Requires:       perl(DateTime)
Requires:       perl(HTTP::Date)
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(LWP::Simple)
Requires:       perl(Params::Validate)
Requires:       perl(Text::CSV)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Requires:       perl(WWW::Mechanize) >= 1.52
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Net::Trac is simple client library for a remote Trac instance. Because Trac
doesn't provide a web services API, this module currently "fakes" an RPC
interface around Trac's webforms and the feeds it exports. Because of this,
it's somewhat more brittle than a true RPC client would be.

%prep
%setup -q -n Net-Trac-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri May 13 2011 Julian C. Dunn <jdunn@aquezada.com> 0.16-1
- Specfile autogenerated by cpanspec 1.78.
