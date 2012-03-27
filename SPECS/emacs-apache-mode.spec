Name:           emacs-apache-mode
Version:        2.0
Release:        2%{?dist}
Summary:        Major mode for editing Apache files in Emacs
License:        GPLv2
Group:          Development/Libraries
URL:            http://www.emacswiki.org/cgi-bin/wiki/apache-mode.el
Source: 	http://www.emacswiki.org/cgi-bin/wiki/download/apache-mode.el
Patch1:		apache-mode.el-empirehouse.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       emacs

%description
apache-mode.el is an Emacs major mode for editing Apache HTTPD
configuration files.

%prep
%setup -q -c -T
cp %{S:0} %{_builddir}/%{name}-%{version}
%patch1

%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/emacs/site-lisp
install %{_builddir}/%{?buildsubdir}/apache-mode.el $RPM_BUILD_ROOT/%{_datadir}/emacs/site-lisp

%{_fixperms} $RPM_BUILD_ROOT/*

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/apache-mode.el


%changelog
* Tue Apr 05 2011 Julian C. Dunn <jdunn@aquezada.com> - 2.0-2
- Patch with current directive list for Apache 2.2

* Thu Nov 11 2010 Julian C. Dunn <jdunn@aquezada.com> - 092710-1
- Initial build
