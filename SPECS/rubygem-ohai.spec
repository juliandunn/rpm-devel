# Generated from ohai-7.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ohai

Name: rubygem-%{gem_name}
Version: 7.0.4
Release: 1%{?dist}
Summary: Ohai profiles your system and emits JSON
Group: Development/Languages
License: ASL
URL: http://github.com/opscode/ohai
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: ohai-ffi-yajl.patch
Patch1: ohai-gemspec.patch
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(mime-types)
Requires: rubygem(systemu)
Requires: rubygem(ffi-yajl) 
Requires: rubygem(mixlib-cli) 
Requires: rubygem(mixlib-config) 
Requires: rubygem(mixlib-log) 
Requires: rubygem(mixlib-shellout)
Requires: rubygem(ipaddress) 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
# BuildRequires: rubygem(rspec-core) 
# BuildRequires: rubygem(rspec-expectations) 
# BuildRequires: rubygem(rspec-mocks) 
# BuildRequires: rubygem(rspec_junit_formatter) 
# BuildRequires: rubygem(chef) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Ohai profiles your system and emits JSON.


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

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -pa ./%{_bindir}/* %{buildroot}%{_bindir}

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib
popd

%files
%dir %{gem_instdir}
%{_bindir}/ohai
%{gem_instdir}/bin
# XXX what to do with this?
%doc %{gem_instdir}/docs/man/man1/ohai.1
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE

%changelog
* Fri Jun 27 2014 Julian C. Dunn (<jdunn@aquezada.com>) - 7.0.4-1
- Initial package
