%define bdbv 4.8.30
%global selinux_variants mls strict targeted

%if 0%{?_no_gui:1}
%define _buildqt 0
%define buildargs --with-gui=no
%else
%define _buildqt 1
%if 0%{?_use_qt4}
%define buildargs --with-qrencode --with-gui=qt4
%else
%define buildargs --with-qrencode --with-gui=qt5
%endif
%endif

Name:		n33bcoin
Version:	0.12.0
Release:	2%{?dist}
Summary:	Peer to Peer Cryptographic Currency

Group:		Applications/System
License:	MIT
URL:		https://n33bcoin.org/
Source0:	https://n33bcoin.org/bin/n33bcoin-core-%{version}/n33bcoin-%{version}.tar.gz
Source1:	http://download.oracle.com/berkeley-db/db-%{bdbv}.NC.tar.gz

Source10:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/contrib/debian/examples/n33bcoin.conf

#man pages
Source20:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/doc/man/n33bcoind.1
Source21:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/doc/man/n33bcoin-cli.1
Source22:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/doc/man/n33bcoin-qt.1

#selinux
Source30:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/contrib/rpm/n33bcoin.te
# Source31 - what about n33bcoin-tx and bench_n33bcoin ???
Source31:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/contrib/rpm/n33bcoin.fc
Source32:	https://raw.githubusercontent.com/n33bcoin/n33bcoin/v%{version}/contrib/rpm/n33bcoin.if

Source100:	https://upload.wikimedia.org/wikipedia/commons/4/46/N33Bcoin.svg

%if 0%{?_use_libressl:1}
BuildRequires:	libressl-devel
%else
BuildRequires:	openssl-devel
%endif
BuildRequires:	boost-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	autoconf automake libtool
BuildRequires:	libevent-devel


Patch0:		n33bcoin-0.12.0-libressl.patch


%description
N33Bcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of n33bcoins is carried out collectively by the network.

%if %{_buildqt}
%package core
Summary:	Peer to Peer Cryptographic Currency
Group:		Applications/System
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
%if 0%{?_use_qt4}
BuildRequires:	qt-devel
%else
BuildRequires:	qt5-qtbase-devel
# for /usr/bin/lrelease-qt5
BuildRequires:	qt5-linguist
%endif
BuildRequires:	protobuf-devel
BuildRequires:	qrencode-devel
BuildRequires:	%{_bindir}/desktop-file-validate
# for icon generation from SVG
BuildRequires:	%{_bindir}/inkscape
BuildRequires:	%{_bindir}/convert

%description core
N33Bcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of n33bcoins is carried out collectively by the network.

This package contains the Qt based graphical client and node. If you are looking
to run a N33Bcoin wallet, this is probably the package you want.
%endif


%package libs
Summary:	N33Bcoin shared libraries
Group:		System Environment/Libraries

%description libs
This package provides the n33bcoinconsensus shared libraries. These libraries
may be used by third party software to provide consensus verification
functionality.

Unless you know need this package, you probably do not.

%package devel
Summary:	Development files for n33bcoin
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files and static library for the
n33bcoinconsensus shared library. If you are developing or compiling software
that wants to link against that library, then you need this package installed.

Most people do not need this package installed.

%package server
Summary:	The n33bcoin daemon
Group:		System Environment/Daemons
Requires:	n33bcoin-utils = %{version}-%{release}
Requires:	selinux-policy policycoreutils-python
Requires(pre):	shadow-utils
Requires(post):	%{_sbindir}/semodule %{_sbindir}/restorecon %{_sbindir}/fixfiles %{_sbindir}/sestatus
Requires(postun):	%{_sbindir}/semodule %{_sbindir}/restorecon %{_sbindir}/fixfiles %{_sbindir}/sestatus
BuildRequires:	systemd
BuildRequires:	checkpolicy
BuildRequires:	%{_datadir}/selinux/devel/Makefile

%description server
This package provides a stand-alone n33bcoin-core daemon. For most users, this
package is only needed if they need a full-node without the graphical client.

Some third party wallet software will want this package to provide the actual
n33bcoin-core node they use to connect to the network.

If you use the graphical n33bcoin-core client then you almost certainly do not
need this package.

%package utils
Summary:	N33Bcoin utilities
Group:		Applications/System

%description utils
This package provides several command line utilities for interacting with a
n33bcoin-core daemon.

