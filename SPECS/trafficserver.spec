# FIXME: provide systemd startup for rawhide/F15
#	https://fedoraproject.org/wiki/Packaging:Guidelines:Systemd
Summary:	Fast, scalable and extensible HTTP/1.1 compliant caching proxy server
Name:		trafficserver
Version:	3.0.3
Release:	1%{?dist}
License:	ASL 2.0
Group:		System Environment/Daemons
Source0:	http://www.apache.org/dist/%{name}/%{name}-%{version}.tar.bz2
Source1:	trafficserver.sysconf
URL:		http://trafficserver.apache.org/index.html
# BuildRoot is only needed for EPEL5:
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	autoconf, automake, libtool, openssl-devel, tcl-devel, expat-devel
BuildRequires:	pcre-devel, zlib-devel, xz-devel, gcc-c++

Patch2:		trafficserver-init_scripts.patch
Patch7:		trafficserver_make_install.patch
Patch51:	trafficserver-cluster_interface_linux.patch
# Fixed on v3.1:
Patch52:	trafficserver-condrestart.patch


%description
Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant
caching proxy server.

%prep
%setup -q

%patch2 -p1 -b .patch2
%patch7 -p1 -b .patch7
%patch51 -p1 -b .patch51
%patch52 -p1 -b .patch52

%build
./configure --enable-layout=Gentoo --libdir=%{_libdir}/trafficserver --with-tcl=%{_libdir} --with-user=ats --with-group=ats
make %{?_smp_mflags}

