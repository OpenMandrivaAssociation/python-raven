Name:           python3-raven
Version:        5.10.2
Release:        1
Summary:        Python client for Sentry
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/raven/
Source0:        http://pypi.python.org/packages/source/r/raven/raven-%{version}.tar.gz
Patch0:         raven-use-system-cacert.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django,
and Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%prep
%setup -q -n raven-%{version}
%patch0 -p1

rm raven/data/cacert.pem
rmdir raven/data

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot}

%check
#Disable check for now because of missing dependency pytest-timeout
#python3 setup.py test

%files
%doc README.rst LICENSE
%{_bindir}/raven
%{py3_puresitedir}/*

