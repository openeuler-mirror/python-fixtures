%bcond_without tests

Name:           python-fixtures
Version:        3.0.0
Release:        16
Summary:        A python contract for writing reusable state / support logic tests
License:        ASL 2.0 or BSD
URL:            https://launchpad.net/python-fixtures
Source0:        https://pypi.python.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
#Refer: https://github.com/testing-cabal/fixtures/commit/fe830674abd4926d96d38f9992f3e31b00cd891a
Patch0000:      fix-test_monkeypatch-failed.patch
BuildArch:      noarch

%description
Fixtures is a python contract that provides reusable state / support logic
for unit testing. It includes some helper and adaptation logic to write your
own fixtures using the fixtures contract.

%package -n python3-fixtures
Summary:        A python3 contract for reusable state / support logic
BuildArch:      noarch
BuildRequires:  python3-devel python3-pbr >= 0.11
%if %{with tests}
BuildRequires:  python3-mock
BuildRequires:  python3-testtools >= 0.9.22
%endif
Requires:       python3-testtools >= 0.9.22 python3-six
%{?python_provide:%python_provide python3-fixtures}

%description -n python3-fixtures
Fixtures is a python3 contract that provides reusable state / support logic
for unit testing. It includes some helper and adaptation logic to write your
own fixtures using the fixtures contract.

%prep
%autosetup -n fixtures-%{version} -p1

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} -m testtools.run fixtures.test_suite
%endif

%files -n python3-fixtures
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python3_sitelib}/fixtures
%{python3_sitelib}/fixtures-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Apr 24 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 3.0.0-16
- active build with/without test

* Fri Apr 1 2022 caodongxia <caodongxia@huawei.com> - 3.0.0-15
- Fix test_monkeypatch failed due to python3.10

* Tue Sep 29 2020 liuweibo <liuweibo10@huawei.com> - 3.0.0-14
- Fix Source0

* Mon Aug 10 2020 lingsheng <lingsheng@huawei.com> - 3.0.0-13
- Remove python2-fixtures subpackage

* Mon Nov 25 2019 Ling Yang <lingyang2@huawei.com> - 3.0.0-12
- Package init
