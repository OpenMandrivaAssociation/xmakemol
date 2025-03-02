Name: 	 	xmakemol
Summary: 	Simple XYZ molecule editor and GL viewer
Version: 	5.16
Release: 	9

Source:		http://savannah.nongnu.org/download/xmakemol/%{name}-%{version}.tar.gz
Patch0:		xmakemol-compile.patch
URL:		https://vegemite.chem.nottingham.ac.uk/~xmakemol/
License:	GPL
Group:		Sciences/Chemistry
BuildRequires:	pkgconfig(x11)
BuildRequires:	motif-devel
BuildRequires:	pkgconfig(xt)

%description
XMakemol can be used to view and manipulate atomic and molecular data given in
xyz format.

XMakemol can produce output in PostScript (black and white or colour)and in xpm
format (which can be translated to gif format using xpmtoppm and ppmtogif).

XMakemol can also produce a series of xpm files which can be translated into an
animated gif file using the bundled utility xmake_anim.pl (formerly
gmake_anim.pl).

%prep
%autosetup -p1

%build
# OpenGL wants <GL/GLwMDrawA.h> -- where does that come from?
%configure --without-opengl
%make_build
										
%install
%make_install
cp xmake_anim.pl.1 %buildroot/%_mandir/man1

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=XMakeMol
Comment=Simple molecule editor and viewer
Exec=%{_bindir}/%{name} 
Icon=chemistry_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Motif;Education;Science;Chemistry;
EOF

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS PROBLEMS ToDo.txt 
%{_bindir}/%name
%{_bindir}/xmake_anim.pl
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
