Name     : rubygem-benchmark_suite
Version  : 1.0.0
Release  : 5
URL      : https://rubygems.org/downloads/benchmark_suite-1.0.0.gem
Source0  : https://rubygems.org/downloads/benchmark_suite-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
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

cp -pa lib/benchmark/helpers.rb \
%{buildroot}%{gem_dir}/gems/benchmark_suite-1.0.0/lib/benchmark

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/benchmark_suite-1.0.0
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/bin/benchmark
/usr/lib64/ruby/gems/2.2.0/cache/benchmark_suite-1.0.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/SimpleReport/cdesc-SimpleReport.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/SimpleReport/end-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/SimpleReport/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/SimpleReport/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/add_report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/cdesc-Suite.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/create-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/current-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/display-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/quiet%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/quiet%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/report-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/reports-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/running-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/warming-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/Suite/warmup_stats-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/Benchmark/cdesc-Benchmark.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/BenchmarkSuite/cdesc-BenchmarkSuite.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/benchmark_suite-1.0.0/ri/page-README_txt.ri
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/README.txt
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/bin/benchmark
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/lib/benchmark/helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/lib/benchmark/suite-run.rb
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/lib/benchmark/suite.rb
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/lib/benchmark_suite.rb
/usr/lib64/ruby/gems/2.2.0/gems/benchmark_suite-1.0.0/test/test_benchmark_suite.rb
/usr/lib64/ruby/gems/2.2.0/specifications/benchmark_suite-1.0.0.gemspec
