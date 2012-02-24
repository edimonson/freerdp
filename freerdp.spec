%define major 1
%define pkgname	FreeRDP
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A free remote desktop protocol client
Name:		freerdp
Version:	1.0.1
%if %mdkversion <= 201100 
Release:	%mkrel 2
%else
Release:	2
%endif
License:	Apache
Group:		Networking/Remote access
URL:		http://www.freerdp.com/
Source0:	https://github.com/downloads/FreeRDP/FreeRDP/%{pkgname}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	cups-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxcursor-devel
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(x11)
BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	xmlto
BuildRequires:	pkgconfig(xinerama)
Requires:	%{libname} = %{version}-%{release}
Patch0:		double_usr_libdir_path.patch

%description
FreeRDP is a fork of the rdesktop project.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q -n FreeRDP-FreeRDP-8e62721
%patch0 -p1

%build
%cmake

%make

%install
cd build/
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/%{name}/*.la
rm -rf %{buildroot}%{_libdir}/*.la

%files
%doc README
%{_bindir}/*
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/freerdp.pc
