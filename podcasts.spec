Name:           podcasts
Version:        0.7.1
Release:        1
Summary:        Listen to your favorite podcasts, right from your desktop.

License:        GPL-3.0
URL:            https://apps.gnome.org/Podcasts/
Source0: https://gitlab.gnome.org/World/podcasts/-/archive/0.7.1/podcasts-0.7.1.tar.gz

BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  glib
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-good gstreamer1-plugins-good-extras
BuildRequires:  gstreamer1-vaapi gstreamer1
BuildRequires:  rust-openssl-devel
BuildRequires:  cmake
BuildRequires:  pkgconf-pkg-config
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       gtk4
Requires:       libadwaita
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       openssl

%description



%prep
cd %{_builddir}/
git clone --recurse-submodules https://gitlab.gnome.org/World/podcasts.git
cd %{_builddir}/podcasts
git checkout f1cfdc61198c920c3be4e3a75f3c7311d0e528ce

%build
cd podcasts*
%meson --buildtype release
%meson_build -j 1


%install
cd podcasts
%meson_install

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Podcasts.desktop
%{_datadir}/dbus-1/services/org.gnome.Podcasts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Podcasts.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Podcasts*.svg
%{_datadir}/metainfo/org.gnome.Podcasts.appdata.xml
%{_datadir}/locale/

%changelog
* Mon Jun 24 2024 sunrise2011
- хуй
