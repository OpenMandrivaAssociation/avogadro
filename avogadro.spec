
%define major 1
%define libname %mklibname %name %major

Name:           avogadro
Summary:        An advanced molecular editor for chemical purposes
Group:          System/Libraries
Version:        1.0.1
Release:        %mkrel 3
License:        GPLv2
URL:            http://avogadro.openmolecules.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		avogadro-1.0.1-fix-build-with-newer-sip.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  cmake >= 2.6.0
BuildRequires:  qt4-devel
BuildRequires:  qt4-linguist
BuildRequires:  eigen2 >= 2.0.9
BuildRequires:  openbabel-devel >= 2.2.3
BuildRequires:  boost-devel >= 1.35
BuildRequires:  glew-devel >= 1.5.0
BuildRequires:  docbook-utils
BuildRequires:  python-sip
BuildRequires:  python-numpy-devel
Requires:	%libname = %{version}-%{release}

%description
An advanced molecular editor designed for cross-platform use
in computational chemistry,molecular modeling, bioinformatics,
materials science,and related areas, which offers flexible
rendering and a powerful plugin architecture.

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/%name
%{_bindir}/avopkg
%{_datadir}/%name
%{_datadir}/pixmaps/%name-icon.png
%{_datadir}/applications/%name.desktop
%{_mandir}/man1/%name.1*
%{_mandir}/man1/avopkg.1*
%{python_sitelib}/Avogadro.so
%{_datadir}/libavogadro/
%dir %{_libdir}/%name/
%dir %{_libdir}/%name/1_0/
%{_libdir}/%name/1_0/colors
%{_libdir}/%name/1_0/extensions
%{_libdir}/%name/1_0/engines
%{_libdir}/%name/1_0/tools


#--------------------------------------------------------------------
%package -n %libname
Summary:        Shared libraries for Avogadro
Group:          System/Libraries

%description -n %libname
Libraries for Avogadro molecular editor.

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libavogadro.so.%{major}*


#--------------------------------------------------------------------
%package devel
Summary:        Development files for Avogadro
Group:          Development/C++
Requires:	%libname = %{version}-%{release}

%description devel
Development Avogadro files.

%files devel
%defattr(-,root,root,-)
%{_includedir}/%name
%{_libdir}/libavogadro.so
%{_libdir}/%name/*.cmake
%{_libdir}/%name/1_0/*.cmake
%{_libdir}/%name/1_0/cmake/
%dir %{qt4dir}/mkspecs/features/
%{qt4dir}/mkspecs/features/%name.prf


#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
%{cmake_qt4}\
	%{?ENABLE_TESTS} \
	-DENABLE_GLSL:BOOL=ON \
	-DENABLE_PYTHON:BOOL=ON

%make

%install
rm -rf %buidroot
%makeinstall_std -C build


%clean
rm -rf %buildroot
