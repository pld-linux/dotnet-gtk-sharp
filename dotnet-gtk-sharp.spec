#
# Conditional build:
%bcond_without	gda	# don't build gda binding
%bcond_without	gnome	# don't build GNOME (and dependent) bindings
#
%define		gtkhtml_soversion	%(/bin/ls %{_libdir}/libgtkhtml-3.6.so.* 2>/dev/null | /usr/bin/head -n 1 | /bin/awk '{ split($1,v,"."); print v[4]; }')
%define		gtkhtml_version		%(if [ -e /usr/bin/pkg-config ]; then /usr/bin/pkg-config --modversion libgtkhtml-3.6 2>/dev/null || echo 0; else echo 0; fi)
%include	/usr/lib/rpm/macros.perl
Summary:	.NET language bindings for GTK+ and GNOME
Summary(pl):	Wi±zania GTK+ oraz GNOME dla .NET
Name:		dotnet-gtk-sharp
Version:	1.0.6
Release:	3
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.go-mono.com/archive/%{version}/gtk-sharp-%{version}.tar.gz
# Source0-md5:	2651d14fe77174ab20b8af53d150ee11
Patch0:		%{name}-gtkhtml31.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-mint.patch
#Patch3:		%{name}-disable-rsvg-sample.patch
Patch4:		%{name}-pc-libdir.patch
URL:		http://gtk-sharp.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	libart_lgpl-devel >= 2.2.0
%{?with_gda:BuildRequires:	libgda-devel >= 1.0.0}
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	librsvg-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp >= 1.0.2
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
%if %{with gnome}
BuildRequires:	gtkhtml-devel >= 3.6.1
BuildRequires:	libgnomecanvas-devel >= 2.4.0
%{?with_gda:BuildRequires:	libgnomedb-devel >= 1.0.0}
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	vte-devel >= 0.11.10
%endif
%{?with_gnome:Requires:	gtkhtml = %{gtkhtml_version}}
Provides:	dotnet-gtk
Provides:	gtk-sharp
Obsoletes:	dotnet-gtk
Obsoletes:	gtk-sharp
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z GTK+2 oraz
GNOME2.

%package devel
Summary:	Development part of GTK#
Summary(pl):	Czê¶æ dla programistów GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	dotnet-gtk-devel
Provides:	gtk-sharp-devel
Obsoletes:	dotnet-gtk-devel
Obsoletes:	gtk-sharp-devel

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%description devel -l pl
Narzêdzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystaj±cych z GTK#.

%package static
Summary:	Static gtk-sharp libraries
Summary(pl):	Biblioteki statyczne gtk-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	dotnet-gtk-static
Provides:	gtk-sharp-static
Obsoletes:	dotnet-gtk-static
Obsoletes:	gtk-sharp-static

%description static
Static gtk-sharp libraries.

%description static -l pl
Biblioteki statyczne gtk-sharp.

%prep
%setup -q -n gtk-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1

# workaround for variable name
echo 'm4_pattern_allow(PKG_PATH)' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	GTKHTMLSOVERSION=%{gtkhtml_soversion}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen*
%attr(755,root,root) %{_libdir}/lib*sharpglue.so
%{_libdir}/lib*sharpglue.la
%{_libdir}/mono/gac/*

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%{_datadir}/gapi
%{_examplesdir}/%{name}-%{version}
%{_pkgconfigdir}/*
%{_libdir}/mono/gtk-sharp

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*sharpglue.a
