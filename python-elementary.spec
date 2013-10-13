Summary:	Elementary bindings for Python
Name:		python-elementary
Version:	1.7.0
Release:	1
Group:		Graphical desktop/Enlightenment
License:	GPLv2
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2

#uildRequires:	pkgconfig(eina)
#uildRequires:	pkgconfig(elementary)
#uildRequires:	pkgconfig(evas)
#uildRequires:	pkgconfig(python-evas)
#uildRequires:	python-cython

%description
Python support files for Elementary.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python

%description devel
Development files for the Python wrapper for the Elementary libraries.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
chmod -R +x %{buildroot}/%{_datadir}/%{name}/examples/

%files
%doc README
%{py_platsitedir}/elementary/*

%files devel
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

