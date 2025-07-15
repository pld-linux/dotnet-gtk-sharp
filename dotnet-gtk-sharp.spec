#
# Conditional build:
%bcond_with	gda	# GDA bindings
%bcond_without	gnome	# GNOME (and dependent) bindings
%bcond_without	gnomedb	# GNOME DB bindings [depends on gda && gnome]
%bcond_without	gtkhtml	# GTKHTML bindings
%bcond_without	librsvg	# RSVG bindings
%bcond_without	vte	# VTE bindings [depends on gnome]
#
%if %{without gda} || %{without gnome}
%undefine	with_gnomedb
%endif
%if %{without gnome}
%undefine	with_gtkhtml
%undefine	with_vte
%endif
%if %{with gtkhtml}
%define		gtkhtml_soversion	%(/bin/ls %{_libdir}/libgtkhtml-3.14.so.* 2>/dev/null | /usr/bin/head -n 1 | /bin/awk '{ split($1,v,"."); print v[4]; }')
%endif
Summary:	.NET language bindings for GTK+ and GNOME
Summary(pl.UTF-8):	Wiązania GTK+ oraz GNOME dla .NET
Name:		dotnet-gtk-sharp
Version:	1.0.10
Release:	12
License:	LGPL v2
Group:		Libraries
Source0:	http://download.mono-project.com/sources/gtk-sharp/gtk-sharp-%{version}.tar.gz
# Source0-md5:	e21fb3c5a39374f86ba70b926311a6d0
Patch0:		%{name}-gtkhtml.patch
Patch1:		%{name}-mint.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-glib.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gawk
%{?with_gtkhtml:BuildRequires:	gtkhtml3-devel >= 3.16.0}
BuildRequires:	libart_lgpl-devel >= 2.2.0
%{?with_gda:BuildRequires:	libgda-devel >= 1.0.0}
BuildRequires:	libglade2-devel >= 2.0.1
%if %{with gnome}
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
%endif
%{?with_gnomedb:BuildRequires:	libgnomedb-devel >= 1.0.0}
%{?with_librsvg:BuildRequires:	librsvg-devel >= 2.4.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp >= 1.0.2
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
%{?with_vte:BuildRequires:	vte0-devel >= 0.11.10}
Requires:	mono >= 1.0.2
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+2 and GNOME2 libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z GTK+2 oraz
GNOME2.

%package devel
Summary:	Development part of GTK#
Summary(pl.UTF-8):	Część dla programistów GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%description devel -l pl.UTF-8
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z GTK#.

%package static
Summary:	Static gtk-sharp libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtk-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-sharp libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtk-sharp.

%package art
Summary:	Art# - .NET language bindings for libart_lgpl library
Summary(pl.UTF-8):	Art# - wiązanie .NET do biblioteki libart_lgpl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libart_lgpl >= 2.2.0

%description art
Art# - .NET language bindings for libart_lgpl library.

%description art -l pl.UTF-8
Art# - wiązanie .NET do biblioteki libart_lgpl.

%package art-devel
Summary:	.NET language bindings for libart_lgpl library - development files
Summary(pl.UTF-8):	Wiązanie .NET do biblioteki libart_lgpl - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-art = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description art-devel
.NET language bindings for libart_lgpl library - development files.

%description art-devel -l pl.UTF-8
Wiązanie .NET do biblioteki libart_lgpl - pliki programistyczne.

%package gnome
Summary:	Gnome# - .NET language bindings for GNOME libraries
Summary(pl.UTF-8):	Gnome# - wiązania .NET dla bibliotek GNOME
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-art = %{version}-%{release}

%description gnome
Gnome# - .NET language bindings for GNOME libraries.

%description gnome -l pl.UTF-8
Gnome# - wiązania .NET dla bibliotek GNOME.

%package gnome-devel
Summary:	.NET language bindings for GNOME libraries - development files
Summary(pl.UTF-8):	Wiązania .NET dla bibliotek GNOME - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-art-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
.NET language bindings for GNOME libraries - development files.

%description gnome-devel -l pl.UTF-8
Wiązania .NET dla bibliotek GNOME - pliki programistyczne.

%package gnome-static
Summary:	.NET language bindings for GNOME libraries - static libraries
Summary(pl.UTF-8):	Wiązania .NET dla bibliotek GNOME - static libraries
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
.NET language bindings for GNOME libraries - static libraries.

%description gnome-static -l pl.UTF-8
Wiązania .NET dla bibliotek GNOME - static libraries.

%package gda
Summary:	Gda# - .NET language bindings for GDA library
Summary(pl.UTF-8):	Gda# - wiązania .NET dla biblioteki GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgda-devel >= 1.0.0

%description gda
Gda# - .NET language bindings for GDA library.

%description gda -l pl.UTF-8
Gda# - wiązania .NET dla biblioteki GDA.

%package gda-devel
Summary:	.NET language bindings for GDA library - development files
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GDA - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gda = %{version}-%{release}

%description gda-devel
.NET language bindings for GDA library - development files.

%description gda-devel -l pl.UTF-8
Wiązania .NET dla biblioteki GDA - pliki programistyczne.

%package gnomedb
Summary:	GnomeDB# - .NET language bindings for GNOME-DB library
Summary(pl.UTF-8):	GnomeDB# - wiązania .NET dla biblioteki GNOME-DB
Group:		Libraries
Requires:	%{name}-gda = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	libgnomedb >= 1.0.0

%description gnomedb
GnomeDB# - .NET language bindings for GNOME-DB library.

%description gnomedb -l pl.UTF-8
GnomeDB# - wiązania .NET dla biblioteki GNOME-DB.

%package gnomedb-devel
Summary:	.NET language bindings for GNOME-DB library - development files
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GNOME-DB - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-gda-devel = %{version}-%{release}
Requires:	%{name}-gnome-devel = %{version}-%{release}
Requires:	%{name}-gnomedb = %{version}-%{release}

%description gnomedb-devel
.NET language bindings for GNOME-DB library - development files.

%description gnomedb-devel -l pl.UTF-8
Wiązania .NET dla biblioteki GNOME-DB - pliki programistyczne.

%package gtkhtml
Summary:	Gtkhtml# - .NET language bindings for GtkHTML library
Summary(pl.UTF-8):	Gtkhtml# - wiązania .NET do biblioteki GtkHTML
Group:		Libraries
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	gtkhtml3 >= 3.16.0

%description gtkhtml
Gtkhtml# - .NET language bindings for GtkHTML library.

%description gtkhtml -l pl.UTF-8
Gtkhtml# - wiązania .NET do biblioteki GtkHTML.

%package gtkhtml-devel
Summary:	.NET language bindings for GtkHTML library - development files
Summary(pl.UTF-8):	Wiązania .NET do biblioteki GtkHTML - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}
Requires:	%{name}-gtkhtml = %{version}-%{release}

