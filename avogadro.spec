%define	maj0	0
%define major	1
%define libname %mklibname %{name} %{major}
%define	libOQ	%mklibname %{name}_OpenQube %{maj0}
%define	devname	%mklibname %{name}avogadro -d

Summary:	An advanced molecular editor for chemical purposes
Name:		avogadro
Group:		System/Libraries
Version:	1.1.0
Release:	4
License:	GPLv2
Url:		http://avogadro.openmolecules.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		avogadro-1.1.0-qtprefix.patch
Patch1:		avogadro-1.1.0-textrel.patch
Patch2:		avogadro-1.1.0-no-strip.patch

BuildRequires:	cmake >= 2.6.0
BuildRequires:	docbook-utils
BuildRequires:	python-sip
BuildRequires:	qt4-linguist
BuildRequires:	boost-devel
BuildRequires:	python-numpy-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(openbabel-2.0)
BuildRequires:	pkgconfig(python)

%description
An advanced molecular editor designed for cross-platform use
in computational chemistry,molecular modeling, bioinformatics,
materials science,and related areas, which offers flexible
rendering and a powerful plugin architecture.

%package -n %{libname}
Summary:	Shared libraries for Avogadro
Group:		System/Libraries

%description -n %{libname}
Libraries for Avogadro molecular editor.

%package -n %{libOQ}
Summary:	Shared libraries for Avogadro
Group:		System/Libraries
Conflicts:	%{_lib}avogadro1 < 1.1.0-3

%description -n %{libOQ}
Libraries for Avogadro molecular editor.

%package -n %{devname}
Summary:	Development files for Avogadro
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libOQ} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 1.1.0-3

%description -n %{devname}
Development Avogadro files.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

%build
%cmake \
	-DENABLE_GLSL:BOOL=ON \
	-DENABLE_PYTHON:BOOL=ON
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_bindir}/avopkg
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/libavogadro/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/1_1/
%{_libdir}/%{name}/1_1/colors
%{_libdir}/%{name}/1_1/extensions
%{_libdir}/%{name}/1_1/engines
%{_libdir}/%{name}/1_1/tools
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/avopkg.1*
# should this be a separate python pkg
%{python_sitearch}/Avogadro.so

%files -n %{libname}
%{_libdir}/libavogadro.so.%{major}*

%files -n %{libOQ}
%{_libdir}/libavogadro_OpenQube.so.%{maj0}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libavogadro.so
%{_libdir}/libavogadro_OpenQube.so
%{_libdir}/%{name}/*.cmake
%{_libdir}/%{name}/1_1/*.cmake
%{_libdir}/%{name}/1_1/cmake/
%{qt4dir}/mkspecs/features/%{name}.prf
%{_libdir}/pkgconfig/avogadro.pc

