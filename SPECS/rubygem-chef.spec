# Generated from chef-11.12.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chef

# Turn off any bytecompiling of python. That's because Chef ships a
# script called yum-dump.py and we don't want that to be bytecompiled.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name: rubygem-%{gem_name}
Version: 11.12.4
Release: 1%{?dist}
Summary: The Chef configuration management system
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/opscode/chef
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: chef.gemspec.patch
Patch1: chef.ffi-yajl.patch
Patch2: chef.hardcoded-paths-in-tests.patch
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(mixlib-config)
Requires: rubygem(mixlib-cli)
Requires: rubygem(mixlib-log)
Requires: rubygem(mixlib-authentication)
Requires: rubygem(mixlib-shellout)
Requires: rubygem(ohai)
Requires: rubygem(rest-client) < 1.7.0
Requires: rubygem(mime-types) => 1.16
Requires: rubygem(mime-types) < 2
Requires: rubygem(ffi-yajl) >= 0.2.0
Requires: rubygem(net-ssh)
Requires: rubygem(net-ssh-multi)
Requires: rubygem(highline) >= 1.6.9
Requires: rubygem(erubis) >= 2.7
Requires: rubygem(diff-lcs) >= 1.2.4
Requires: rubygem(chef-zero) >= 2.0.2
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(rack) 
# BuildRequires: rubygem(rspec_junit_formatter) 
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(rspec-mocks)
BuildRequires: rubygem(mixlib-authentication)
BuildRequires: rubygem(erubis)
BuildRequires: rubygem(rest-client)
BuildRequires: rubygem(chef-zero)
BuildRequires: rubygem(highline)
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(net-ssh-multi)
BuildRequires: rubygem(ffi-yajl)
BuildRequires: rubygem(mime-types)
# Needed by tests
BuildRequires: git
BuildRequires: hostname
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A systems integration framework, built to bring the benefits of configuration
management to your entire infrastructure.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Move manpages
mkdir -p %{buildroot}%{_mandir}
rm %{buildroot}%{gem_instdir}/distro/common/man/man1/README.md
mv %{buildroot}%{gem_instdir}/distro/common/man/{man1,man8} \
        %{buildroot}%{_mandir}
rmdir %{buildroot}%{gem_instdir}/distro/common/man
# Remove markdown files; only needed to generate man pages and HTML docs
rm -rf %{buildroot}%{gem_instdir}/distro/common/markdown

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/tasks
%{_bindir}/chef-client
%{_bindir}/chef-solo
%{_bindir}/knife
%{_bindir}/chef-shell
%{_bindir}/shef
%{_bindir}/chef-apply
%{_mandir}/man1
%{_mandir}/man8
# Irrelevant on non-Windows
%exclude %{_bindir}/chef-service-manager
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/distro

%changelog
* Mon Jun 30 2014 Julian C. Dunn (<jdunn@aquezada.com>) - 11.12.4-1
- Major update to 11.12.4

* Sun May 27 2012 Jonas Courteau <rpms@courteau.org> - 0.10.10-2
- Fixed license short name
- Updated summary
- Don't package markdown docs
- Don't package tests
- Added chkconfig to post/preun sections
- Converted to fc17 Rubygem build format

* Sat May 12 2012 Jonas Courteau <rpms@courteau.org> - 0.10.10-1
- Updated to 0.10.10

* Sun Apr 22 2012 Jonas Courteau <rpms@courteau.org> - 0.10.8-1
- Initial package
