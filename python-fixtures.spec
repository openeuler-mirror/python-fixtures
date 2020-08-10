Name:           python-fixtures
Version:        3.0.0
Release:        13
Summary:        A python contract for writing reusable state / support logic tests
License:        ASL 2.0 or BSD
URL:            https://launchpad.net/python-fixtures
Source0:        http://pypi.python.org/packages/source/f/fixtures/fixtures-%{version}.tar.gz
BuildArch:      noarch

%description
Fixtures is a python contract that provides reusable state / support logic
for unit testing. It includes some helper and adaptation logic to write your
own fixtures using the fixtures contract.

%package -n python3-fixtures
Summary:        A python3 contract for reusable state / support logic
BuildArch:      noarch
BuildRequires:  python3-devel python3-pbr >= 0.11 python3-mock python3-testtools >= 0.9.22
Requires:       python3-testtools >= 0.9.22 python3-six
%{?python_provide:%python_provide python3-fixtures}

%description -n python3-fixtures
Fixtures is a python3 contract that provides reusable state / support logic
for unit testing. It includes some helper and adaptation logic to write your
own fixtures using the fixtures contract.

%prep
%autosetup -n fixtures-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m testtools.run fixtures.test_suite

%files -n python3-fixtures
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python3_sitelib}/fixtures
%{python3_sitelib}/fixtures-%{version}-py?.?.egg-info

%changelog
* Mon Aug 10 2020 lingsheng <lingsheng@huawei.com> - 3.0.0-13
- Remove python2-fixtures subpackage

* Mon Nov 25 2019 Ling Yang <lingyang2@huawei.com> - 3.0.0-12
- Package init
