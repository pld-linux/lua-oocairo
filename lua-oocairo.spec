Summary:	This module provides access to the Cairo vector graphics library from within Lua
Summary(hu.UTF-8):	Ezzel a modullal a Cairo grafikus könyvtárhoz férhetsz hozzá Lua-ból
Name:		lua-oocairo
Version:	1.2
Release:	0.1
License:	MIT
Group:		Development/Languages
Source0:	http://www.daizucms.org/lua/library/oocairo/download/%{name}-%{version}.tar.gz
# Source0-md5:	db932466e55228332875e24aeefbfb01
URL:		http://www.daizucms.org/lua/library/oocairo/
BuildRequires:	cairo-devel
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides access to the Cairo vector graphics library from
within Lua.

%description -l hu.UTF-8
Ezzel a modullal a Cairo grafikus könyvtárhoz férhetsz hozzá Lua-ból.

%prep
%setup -q
%{__sed} -i "s@lua5\.1@lua51@g ; s@^\(LIBTOOL :=.*\)@\1 --tag=CC@ ; s@^PREFIX.*@PREFIX=%{_prefix}@" Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/lua/5.1
install -d $RPM_BUILD_ROOT%{_mandir}/man3
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/images
install .libs/liblua-oocairo.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/lua/5.1/oocairo.so
install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install examples/*.lua $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/images/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/images


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{_libdir}/lua/5.1/oocairo.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/images
%{_examplesdir}/%{name}-%{version}/*.lua
%{_examplesdir}/%{name}-%{version}/images/*