%install
echo $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# the traffic_shell manual conflict with bash: exit enable,
# so we rename these to ts-enable, ts-exit and ts-disable.
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
cp doc/man/*.1 $RPM_BUILD_ROOT/usr/share/man/man1/
mv $RPM_BUILD_ROOT/usr/share/man/man1/enable.1 \
$RPM_BUILD_ROOT/usr/share/man/man1/ts-enable.1
mv $RPM_BUILD_ROOT/usr/share/man/man1/disable.1 \
$RPM_BUILD_ROOT/usr/share/man/man1/ts-disable.1
mv $RPM_BUILD_ROOT/usr/share/man/man1/exit.1 \
$RPM_BUILD_ROOT/usr/share/man/man1/ts-exit.1
cat <<EOF > README.fedora
The man-pages for enable, disable and exit was renamed to ts-enable, 
ts-disable and ts-exit to avoid conflicts with other man-pages.
EOF

mkdir -p $RPM_BUILD_ROOT/etc/init.d/
mv $RPM_BUILD_ROOT/usr/bin/trafficserver $RPM_BUILD_ROOT/etc/init.d

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 -p %{SOURCE1} \
   $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/trafficserver

# Remove static libs (needs to go to separate -static subpackage if we
# want these:
rm -f $RPM_BUILD_ROOT/%{_libdir}/trafficserver/libtsmgmt.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/trafficserver/libtsutil.a

# Don't include libtool archives:
rm -f $RPM_BUILD_ROOT/%{_libdir}/trafficserver/libtsmgmt.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/trafficserver/libtsutil.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/trafficserver/plugins/conf_remap.la

# The clean section  is only needed for EPEL and Fedora < 13
# http://fedoraproject.org/wiki/PackagingGuidelines#.25clean
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, ats, ats, -)
%doc README CHANGES NOTICE README.fedora LICENSE
%attr(0644, root, root) /usr/share/man/man1/*
%attr(0755,root,root) /usr/bin/traffic*
%attr(0755,root,root) %dir %{_libdir}/trafficserver
%attr(0755,root,root) %dir %{_libdir}/trafficserver/plugins
%attr(0755,root,root) %{_libdir}/trafficserver/*.so.*
%attr(0755,root,root) %{_libdir}/trafficserver/plugins/*.so
%config(noreplace) /etc/trafficserver/*
%attr(0755, root, root) /etc/init.d/trafficserver
%attr(0755, ats, ats) %dir /etc/trafficserver
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/sysconfig/trafficserver
%dir /var/log/trafficserver
%dir /var/run/trafficserver
%dir /var/cache/trafficserver

%post
/sbin/ldconfig
if [ $1 -eq 1 ] ; then
  /sbin/chkconfig --add %{name}
fi

%pre
getent group ats >/dev/null || groupadd -r ats -g 176 &>/dev/null
getent passwd ats >/dev/null || \
useradd -r -u 176 -g ats -d / -s /sbin/nologin \
	-c "Apache Traffic Server" ats &>/dev/null

%preun
if [ $1 -eq 0 ] ; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%postun
/sbin/ldconfig
if [ $1 -eq 1 ] ; then
   /sbin/service trafficserver condrestart &>/dev/null || :
fi


%package devel
Summary: Apache Traffic Server development libraries and header files
Group: Development/Libraries
Requires: trafficserver = %{version}-%{release}
%description devel
The trafficserver-devel package include plug-in development libraries and
header files, and Apache httpd style module build system.

%files devel
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/bin/tsxs
%attr(0755,root,root) %dir /usr/include/ts
%attr(0644,root,root) /usr/include/ts/*
%attr(0755,root,root) %dir %{_libdir}/trafficserver
%attr(0755,root,root) %dir %{_libdir}/trafficserver/plugins
%attr(0644,root,root) %{_libdir}/trafficserver/*.so

%changelog
* Sat Mar 10 2012 <janfrode@tanso.net> - 3.0.3-1
- Removed mixed use of spaces and tabs in specfile.

* Mon Feb 13 2012 <janfrode@tanso.net> - 3.0.3-0
- Update to v3.0.3

* Thu Dec 8 2011 <janfrode@tanso.net> - 3.0.2-0
- Update to v3.0.2
- Fix conderestart in initscript, TS-885.

* Tue Jul 19 2011 <janfrode@tanso.net> - 3.0.1-0
- Update to v3.0.1
- Remove uninstall-hook from trafficserver_make_install.patch, removed in v3.0.1.

* Thu Jun 30 2011 <janfrode@tanso.net> - 3.0.0-6
- Note FIXME's on top.
- Remove .la and static libs.
- mktemp'd buildroot.
- include license

* Mon Jun 27 2011 <janfrode@tanso.net> - 3.0.0-5
- Rename patches to start with trafficserver-.
- Remove odd version macro.
- Clean up mixed-use-of-spaces-and-tabs.

* Wed Jun 23 2011 <janfrode@tanso.net> - 3.0.0-4
- Use dedicated user/group ats/ats.
- Restart on upgrades.

* Thu Jun 16 2011 <zym@apache.org> - 3.0.0-3
- update man pages, sugest from Jan-Frode Myklebust <janfrode@tanso.net>
- patch records.config to fix the crashing with cluster iface is noexist
- cleanup spec file

* Wed Jun 15 2011 <zym@apache.org> - 3.0.0-2
- bump to version 3.0.0 stable release
- cleanup the spec file and patches

* Tue May 24 2011 <yonghao@taobao.com> - 2.1.8-2
- fix tcl linking

* Thu May  5 2011 <yonghao@taobao.com> - 2.1.8-1
- bump to 2.1.8
- comment out wccp

* Fri Apr  1 2011 <yonghao@taobao.com> - 2.1.7-3
- enable wccp and fixed compile warning
- never depends on sqlite and db4, add libz and xz-libs
- fix libary permission, do post ldconfig updates

* Sun Mar 27 2011 <yonghao@taobao.com> - 2.1.7-2
- patch traffic_shell fix

* Tue Mar 22 2011 <yonghao@taobao.com> - 2.1.7-1
- bump to v2.1.7
- fix centos5 building
- drop duplicated patches

* Tue Mar 19 2011 <yonghao@taobao.com> - 2.1.6-2
- fix gcc 4.6 building
- split into -devel package for devel libs
- fix init scripts for rpmlint requirement
- fix install scripts to build in mock, without root privileges

* Tue Mar 01 2011 <yonghao@taobao.com> - 2.1.6-1
- bump to 2.1.6 unstable
- replace config layout name as Fedora

* Thu Nov 18 2010 <yonghao@taobao.com> - 2.1.4
- initial release for public
- original spec file is from neomanontheway@gmail.com
