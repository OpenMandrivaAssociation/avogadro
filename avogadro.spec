%define maj0 0
%define major 1
%define libname %mklibname %{name} %{major}
%define libOQ %mklibname %{name}_OpenQube %{maj0}
%define devname	%mklibname %{name} -d
%define abi %(echo %{version} |cut -d. -f1-2 |sed -e 's,\\.,_,g')
%define i18n_version	1.100.0

Summary:	An advanced molecular editor for chemical purposes
Name:		avogadro
Group:		System/Libraries
Version:	1.100.0
Release:	1
License:	BSD
Url:		https://www.openchemistry.org/projects/avogadro2/
Source0:	https://github.com/OpenChemistry/avogadroapp/archive/%{version}.tar.gz
Source1:	https://github.com/OpenChemistry/avogadro-i18n/archive/%{i18n_version}/avogadro-i18n-%{i18n_version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	doxygen
BuildRequires:	hdf5-devel
BuildRequires:	spglib-devel
BuildRequires:	cmake(AvogadroLibs)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Help)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(glu)
Requires:	openbabel
Requires:	python

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
%autosetup -p1 -n avogadroapp-%{version} -a1


# help cmake to find translations
ln -s ${PWD}/avogadro-i18n-%{i18n_version}/ ../avogadro-i18n

%build
%cmake \
        -DQT_VERSION=6 \
	-DENABLE_TESTING:BOOL=OFF \
	-DBUILD_DOCUMENTATION:BOOL=ON \
        -DAvogadro_ENABLE_RPC=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# more icons
for i in 64 128 256 512; do
    install -Dpm 644 avogadro/icons/%{name}2_${i}.png %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}2.png
done

%files
%doc CONTRIBUTING.md README.md
%doc %{_docdir}/AvogadroApp
%{_bindir}/%{name}2
%{_datadir}/applications/org.openchemistry.Avogadro2.desktop
%{_iconsdir}/hicolor/*/apps/%{name}2.png
%{_iconsdir}/hicolor/*/apps/org.openchemistry.Avogadro2.{png,svg}
%{_datadir}/avogadro2/i18n/avogadroapp-*.qm
%{_datadir}/avogadro2/i18n/avogadrolibs-*.qm
%{_metainfodir}/org.openchemistry.Avogadro2.metainfo.xml
