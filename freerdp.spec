%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define _disable_ld_no_undefined 1

Summary:	A free remote desktop protocol client
Name:		freerdp
Version:	1.0.1
Release:	1
License:	Apache
Group:		Networking/Remote access
Url:		http://freerdp.sourceforge.net/
Source0:	https://github.com/downloads/FreeRDP/FreeRDP/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(openssl)
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	libxcursor-devel
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(x11)
BuildRequires:	cmake
BuildRequires:	xmlto
BuildRequires:	docbook-style-xsl

%description
FreeRDP is a fork of the rdesktop project.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%cmake \
    -DWITH_CUPS=ON \
    -DWITH_PULSEAUDIO=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XV=ON \
    -DWITH_ALSA=OFF \
    -DWITH_CUNIT=OFF \
    -DWITH_DIRECTFB=OFF \
    -DWITH_FFMPEG=OFF \
    -DWITH_SSE2=OFF \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%make

%install
cd build
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/%{name}/*.la
rm -rf %{buildroot}%{_libdir}/*.la

%files
%doc ChangeLog LICENSE README
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/xfreerdp.1.*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/freerdp.pc
