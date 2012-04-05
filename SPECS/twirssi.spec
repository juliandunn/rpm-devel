Name:           twirssi
Version:        2.5.1
Release:        3%{?dist}
Summary:        An Irssi script to interact with Twitter
License:        GPLv2
Group:          Applications/Communications
URL:            http://twirssi.com/
Source0:        http://twirssi.com/%{name}-%{version}.pl
Source1:        https://raw.github.com/zigdon/twirssi/master/README
Source2:        https://raw.github.com/zigdon/twirssi/master/gpl-2.0.txt
BuildArch:      noarch
Requires:       irssi
Requires:       perl(base)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Temp)
Requires:       perl(HTML::Entities)
Requires:       perl(HTTP::Date)
Requires:       perl(Irssi)
Requires:       perl(Irssi::Irc)
Requires:       perl(JSON::Any)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)  
Requires:       perl(Net::Twitter) >= 3.11009
Requires:       perl(WWW::Shorten)

%description
Twirssi allows you interact with Twitter and Identi.ca from Irssi. It can
handle tweets and direct messages (DMs), and supports multiple accounts on
either Twitter or Identi.ca.

%prep

%build

%install

install -d $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts
install -m 644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts/%{name}.pl
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%{_datarootdir}/irssi/scripts/%{name}.pl
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Apr 05 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-3
- Correct missed deps per bz#809948

* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-2
- Changes per review in bz#808254

* Wed Feb 29 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-1
- Update to 2.5.1

* Mon Jul 05 2010 Julian C. Dunn <jdunn@aquezada.com> 2.4.3-1
- Initial import of 2.4.3
