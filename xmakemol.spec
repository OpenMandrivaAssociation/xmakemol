%define name	xmakemol
%define version 5.15
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Simple XYZ molecule editor and GL viewer
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/xmakemol/%{name}-%{version}.tar.bz2
URL:		http://vegemite.chem.nottingham.ac.uk/~xmakemol/
License:	GPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel xpm-devel MesaGLU-devel lesstif-devel mesaglw-devel

%description
XMakemol can be used to view and manipulate atomic and molecular data given in
xyz format.

XMakemol can produce output in PostScript (black and white or colour)and in xpm
format (which can be translated to gif format using xpmtoppm and ppmtogif).

XMakemol can also produce a series of xpm files which can be translated into an
animated gif file using the bundled utility xmake_anim.pl (formerly
gmake_anim.pl).

%prep
%setup -q
perl -p -i -e 's/-O2/$RPM_OPT_FLAGS/g' Makefile

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
cp xmake_anim.pl.1 %buildroot/%_mandir/man1

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=XMakeMol
Comment=Simple XYZ molecule editor and GL viewer
Exec=%{_bindir}/%{name} 
Icon=chemistry_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Motif;Education;Science;Chemistry;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS PROBLEMS ToDo.txt 
%{_bindir}/%name
%{_bindir}/xmake_anim.pl
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
