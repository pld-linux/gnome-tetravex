Summary:	GNOME Tetravex game
Summary(pl.UTF-8):	Gra GNOME Tetravex
Name:		gnome-tetravex
Version:	3.34.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tetravex/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	d80ea0ff368aedd03f5e49c7fbf2684a
URL:		https://wiki.gnome.org/Apps/Tetravex
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.14
BuildRequires:	meson >= 0.37.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.14
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-tetravex
%{_datadir}/glib-2.0/schemas/org.gnome.Tetravex.gschema.xml
%{_datadir}/metainfo/org.gnome.Tetravex.appdata.xml
%{_desktopdir}/org.gnome.Tetravex.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Tetravex.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tetravex.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tetravex-symbolic.svg
%{_mandir}/man6/gnome-tetravex.6*