%description gtkhtml-devel
.NET language bindings for GtkHTML library - development files.

%description gtkhtml-devel -l pl.UTF-8
Wiązania .NET do biblioteki GtkHTML - pliki programistyczne.

%package rsvg
Summary:	Rsvg# - .NET language bindings for RSVG library
Summary(pl.UTF-8):	Rsvg# - wiązania .NET do biblioteki RSVG
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-art = %{version}-%{release}
Requires:	librsvg >= 2.4.0

%description rsvg
Rsvg# - .NET language bindings for RSVG library.

%description rsvg -l pl.UTF-8
Rsvg# - wiązania .NET do biblioteki RSVG.

%package rsvg-devel
Summary:	.NET language bindings for RSVG library - development files
Summary(pl.UTF-8):	Wiązania .NET do biblioteki RSVG - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-art-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-rsvg = %{version}-%{release}

%description rsvg-devel
.NET language bindings for RSVG library - development files.

%description rsvg-devel -l pl.UTF-8
Wiązania .NET do biblioteki RSVG - pliki programistyczne.

%package vte
Summary:	Vte# - .NET language bindings for Vte library
Summary(pl.UTF-8):	Vte# - wiązania .NET do biblioteki Vte
Group:		Libraries
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	vte0 >= 0.11.10

%description vte
Vte# - .NET language bindings for Vte library.

%description vte -l pl.UTF-8
Vte# - wiązania .NET do biblioteki Vte.

%package vte-devel
Summary:	.NET language bindings for Vte library - development files
Summary(pl.UTF-8):	Wiązania .NET do biblioteki Vte - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}
Requires:	%{name}-vte = %{version}-%{release}

%description vte-devel
.NET language bindings for Vte library - development files.

%description vte-devel -l pl.UTF-8
Wiązania .NET do biblioteki Vte - pliki programistyczne.

%package examples
Summary:	Examples for Gtk# 1.x libraries
Summary(pl.UTF-8):	Przykłady do bibliotek Gtk# 1.x
Group:		Development/Libraries

%description examples
Examples for Gtk# 1.x libraries.

%description examples -l pl.UTF-8
Przykłady do bibliotek Gtk# 1.x.

