%include	/usr/lib/rpm/macros.perl
Summary:	.NET language bindings for Gtk+ and GNOME
Summary(pl):	Wiązania Gtk+ oraz GNOME dla .NET
Name:		gtk-sharp
Version:	0.18
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	http://belnet.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	aa85960a335801c813b522bbc8438b2c
Patch0:		%{name}-gtkhtml31.patch
URL:		http://gtk-sharp.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkhtml-devel >= 3.0.0
BuildRequires:	libgda-devel >= 1.0.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.4.0
BuildRequires:	libgnomedb >= 1.0.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	librsvg-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:  mono-devel
BuildRequires:  ncurses-devel
BuildRequires:	rpm-perlprov
BuildRequires:	vte-devel >= 0.11.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Gtk+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wiązania dla .NET do bibliotek z Gtk+2 oraz
GNOME2.

%package devel
Summary:	Development part of GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%description devel -l pl
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z GTK#.

%package static
Summary:	Static gtk-sharp libraries
Summary(pl):	Biblioteki statyczne gtk-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk-sharp libraries.

%description static -l pl
Biblioteki statyczne gtk-sharp.

%prep
%setup -q
%patch0 -p1

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/perl5/GAPI $RPM_BUILD_ROOT%{perl_vendorlib}
cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen*
%attr(755,root,root) %{_libdir}/lib*sharpglue.so
%{_libdir}/lib*sharpglue.la
%{_libdir}/*.dll

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%{_datadir}/gapi
%{perl_vendorlib}/GAPI
%{_examplesdir}/%{name}-%{version}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*sharpglue.a
