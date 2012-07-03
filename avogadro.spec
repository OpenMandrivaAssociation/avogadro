%define debug_package %nil

%define major 1
%define libname %mklibname %name %major

Name:           avogadro
Summary:        An advanced molecular editor for chemical purposes
Group:          System/Libraries
Version:        1.0.3
Release:        4
License:        GPLv2
URL:            http://avogadro.openmolecules.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		avogadro-1.0.3-qtprefix.patch
Patch1:		avogadro-1.0.3-replace-qt4_automoc-with-qt4_wrap_cpp.patch
Patch2:		avogadro-1.0.3-fix-boost.patch
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
BuildRequires:	python-devel
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
%{python_sitearch}/Avogadro.so
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
%{qt4dir}/mkspecs/features/%name.prf

#--------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{cmake} \
	-DENABLE_GLSL:BOOL=ON \
	-DENABLE_PYTHON:BOOL=ON
%make

%install
rm -rf %buidroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
