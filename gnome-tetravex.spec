Summary:	GNOME Tetravex game
Summary(pl.UTF-8):	Gra GNOME Tetravex
Name:		gnome-tetravex
Version:	3.38.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-tetravex/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	0769bfaa57a82b95a464961a43d31073
URL:		https://wiki.gnome.org/Apps/Tetravex
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gtk+3-devel >= 3.22.23
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.46.3
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.42.0
Requires:	glib2 >= 1:2.42.0
Requires:	gtk+3 >= 3.22.23
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
%meson build \
	-Dbuild_cli=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# gnome-tetravex and gnome-tetravex-gui domains
%find_lang %{name} --with-gnome --all-name

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
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-tetravex
%attr(755,root,root) %{_bindir}/gnome-tetravex-cli
%{_datadir}/dbus-1/services/org.gnome.Tetravex.service
%{_datadir}/glib-2.0/schemas/org.gnome.Tetravex.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.TetravexCli.gschema.xml
%{_datadir}/metainfo/org.gnome.Tetravex.appdata.xml
%{_desktopdir}/org.gnome.Tetravex.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tetravex.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tetravex-symbolic.svg
%{_mandir}/man6/gnome-tetravex.6*
%{_mandir}/man6/gnome-tetravex-cli.6*
