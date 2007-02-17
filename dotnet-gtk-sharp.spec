#
# Conditional build:
%bcond_with	gda	# don't build gda binding
%bcond_without	gnome	# don't build GNOME (and dependent) bindings
#
%define		gtkhtml_soversion	%(/bin/ls %{_libdir}/libgtkhtml-3.8.so.* 2>/dev/null | /usr/bin/head -n 1 | /bin/awk '{ split($1,v,"."); print v[4]; }')
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.mono
Summary:	.NET language bindings for GTK+ and GNOME
Summary(pl.UTF-8):	Wiązania GTK+ oraz GNOME dla .NET
Name:		dotnet-gtk-sharp
Version:	1.0.10
Release:	8
License:	LGPL
Group:		Libraries
#Source0Download: http://go-mono.com/sources/
Source0:	http://go-mono.com/sources/gtk-sharp/gtk-sharp-%{version}.tar.gz
# Source0-md5:	e21fb3c5a39374f86ba70b926311a6d0
Patch0:		%{name}-gtkhtml.patch
Patch1:		%{name}-mint.patch
Patch2:		%{name}-am.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	libart_lgpl-devel >= 2.2.0
%{?with_gda:BuildRequires:	libgda-devel >= 1.0.0}
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp >= 1.0.2
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
%if %{with gnome}
BuildRequires:	gtkhtml-devel >= 3.8.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
%{?with_gda:BuildRequires:	libgnomedb-devel >= 1.0.0}
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
# depends on GNOME (vfs, printui) in PLD
BuildRequires:	librsvg-devel >= 2.4.0
BuildRequires:	vte-devel >= 0.11.10
%endif
Requires:	mono >= 1.0.2
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

%package gnome
Summary:	.NET language bindings for GNOME libraries
Summary(pl.UTF-8):	Wiązania .NET dla bibliotek GNOME
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
.NET language bindings for GNOME libraries.

%description gnome -l pl.UTF-8
Wiązania .NET dla bibliotek GNOME.

%package gnome-devel
Summary:	.NET language bindings for GNOME libraries - development files
Summary(pl.UTF-8):	Wiązania .NET dla bibliotek GNOME - pliki programistyczne
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
.NET language bindings for GNOME libraries - development files.

%description gnome-devel -l pl.UTF-8
Wiązania .NET dla bibliotek GNOME - pliki programistyczne.

%package gnome-static
Summary:	.NET language bindings for GNOME libraries - static libraries
Summary(pl.UTF-8):	Wiązania .NET dla bibliotek GNOME - static libraries
Group:		Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
.NET language bindings for GNOME libraries - static libraries.

%description gnome-static -l pl.UTF-8
Wiązania .NET dla bibliotek GNOME - static libraries.

%package gda
Summary:	.NET language bindings for GDA library
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gda
.NET language bindings for GDA library.

%description gda -l pl.UTF-8
Wiązania .NET dla biblioteki GDA.

%package gda-devel
Summary:	.NET language bindings for GDA library - development files
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GDA - pliki programistyczne
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gda = %{version}-%{release}

%description gda-devel
.NET language bindings for GDA library - development files.

%description gda-devel -l pl.UTF-8
Wiązania .NET dla biblioteki GDA - pliki programistyczne.

%package gnomedb
Summary:	.NET language bindings for GNOME-DB library
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GNOME-DB
Group:		Libraries
Requires:	%{name}-gda = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnomedb
.NET language bindings for GNOME-DB library.

%description gnomedb -l pl.UTF-8
Wiązania .NET dla biblioteki GNOME-DB.

%package gnomedb-devel
Summary:	.NET language bindings for GNOME-DB library - development files
Summary(pl.UTF-8):	Wiązania .NET dla biblioteki GNOME-DB - pliki programistyczne
Group:		Libraries
Requires:	%{name}-gda-devel = %{version}-%{release}
Requires:	%{name}-gnome-devel = %{version}-%{release}
Requires:	%{name}-gnomedb = %{version}-%{release}

%description gnomedb-devel
.NET language bindings for GNOME-DB library - development files.

%description gnomedb-devel -l pl.UTF-8
Wiązania .NET dla biblioteki GNOME-DB - pliki programistyczne.

%prep
%setup -q -n gtk-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
%doc README
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
%{_prefix}/lib/mono/gac/art-sharp
%{_prefix}/lib/mono/gac/atk-sharp
%{_prefix}/lib/mono/gac/gdk-sharp
%{_prefix}/lib/mono/gac/glade-sharp
%{_prefix}/lib/mono/gac/glib-sharp
%{_prefix}/lib/mono/gac/gtk-sharp
%{_prefix}/lib/mono/gac/pango-sharp

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%dir %{_prefix}/lib/mono/gtk-sharp
%{_prefix}/lib/mono/gtk-sharp/art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/glade-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/pango-sharp.dll
%dir %{_datadir}/gapi
%{_datadir}/gapi/art-*.xml
%{_datadir}/gapi/atk-api.xml
%{_datadir}/gapi/gdk-*.xml
%{_datadir}/gapi/glade-api.xml
%{_datadir}/gapi/gtk-*.xml
%{_datadir}/gapi/pango-api.xml
%{_pkgconfigdir}/art-sharp.pc
%{_pkgconfigdir}/gapi.pc
%{_pkgconfigdir}/glade-sharp.pc
%{_pkgconfigdir}/gtk-sharp.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdksharpglue.a
%{_libdir}/libgladesharpglue.a
%{_libdir}/libglibsharpglue.a
%{_libdir}/libgtksharpglue.a
%{_libdir}/libpangosharpglue.a

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen*
%attr(755,root,root) %{_libdir}/libgnomesharpglue.so
%{_libdir}/libgnomesharpglue.la
%{_prefix}/lib/mono/gac/gconf-sharp
%{_prefix}/lib/mono/gac/gconf-sharp-peditors
%{_prefix}/lib/mono/gac/gnome-sharp
%{_prefix}/lib/mono/gac/gtkhtml-sharp
%{_prefix}/lib/mono/gac/rsvg-sharp
%{_prefix}/lib/mono/gac/vte-sharp

%files gnome-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp/gnome-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/gtkhtml-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/rsvg-sharp.dll
%{_prefix}/lib/mono/gtk-sharp/vte-sharp.dll
%{_datadir}/gapi/gnome-api.xml
%{_datadir}/gapi/gtkhtml-api.xml
%{_datadir}/gapi/rsvg-api.xml
%{_datadir}/gapi/vte-api.xml
%{_pkgconfigdir}/gconf-sharp.pc
%{_pkgconfigdir}/gnome-sharp.pc
%{_pkgconfigdir}/gtkhtml-sharp.pc
%{_pkgconfigdir}/rsvg-sharp.pc
%{_pkgconfigdir}/vte-sharp.pc

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

%if %{with gnome} && %{with gda}
%files gnomedb
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gnomedb-sharp

%files gnomedb-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp/gnomedb-sharp.dll
%{_datadir}/gapi/gnomedb-api.xml
%{_pkgconfigdir}/gnomedb-sharp.pc
%endif
