# Generated from chef-zero-2.0.2.gem by gem2rpm -*- rpm-spec -*-

%global gem_name chef-zero

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes
Group: Development/Languages
License: Apache 2.0
URL: http://www.opscode.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(mixlib-log)
Requires: rubygem(hashie)
Requires: rubygem(json)
Requires: rubygem(rack)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%{!?el6:BuildRequires: rubygem(rspec)}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Self-contained, easy-setup, fast-start in-memory Chef server for testing and
solo setup purposes.

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

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
%if %{?el6}0
# spec is too old; need RSpec2
%else
pushd .%{gem_instdir}
rspec
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/chef-zero
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/spec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile

%changelog
* Thu Mar 20 2014 Julian C. Dunn <jdunn@aquezada.com> - 2.0.2-1
- Initial package