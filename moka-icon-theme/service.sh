PKG_VERSION=5.3.2
PKG_DOWNLOAD_URL=https://github.com/snwh/moka-icon-theme/archive/v${PKG_VERSION}.tar.gz

pkg_prebuild_hook()
{
	sudo dnf -y copr enable mkrawiec/themes
}
