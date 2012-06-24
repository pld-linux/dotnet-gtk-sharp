# TODO: fix perl stuff?
Summary:	.NET language bindings for Gtk+ and GNOME
Summary(pl):	Wi�zania Gtk+ oraz GNOME dla .NET
Name:		gtk-sharp
Version:	0.8
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	ftp://ftp.sf.net/pub/sourceforge/gtk-sharp/%{name}-%{version}.tar.gz
URL:		http://gtk-sharp.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgda-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomeui >= 2.0.0
#BuildRequires:	libgnomedb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Gtk+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi�zania dla .NET do bibliotek z Gtk+2 oraz
GNOME2.

%package devel
Summary:	Development part of GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%description devel -l pl
Narz�dzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystaj�cych z GTK#.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl
mv -f $RPM_BUILD_ROOT%{_datadir}/perl5/* $RPM_BUILD_ROOT%{_libdir}/perl5/site_perl

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gconfsharp-schemagen*
%{_libdir}/*.dll
%{_libdir}/libgtksharpglue.*

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*
%{_datadir}/gapi
%{_libdir}/perl5/site_perl/*
%{_examplesdir}/%{name}-%{version}
