Name:           twirssi
Version:        2.6.3
Release:        1%{?dist}
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

# For Fedora < F20, which had versioned docdirs
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Twirssi allows you interact with Twitter and Identi.ca from Irssi. It can
handle tweets and direct messages (DMs), and supports multiple accounts on
either Twitter or Identi.ca.

%prep

%build

%install

install -d $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts
install -m 644 -p %{SOURCE0} $RPM_BUILD_ROOT%{_datarootdir}/irssi/scripts/%{name}.pl
install -d $RPM_BUILD_ROOT%{_pkgdocdir}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_pkgdocdir}
install -m 644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%{_datarootdir}/irssi/scripts/%{name}.pl
%doc %{_pkgdocdir}

%changelog
* Thu Jan 16 2014 Julian C. Dunn <jdunn@aquezada.com> 2.6.3-1
- Update to 2.6.3 (bz#1054485)

* Sun Sep 15 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.2-1
- Update to 2.6.2 (bz#1008269)

* Sat Aug 24 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.0-4
- Update for unversioned docdir change (bz#993953)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.6.0-2
- Perl 5.18 rebuild

* Fri Jun 14 2013 Julian C. Dunn <jdunn@aquezada.com> 2.6.0-1
- Upgrade to 2.6.0 for Twitter 1.1 API

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 05 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-3
- Correct missed deps per bz#809948

* Wed Apr 04 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-2
- Changes per review in bz#808254

* Wed Feb 29 2012 Julian C. Dunn <jdunn@aquezada.com> 2.5.1-1
- Update to 2.5.1

* Mon Jul 05 2010 Julian C. Dunn <jdunn@aquezada.com> 2.4.3-1
- Initial import of 2.4.3