%prep
%setup -q -n gtk-sharp-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# workaround for variable name
echo 'm4_pattern_allow(PKG_PATH)' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{?with_gnome:GTKHTMLSOVERSION=%{gtkhtml_soversion}}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdksharpglue.so
%attr(755,root,root) %{_libdir}/libgladesharpglue.so
%attr(755,root,root) %{_libdir}/libglibsharpglue.so
%attr(755,root,root) %{_libdir}/libgtksharpglue.so
%attr(755,root,root) %{_libdir}/libpangosharpglue.so
%{_libdir}/libgdksharpglue.la
%{_libdir}/libgladesharpglue.la
%{_libdir}/libglibsharpglue.la
%{_libdir}/libgtksharpglue.la
%{_libdir}/libpangosharpglue.la
%{_prefix}/lib/mono/gac/atk-sharp
%{_prefix}/lib/mono/gac/gdk-sharp
%{_prefix}/lib/mono/gac/glade-sharp
%{_prefix}/lib/mono/gac/glib-sharp
%{_prefix}/lib/mono/gac/gtk-sharp
%{_prefix}/lib/mono/gac/pango-sharp

%files devel
%defattr(644,root,root,755)
%doc README.generator
%attr(755,root,root) %{_bindir}/gapi-codegen
%attr(755,root,root) %{_bindir}/gapi-fixup
%attr(755,root,root) %{_bindir}/gapi-fixup.exe
%attr(755,root,root) %{_bindir}/gapi-parser
%attr(755,root,root) %{_bindir}/gapi.pl
%attr(755,root,root) %{_bindir}/gapi2xml.pl
%attr(755,root,root) %{_bindir}/gapi_codegen.exe
%attr(755,root,root) %{_bindir}/gapi_format_xml
%attr(755,root,root) %{_bindir}/gapi_pp.pl
%dir %{_prefix}/lib/mono/gtk-sharp
%{_prefix}/lib/mono/gtk-sharp/art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/pango-sharp.dll
%dir %{_datadir}/gapi
%{_datadir}/gapi/atk-api.xml
%{_datadir}/gapi/gdk-api.xml
%{_datadir}/gapi/gdk-symbols.xml
%{_datadir}/gapi/glade-api.xml
%{_datadir}/gapi/gtk-api.xml
%{_datadir}/gapi/gtk-symbols.xml
%{_datadir}/gapi/pango-api.xml
%{_pkgconfigdir}/gapi.pc
%{_pkgconfigdir}/glade-sharp.pc
%{_pkgconfigdir}/gtk-sharp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdksharpglue.a
%{_libdir}/libgladesharpglue.a
%{_libdir}/libglibsharpglue.a
%{_libdir}/libgtksharpglue.a
%{_libdir}/libpangosharpglue.a

%files art
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/art-sharp

%files art-devel
%defattr(644,root,root,755)
%{_datadir}/gapi/art-api.xml
%{_datadir}/gapi/art-symbols.xml
%{_pkgconfigdir}/art-sharp.pc

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen.exe
%attr(755,root,root) %{_libdir}/libgnomesharpglue.so
%{_libdir}/libgnomesharpglue.la
%{_prefix}/lib/mono/gac/gconf-sharp
%{_prefix}/lib/mono/gac/gconf-sharp-peditors
%{_prefix}/lib/mono/gac/gnome-sharp

%files gnome-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp/gnome-sharp.dll
%{_datadir}/gapi/gnome-api.xml
%{_pkgconfigdir}/gconf-sharp.pc
%{_pkgconfigdir}/gnome-sharp.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnomesharpglue.a
%endif

%if %{with gda}
%files gda
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gda-sharp

%files gda-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gda-sharp.dll
%{_datadir}/gapi/gda-api.xml
%{_pkgconfigdir}/gda-sharp.pc
%endif

%if %{with gnomedb}
%files gnomedb
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gnomedb-sharp

%files gnomedb-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gnomedb-sharp.dll
%{_datadir}/gapi/gnomedb-api.xml
%{_pkgconfigdir}/gnomedb-sharp.pc
%endif

%if %{with gtkhtml}
%files gtkhtml
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gtkhtml-sharp

%files gtkhtml-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gtkhtml-sharp.dll
%{_datadir}/gapi/gtkhtml-api.xml
%{_pkgconfigdir}/gtkhtml-sharp.pc
%endif

%if %{with librsvg}
%files rsvg
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/rsvg-sharp

%files rsvg-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/rsvg-sharp.dll
%{_datadir}/gapi/rsvg-api.xml
%{_pkgconfigdir}/rsvg-sharp.pc
%endif

%if %{with vte}
%files vte
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/vte-sharp

%files vte-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/vte-sharp.dll
%{_datadir}/gapi/vte-api.xml
%{_pkgconfigdir}/vte-sharp.pc
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
