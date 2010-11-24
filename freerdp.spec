%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A free remote desktop protocol client
Name:		freerdp
Version:	0.8.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Remote access
Url:		http://freerdp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/freerdp/0.8/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	cups-devel
BuildRequires:	libalsa-devel
BuildRequires:	libxcursor-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q %{name}-%{version}

%build
%configure2_5x \
	--disable-static \
	--with-sound=alsa

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}
rm -rf %{buildroot}%{_libdir}/%{name}/*.la
rm -rf %{buildroot}%{_libdir}/*.la

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/xfreerdp.1.*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/freerdp.pc
