Summary:	GNOME Tetravex game
Summary(pl.UTF-8):	Gra GNOME Tetravex
Name:		gnome-tetravex
Version:	3.16.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tetravex/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	bbb796e3d2576e11d6c1a127ac6959db
URL:		https://wiki.gnome.org/Apps/Tetravex
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.13.4
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.24
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.13.4
Requires:	hicolor-icon-theme
Provides:	gnome-games-gnotravex = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnotravex < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Tetravex is a simple puzzle where pieces must be positioned so
that the same numbers are touching each other.

%description -l pl.UTF-8
GNOME Tetravex to prosta układanka, w której kawałki muszą być ułożone
tak, aby te same liczby się stykały.

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
%{_desktopdir}/gnome-tetravex.desktop
%{_iconsdir}/HighContrast/*x*/apps/gnome-tetravex.png
%{_iconsdir}/hicolor/*x*/apps/gnome-tetravex.png
%{_iconsdir}/hicolor/scalable/apps/gnome-tetravex.svg
%{_mandir}/man6/gnome-tetravex.6*
