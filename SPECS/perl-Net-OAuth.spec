Name:           perl-Net-OAuth
Version:        0.27
Release:        3%{?dist}
Summary:        OAuth protocol support library for Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-OAuth/
Source0:        http://www.cpan.org/authors/id/K/KG/KGRENNAN/Net-OAuth-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor) >= 0.31
BuildRequires:  perl(Class::Data::Inheritable) >= 0.06
BuildRequires:  perl(Digest::HMAC_SHA1) >= 1.01
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(UNIVERSAL::require) >= 0.10
BuildRequires:  perl(URI::Escape) >= 3.28
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Class::Accessor) >= 0.31
Requires:       perl(Class::Data::Inheritable) >= 0.06

%description
Perl implementation of OAuth, an open protocol to allow secure API
authentication in a simple and standard method from desktop and web
applications. In practical terms, a mechanism for a Consumer to request
protected resources from a Service Provider on behalf of a user.


%prep
%setup -q -n Net-OAuth-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.19-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.19-2
- rebuild against perl 5.10.1

* Tue Oct 13 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.19-1
- Update to 0.19, fixes security issue (2009.1)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 28 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.14-2
- Fix Requires

* Thu Apr 16 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> 0.14-1
- Specfile autogenerated by cpanspec 1.78.