The n33bcoin-cli utility allows you to communicate and control a n33bcoin daemon
over RPC, the n33bcoin-tx utility allows you to create a custom transaction, and
the bench_n33bcoin utility can be used to perform some benchmarks.

This package contains utilities needed by the n33bcoin-server package.


%prep
%setup -q
%patch0 -p1 -b .libressl
cp -p %{SOURCE10} ./n33bcoin.conf.example
tar -zxf %{SOURCE1}
cp -p db-%{bdbv}.NC/LICENSE ./db-%{bdbv}.NC-LICENSE
mkdir db4 SELinux
cp -p %{SOURCE30} %{SOURCE31} %{SOURCE32} SELinux/


%build
CWD=`pwd`
cd db-%{bdbv}.NC/build_unix/
../dist/configure --enable-cxx --disable-shared --with-pic --prefix=${CWD}/db4
make install
cd ../..

./autogen.sh
%configure LDFLAGS="-L${CWD}/db4/lib/" CPPFLAGS="-I${CWD}/db4/include/" --with-miniupnpc --enable-glibc-back-compat %{buildargs}
make %{?_smp_mflags}

pushd SELinux
for selinuxvariant in %{selinux_variants}; do
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile
	mv n33bcoin.pp n33bcoin.pp.${selinuxvariant}
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd


%install
make install DESTDIR=%{buildroot}

mkdir -p -m755 %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/n33bcoind %{buildroot}%{_sbindir}/n33bcoind

# systemd stuff
mkdir -p %{buildroot}%{_tmpfilesdir}
cat <<EOF > %{buildroot}%{_tmpfilesdir}/n33bcoin.conf
d /run/n33bcoind 0750 n33bcoin n33bcoin -
EOF
touch -a -m -t 201504280000 %{buildroot}%{_tmpfilesdir}/n33bcoin.conf

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cat <<EOF > %{buildroot}%{_sysconfdir}/sysconfig/n33bcoin
# Provide options to the n33bcoin daemon here, for example
# OPTIONS="-testnet -disable-wallet"

OPTIONS=""

# System service defaults.
# Don't change these unless you know what you're doing.
CONFIG_FILE="%{_sysconfdir}/n33bcoin/n33bcoin.conf"
DATA_DIR="%{_localstatedir}/lib/n33bcoin"
PID_FILE="/run/n33bcoind/n33bcoind.pid"
EOF
touch -a -m -t 201504280000 %{buildroot}%{_sysconfdir}/sysconfig/n33bcoin

mkdir -p %{buildroot}%{_unitdir}
cat <<EOF > %{buildroot}%{_unitdir}/n33bcoin.service
[Unit]
Description=N33Bcoin daemon
After=syslog.target network.target

[Service]
Type=forking
ExecStart=%{_sbindir}/n33bcoind -daemon -conf=\${CONFIG_FILE} -datadir=\${DATA_DIR} -pid=\${PID_FILE} \$OPTIONS
EnvironmentFile=%{_sysconfdir}/sysconfig/n33bcoin
User=n33bcoin
Group=n33bcoin

Restart=on-failure
PrivateTmp=true
TimeoutStopSec=120
TimeoutStartSec=60
StartLimitInterval=240
StartLimitBurst=5

[Install]
WantedBy=multi-user.target
EOF
touch -a -m -t 201504280000 %{buildroot}%{_unitdir}/n33bcoin.service
#end systemd stuff

mkdir %{buildroot}%{_sysconfdir}/n33bcoin
mkdir -p %{buildroot}%{_localstatedir}/lib/n33bcoin

#SELinux
for selinuxvariant in %{selinux_variants}; do
	install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
	install -p -m 644 SELinux/n33bcoin.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/n33bcoin.pp
done

