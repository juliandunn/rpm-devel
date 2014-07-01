# Generated from ffi-yajl-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ffi-yajl

Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?dist}
Summary: Ruby FFI wrapper around YAJL 2.x
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/lamont-granquist/ffi-yajl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: ffi-yajl.gemspec.patch
Patch1: ffi-yajl.extconf.rb.patch
Patch2: ffi-yajl.vendoring.patch
Patch3: ffi-yajl.old-rspec.patch
%{!?el6:Requires: ruby(release)}
Requires: ruby(rubygems) 
Requires: rubygem(ffi)
Requires: yajl
%{!?el6:BuildRequires: ruby(release)}
BuildRequires: rubygems-devel 
%{!?el6:BuildRequires: rubygem(rspec)}
BuildRequires: rubygem(ffi)
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

# If there were programs installed:
mkdir -p %{buildroot}%{_bindir}
cp -pa ./%{_bindir}/* %{buildroot}%{_bindir}

# If there are C extensions, copy them to the extdir.
%if 0%{?fedora} >= 21
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,ffi_yajl/ext/*.so} %{buildroot}%{gem_extdir_mri}/
%else
mkdir -p %{buildroot}%{gem_extdir_mri}/lib/ffi_yajl/ext
mv %{buildroot}%{gem_instdir}/lib/ffi_yajl/ext/*.so %{buildroot}%{gem_extdir_mri}/lib/ffi_yajl/ext
%endif

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
rspec
popd

%files
%dir %{gem_instdir}
%exclude %{_bindir}/ffi-yajl-bench
%exclude %{gem_instdir}/bin/ffi-yajl-bench
%exclude %{gem_instdir}/lib/ffi_yajl/benchmark
%exclude %{gem_instdir}/lib/ffi_yajl/ext/.keep
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
* Thu Jun 26 2014 Julian C. Dunn (<jdunn@aquezada.com>) - 0.2.0-1
- Update to 0.2.0

* Sat Mar 22 2014 Julian C. Dunn (<jdunn@aquezada.com>) - 0.0.4-1
- Initial package
