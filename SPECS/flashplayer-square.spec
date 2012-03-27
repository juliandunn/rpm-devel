Name:           flashplayer-square
Version:        111710
Release:        2%{?dist}
Summary:        Adobe Flash Player "Square" Developer Prerelease
License:        Proprietary
Group:          Development/Libraries
URL:            http://labs.adobe.com/
Source0:		http://download.macromedia.com/pub/labs/flashplayer10/flashplayer10_2_p3_64bit_linux_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      x86_64
Requires:       mozilla-filesystem

%description
Developer preview release of Adobe® Flash® Player "Square" (codename).
Flash Player "Square" enables 64-bit and enhanced Internet Explorer 9
support. 

%prep
%setup -q -c


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/lib64/mozilla/plugins
install libflashplayer.so $RPM_BUILD_ROOT/usr/lib64/mozilla/plugins

%{_fixperms} $RPM_BUILD_ROOT/*

%check

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/mozilla/plugins/libflashplayer.so


%changelog
* Sun Dec 12 2010 Julian C. Dunn <jdunn@aquezada.com> - 111710-1
- Upgrade to 10.2 preview 3

* Thu Nov 11 2010 Julian C. Dunn <jdunn@aquezada.com> - 092710-1
- Initial build


