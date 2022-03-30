#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		polib
%define		egg_name	polib
%define		pypi_name	polib
Summary:	A library to parse and manage gettext catalogs
Name:		python-%{pypi_name}
Version:	1.0.7
Release:	7
License:	MIT
Source0:	http://bitbucket.org/izi/polib/get/%{version}.tar.gz
# Source0-md5:	270110a7010425738e9a08832c5cba4f
Group:		Libraries/Python
URL:		http://bitbucket.org/izi/polib/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polib allows you to manipulate, create, modify gettext files (pot, po
and mo files). You can load existing files, iterate through it's
entries, add, modify entries, comments or metadata, etc... or create
new po files from scratch.

polib provides a simple and pythonic API, exporting only three
convenience functions 'pofile', 'mofile' and 'detect_encoding', and
the 4 core classes: POFile, MOFile, POEntry and MOEntry for creating
new files/entries.

%package -n python3-%{pypi_name}
Summary:	A library to parse and manage gettext catalogs
Group:		Libraries/Python

%description -n python3-%{pypi_name}
polib allows you to manipulate, create, modify gettext files (pot, po
and mo files). You can load existing files, iterate through it's
entries, add, modify entries, comments or metadata, etc... or create
new po files from scratch.

polib provides a simple and pythonic API, exporting only three
convenience functions 'pofile', 'mofile' and 'detect_encoding', and
the 4 core classes: POFile, MOFile, POEntry and MOEntry for creating
new files/entries.

%prep
%setup -qc
mv izi-polib-d75ce6dbbc2a/* .

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.cpython-*.pyc
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
