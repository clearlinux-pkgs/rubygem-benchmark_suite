#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-benchmark_suite
Version  : 1.0.0
Release  : 6
URL      : https://rubygems.org/downloads/benchmark_suite-1.0.0.gem
Source0  : https://rubygems.org/downloads/benchmark_suite-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-benchmark_suite-bin
BuildRequires : ruby
BuildRequires : rubygem-benchmark-ips
BuildRequires : rubygem-benchmark_suite
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit
Patch1: 0001-Add-helpers.patch

%description
= benchmark_suite
* http://github.com/evanphx/benchmark_suite
== DESCRIPTION:
A set of enhancements to the standard library benchmark.rb

%package bin
Summary: bin components for the rubygem-benchmark_suite package.
Group: Binaries

%description bin
bin components for the rubygem-benchmark_suite package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n benchmark_suite-1.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-benchmark_suite.gemspec
%patch1 -p1

%build
gem build rubygem-benchmark_suite.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
benchmark_suite-1.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/benchmark_suite-1.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/README.txt
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/bin/benchmark
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/lib/benchmark/suite-run.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/lib/benchmark/suite.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/lib/benchmark_suite.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark_suite-1.0.0/test/test_benchmark_suite.rb
/usr/lib64/ruby/gems/2.3.0/specifications/benchmark_suite-1.0.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/benchmark
