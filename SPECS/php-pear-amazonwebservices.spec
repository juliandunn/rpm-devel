%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}

Name:		php-channel-amazonwebservices
Version:	1.0.0
Release:	1%{?dist}
Summary:	Adds Amazon Web Services channel to PEAR

Group:		Development/Languages
License:	LGPLv2
URL:		https://github.com/amazonwebservices/
Source0:	http://pear.amazonwebservices.com/channel.xml
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:	php-pear >= 1:1.4.9-1.2
Requires:	php-cli
Requires:	php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:	php-channel(pear.amazonwebservices.com)

%description
This package adds the Amazon Web Services channel which allows
the Amazon PHP SDK to be installed.


%prep
%setup -q -c -T


%build
# Empty build section, nothing to build


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{pear_xmldir}
%{__install} -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{pear_xmldir}/pear.amazonwebservices.com.xml


%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
if [ $1 -eq  1 ] ; then
	%{__pear} channel-add %{pear_xmldir}/pear.amazonwebservices.com.xml > /dev/null || :
else
	%{__pear} channel-update %{pear_xmldir}/pear.amazonwebservices.com.xml > /dev/null ||:
fi


%postun
if [ $1 -eq 0 ] ; then
	%{__pear} channel-delete pear.amazonwebservices.com > /dev/null || :
fi


%files
%defattr(-,root,root,-)
%{pear_xmldir}/*


%changelog
* Mon Feb 21 2011 Julian C. Dunn <jdunn@aquezada.com> - 1.0.0-1
- Initial release
