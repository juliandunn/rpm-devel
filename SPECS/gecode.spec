Name:           gecode
Version:        4.4.0
Release:        1%{?dist}
Summary:        Generic constraint development environment

Group:          System Environment/Libraries
License:        MIT
URL:            http://www.gecode.org/
Source0:        http://www.gecode.org/download/%{name}-%{version}.7z
Patch0:         gecode-4.0.0-no_examples.patch

BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex >= 2.5.33
BuildRequires:  graphviz
BuildRequires:  qt4-devel
BuildRequires:  p7zip

# Fedora < 20 doesn't have this macro
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# for documentation
BuildRequires:  doxygen tex(latex) tex(dvips)

%description
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6
BuildArch: noarch
%endif

%description doc
The %{name}-doc package contains documentation files for %{name}.


%package examples
Summary:        Example code for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
%if 0%{?fedora} >= 10 || 0%{?rhel} >= 6
BuildArch: noarch
%endif

%description examples
The %{name}-examples package contains example code for %{name}.


%prep
%setup -q
%patch0 -p1 -b .no_examples

# Fix permissions
find . -name '*.hh' -exec chmod 0644 '{}' \;
find . -name '*.hpp' -exec chmod 0644 '{}' \;
find . -name '*.cpp' -exec chmod 0644 '{}' \;
chmod 0644 LICENSE misc/doxygen/*.png

# Fix encoding
pushd examples
for file in bin-packing.cpp black-hole.cpp dominating-queens.cpp scowl.hpp word-square.cpp; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd


%build
aclocal
autoconf

%configure \
  --disable-examples \
  --enable-float-vars \
  --enable-leak-debug \
  --with-boost-include=%{_includedir}/boost

make %{?_smp_mflags}
make doc
make ChangeLog

iconv --from=ISO-8859-1 --to=UTF-8 -o ChangeLog.new ChangeLog
mv ChangeLog.new ChangeLog


%install
make install DESTDIR=$RPM_BUILD_ROOT

#move docs and examples to build root
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
mv doc/html ${RPM_BUILD_ROOT}%{_pkgdocdir}


%clean


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc ChangeLog LICENSE
%{_libdir}/*.so.*
%exclude %{_pkgdocdir}/html

%files devel
%{_bindir}/fzn-gecode
%{_bindir}/mzn-gecode
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so

%files doc
%{_pkgdocdir}
%exclude %{_pkgdocdir}/ChangeLog
%exclude %{_pkgdocdir}/LICENSE

%files examples
%doc examples/*

%changelog
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 4.3.3-2
- Rebuild for boost 1.57.0

* Fri Jan 23 2015 Julian C. Dunn <jdunn@aquezada.com> - 4.3.3-1
- Update to 4.3.3

* Mon Sep 29 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.3.0-1
- Update to 4.3.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.2.1-2
- Rebuild for boost 1.55.0

* Sat Nov 16 2013 Julian C. Dunn <jdunn@aquezada.com> 4.2.1-1
- Update to 4.2.1

* Fri Aug 23 2013 Julian C. Dunn <jdunn@aquezada.com> 4.2.0-1
- Update to 4.2.0
- Switch to unversioned docdir for >= F20 (bz#993768)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 4.0.0-2
- Rebuild for boost 1.54.0

* Sat Jun 15 2013 Julian C. Dunn <jdunn@aquezada.com> 4.0.0-1
- Update to 4.0.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-3
- Fix build on EPEL6

* Tue Aug 21 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-2
- Post-review comments in bz#843695

* Sun May 20 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-1
- Update for 3.7.3
- Drop support for EPEL5. flex is too old

* Fri Apr 01 2011 Erik Sabowski and James Sulinski <team@aegisco.com> 3.5.0-1
- Update for gecode-3.5.0
- Disabled "gist" and "qt" configure options

* Sat May  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 3.3.1-1
- Initial RPM release
