Name:           twirssi
Version:        2.5.1
Release:        1%{?dist}
Summary:        Twirssi allows you to post to Twitter from Irssi.
License:        GPLv2
Group:          Applications/Communications
URL:            http://twirssi.com/
Source0:        http://twirssi.com/%{name}-%{version}.pl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Twirssi allows you to post to Twitter and Identi.ca from Irssi, as well as:

* Read your friend feed, and your replies (from people on and not on your feed).
* Receive and send direct messages (DMs)
* Use multiple accounts, on either twitter or identi.ca - follow, read and post
* See the context when your friends reply to users you aren't following

%prep

%build

%install

install -d $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts
install %{_sourcedir}/%{name}-%{version}.pl $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts/%{name}.pl

%{_fixperms} $RPM_BUILD_ROOT/*

%clean

%files
%{_datarootdir}/irssi/scripts/%{name}.pl

%changelog
* Wed Feb 29 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-1
- Update to 2.5.1

* Mon Jul 05 2010 Julian C. Dunn <jdunn@aquezada.com> 2.4.3-1
- Initial import of 2.4.3
