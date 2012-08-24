Name:           gecode
Version:        3.7.3
Release:        3%{?dist}
Summary:        Generic constraint development environment

Group:          System Environment/Libraries
License:        MIT
URL:            http://www.gecode.org/
Source0:        http://www.gecode.org/download/%{name}-%{version}.tar.gz
Patch0:         gecode-3.7.3-no_examples.patch

BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex >= 2.5.33
BuildRequires:  graphviz
BuildRequires:  qt4-devel

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
mkdir -p ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}-doc-%{version}
mv doc/html ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}-doc-%{version}


%clean


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc ChangeLog LICENSE
%{_libdir}/*.so.*

%files devel
%{_bindir}/fz
%{_bindir}/mzn-gecode
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/*.so

%files doc
%{_defaultdocdir}/%{name}-doc-%{version}

%files examples
%doc examples/*

%changelog
* Wed Aug 23 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-3
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
