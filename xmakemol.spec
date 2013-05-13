%define name	xmakemol
%define version 5.16
%define release  7

Name: 	 	%{name}
Summary: 	Simple XYZ molecule editor and GL viewer
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/xmakemol/%{name}-%{version}.tar.gz
URL:		http://vegemite.chem.nottingham.ac.uk/~xmakemol/
License:	GPL
Group:		Sciences/Chemistry
BuildRequires:	pkgconfig(x11)
BuildRequires:	lesstif-devel
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
%setup -q

%build
# Disable OpenGL for now, as linking against libmesaglw is broken
# AdamW 2007/07
%configure2_5x --without-opengl
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS PROBLEMS ToDo.txt 
%{_bindir}/%name
%{_bindir}/xmake_anim.pl
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 5.16-6mdv2011.0
+ Revision: 634903
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 5.16-5mdv2010.0
+ Revision: 435135
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 5.16-4mdv2009.0
+ Revision: 262458
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 5.16-3mdv2009.0
+ Revision: 257130
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 18 2008 Austin Acton <austin@mandriva.org> 5.16-1mdv2008.1
+ Revision: 154512
- file list
- sync
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jul 20 2007 Adam Williamson <awilliamson@mandriva.org> 5.15-2mdv2008.0
+ Revision: 54073
- disable OpenGL for now, doesn't link properly
- add missing buildrequires
- rebuild against new lesstif
- don't manually bzip2 manpage, leave it to the macro
- xdg menu

  + Austin Acton <austin@mandriva.org>
    - Import xmakemol



* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 5.15-1mdk
- New release 5.15

* Tue Aug 24 2004 Austin Acton <austin@mandrake.org> 5.13-2mdk
- new menu

* Sun Aug 8 2004 Austin Acton <austin@mandrake.org> 5.13-1mdk
- new menu

* Thu Aug 03 2004 Franck Villaume <fvill@freesurf.fr> 5.13-1mdk
- 5.13

* Sun Feb 22 2004 Austin Acton <austin@mandrake.org> 5.11-1mdk
- 5.11

* Wed Oct 8 2003 Austin Acton <aacton@yorku.ca> 5.09-1mdk
- 5.09

* Mon Aug 25 2003 Austin Acton <aacton@yorku.ca> 5.08-1mdk
- 5.08

* Fri Apr 25 2003 Austin Acton <aacton@yorku.ca> 5.07-2mdk
- buildrequires lesstif-devel

* Tue Apr 15 2003 Austin Acton <aacton@yorku.ca> 5.07-1mdk
- initial package