%if %{_buildqt}
# qt icons
install -D -p share/pixmaps/n33bcoin.ico %{buildroot}%{_datadir}/pixmaps/n33bcoin.ico
install -p share/pixmaps/nsis-header.bmp %{buildroot}%{_datadir}/pixmaps/
install -p share/pixmaps/nsis-wizard.bmp %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE100} %{buildroot}%{_datadir}/pixmaps/n33bcoin.svg
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/n33bcoin16.png -w16 -h16
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/n33bcoin32.png -w32 -h32
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/n33bcoin64.png -w64 -h64
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/n33bcoin128.png -w128 -h128
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/n33bcoin256.png -w256 -h256
%{_bindir}/convert -resize 16x16 %{buildroot}%{_datadir}/pixmaps/n33bcoin256.png %{buildroot}%{_datadir}/pixmaps/n33bcoin16.xpm
%{_bindir}/convert -resize 32x32 %{buildroot}%{_datadir}/pixmaps/n33bcoin256.png %{buildroot}%{_datadir}/pixmaps/n33bcoin32.xpm
%{_bindir}/convert -resize 64x64 %{buildroot}%{_datadir}/pixmaps/n33bcoin256.png %{buildroot}%{_datadir}/pixmaps/n33bcoin64.xpm
%{_bindir}/convert -resize 128x128 %{buildroot}%{_datadir}/pixmaps/n33bcoin256.png %{buildroot}%{_datadir}/pixmaps/n33bcoin128.xpm
%{_bindir}/convert %{buildroot}%{_datadir}/pixmaps/n33bcoin256.png %{buildroot}%{_datadir}/pixmaps/n33bcoin256.xpm
touch %{buildroot}%{_datadir}/pixmaps/*.png -r %{SOURCE100}
touch %{buildroot}%{_datadir}/pixmaps/*.xpm -r %{SOURCE100}

# Desktop File - change the touch timestamp if modifying
mkdir -p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/n33bcoin-core.desktop
[Desktop Entry]
Encoding=UTF-8
Name=N33Bcoin
Comment=N33Bcoin P2P Cryptocurrency
Comment[fr]=N33Bcoin, monnaie virtuelle cryptographique pair à pair
Comment[tr]=N33Bcoin, eşten eşe kriptografik sanal para birimi
Exec=n33bcoin-qt %u
Terminal=false
Type=Application
Icon=n33bcoin128
MimeType=x-scheme-handler/n33bcoin;
Categories=Office;Finance;
EOF
# change touch date when modifying desktop
touch -a -m -t 201511100546 %{buildroot}%{_datadir}/applications/n33bcoin-core.desktop
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/n33bcoin-core.desktop

# KDE protocol - change the touch timestamp if modifying
mkdir -p %{buildroot}%{_datadir}/kde4/services
cat <<EOF > %{buildroot}%{_datadir}/kde4/services/n33bcoin-core.protocol
[Protocol]
exec=n33bcoin-qt '%u'
protocol=n33bcoin
input=none
output=none
helper=true
listing=
reading=false
writing=false
makedir=false
deleting=false
EOF
# change touch date when modifying protocol
touch -a -m -t 201511100546 %{buildroot}%{_datadir}/kde4/services/n33bcoin-core.protocol
%endif

# man pages
install -D -p %{SOURCE20} %{buildroot}%{_mandir}/man1/n33bcoind.1
install -p %{SOURCE21} %{buildroot}%{_mandir}/man1/n33bcoin-cli.1
%if %{_buildqt}
install -p %{SOURCE22} %{buildroot}%{_mandir}/man1/n33bcoin-qt.1
%endif

# nuke these, we do extensive testing of binaries in %%check before packaging
rm -f %{buildroot}%{_bindir}/test_*

%check
make check
pushd src
srcdir=. test/n33bcoin-util-test.py
popd
qa/pull-tester/rpc-tests.py -extended

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%pre server
getent group n33bcoin >/dev/null || groupadd -r n33bcoin
getent passwd n33bcoin >/dev/null ||
	useradd -r -g n33bcoin -d /var/lib/n33bcoin -s /sbin/nologin \
	-c "N33Bcoin wallet server" n33bcoin
exit 0

%post server
%systemd_post n33bcoin.service
# SELinux
if [ `%{_sbindir}/sestatus |grep -c "disabled"` -eq 0 ]; then
for selinuxvariant in %{selinux_variants}; do
	%{_sbindir}/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/n33bcoin.pp &> /dev/null || :
done
%{_sbindir}/semanage port -a -t n33bcoin_port_t -p tcp 8332
%{_sbindir}/semanage port -a -t n33bcoin_port_t -p tcp 8333
%{_sbindir}/semanage port -a -t n33bcoin_port_t -p tcp 18332
%{_sbindir}/semanage port -a -t n33bcoin_port_t -p tcp 18333
%{_sbindir}/fixfiles -R n33bcoin-server restore &> /dev/null || :
%{_sbindir}/restorecon -R %{_localstatedir}/lib/n33bcoin || :
fi

%posttrans server
%{_bindir}/systemd-tmpfiles --create

%preun server
%systemd_preun n33bcoin.service

%postun server
%systemd_postun n33bcoin.service
# SELinux
if [ $1 -eq 0 ]; then
	if [ `%{_sbindir}/sestatus |grep -c "disabled"` -eq 0 ]; then
	%{_sbindir}/semanage port -d -p tcp 8332
	%{_sbindir}/semanage port -d -p tcp 8333
	%{_sbindir}/semanage port -d -p tcp 18332
	%{_sbindir}/semanage port -d -p tcp 18333
	for selinuxvariant in %{selinux_variants}; do
		%{_sbindir}/semodule -s ${selinuxvariant} -r n33bcoin &> /dev/null || :
	done
	%{_sbindir}/fixfiles -R n33bcoin-server restore &> /dev/null || :
	[ -d %{_localstatedir}/lib/n33bcoin ] && \
		%{_sbindir}/restorecon -R %{_localstatedir}/lib/n33bcoin &> /dev/null || :
	fi
fi

%clean
rm -rf %{buildroot}

%if %{_buildqt}
%files core
%defattr(-,root,root,-)
%license COPYING db-%{bdbv}.NC-LICENSE
%doc COPYING n33bcoin.conf.example doc/README.md doc/bips.md doc/files.md doc/multiwallet-qt.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md
%attr(0755,root,root) %{_bindir}/n33bcoin-qt
%attr(0644,root,root) %{_datadir}/applications/n33bcoin-core.desktop
%attr(0644,root,root) %{_datadir}/kde4/services/n33bcoin-core.protocol
%attr(0644,root,root) %{_datadir}/pixmaps/*.ico
%attr(0644,root,root) %{_datadir}/pixmaps/*.bmp
%attr(0644,root,root) %{_datadir}/pixmaps/*.svg
%attr(0644,root,root) %{_datadir}/pixmaps/*.png
%attr(0644,root,root) %{_datadir}/pixmaps/*.xpm
%attr(0644,root,root) %{_mandir}/man1/n33bcoin-qt.1*
%endif

%files libs
%defattr(-,root,root,-)
%license COPYING
%doc COPYING doc/README.md doc/shared-libraries.md
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%doc COPYING doc/README.md doc/developer-notes.md doc/shared-libraries.md
%attr(0644,root,root) %{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc

%files server
%defattr(-,root,root,-)
%license COPYING db-%{bdbv}.NC-LICENSE
%doc COPYING n33bcoin.conf.example doc/README.md doc/REST-interface.md doc/bips.md doc/dnsseed-policy.md doc/files.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md
%attr(0755,root,root) %{_sbindir}/n33bcoind
%attr(0644,root,root) %{_tmpfilesdir}/n33bcoin.conf
%attr(0644,root,root) %{_unitdir}/n33bcoin.service
%dir %attr(0750,n33bcoin,n33bcoin) %{_sysconfdir}/n33bcoin
%dir %attr(0750,n33bcoin,n33bcoin) %{_localstatedir}/lib/n33bcoin
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/sysconfig/n33bcoin
%attr(0644,root,root) %{_datadir}/selinux/*/*.pp
%attr(0644,root,root) %{_mandir}/man1/n33bcoind.1*

%files utils
%defattr(-,root,root,-)
%license COPYING
%doc COPYING n33bcoin.conf.example doc/README.md
%attr(0755,root,root) %{_bindir}/n33bcoin-cli
%attr(0755,root,root) %{_bindir}/n33bcoin-tx
%attr(0755,root,root) %{_bindir}/bench_n33bcoin
%attr(0644,root,root) %{_mandir}/man1/n33bcoin-cli.1*



%changelog
* Fri Feb 26 2016 Alice Wonder <buildmaster@librelamp.com> - 0.12.0-2
- Rename Qt package from n33bcoin to n33bcoin-core
- Make building of the Qt package optional
- When building the Qt package, default to Qt5 but allow building
-  against Qt4
- Only run SELinux stuff in post scripts if it is not set to disabled

* Wed Feb 24 2016 Alice Wonder <buildmaster@librelamp.com> - 0.12.0-1
- Initial spec file for 0.12.0 release

# This spec file is written from scratch but a lot of the packaging decisions are directly
# based upon the 0.11.2 package spec file from https://www.ringingliberty.com/n33bcoin/
