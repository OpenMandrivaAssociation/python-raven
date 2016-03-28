Name:           python-raven
Version:        5.11.2
Release:        1
Summary:        Python client for Sentry
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/raven/
Source0:        http://pypi.python.org/packages/source/r/raven/raven-%{version}.tar.gz
Patch0:         raven-use-system-cacert.patch
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools

%description
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django,
and Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%package -n python2-raven
Summary:	Python 2 client for sentry
Group:		Development/Python

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

cp -a . %{py2dir}

%build

pushd %py2dir
python2 setup.py build
popd

python setup.py build


%install

pushd %py2dir
python2 setup.py install --skip-build --root=%{buildroot}
popd

python setup.py install --skip-build --root=%{buildroot}

%check
#Disable check for now because of missing dependency pytest-timeout
#python3 setup.py test

%files
%doc README.rst LICENSE
%{_bindir}/raven
%{py_puresitedir}/*

%files -n python2-raven
%doc README.rst LICENSE
%{py2_puresitedir}/*

