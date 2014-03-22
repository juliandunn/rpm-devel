# Generated from ffi-yajl-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ffi-yajl

Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 1%{?dist}
Summary: Ruby FFI wrapper around YAJL 2.x
Group: Development/Languages
License: Apache-2.0
URL: http://github.com/lamont-granquist/ffi-yajl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(ffi)
Requires: yajl
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildRequires: ruby-devel 
BuildRequires: yajl-devel
Provides: rubygem(%{gem_name}) = %{version}

%description
Ruby FFI wrapper around YAJL 2.x

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/lib
# Not sure I need to do this?
mv %{buildroot}%{gem_instdir}/lib/libyajl.so %{buildroot}%{gem_extdir_mri}/lib/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
rspec
popd

%files
%dir %{gem_instdir}
%{_bindir}/ffi-yajl-bench
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE

%changelog
* Sat Mar 22 2014 Julian C. Dunn (<jdunn@aquezada.com>) - 0.0.4-1
- Initial package
