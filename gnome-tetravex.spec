Summary:	GNOME Tetravex
Name:		gnome-tetravex
Version:	3.12.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tetravex/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	e4e0580daad31fbe97fe76bdf32918af
URL:		https://wiki.gnome.org/Apps/Tetravex
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Provides:	gnome-games-gnotravex = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnotravex < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetravex is a simple puzzle where pieces must be positioned so that
the same numbers are touching each other.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-tetravex
%{_datadir}/appdata/gnome-tetravex.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.tetravex.gschema.xml
#%{_datadir}/gnome-tetravex
%{_desktopdir}/gnome-tetravex.desktop
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man6/gnome-tetravex.6*

