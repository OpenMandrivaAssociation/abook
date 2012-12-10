%define name	abook
%define version	0.6.0
%define beta	pre2
%define release	%mkrel 0.%{beta}.5

Name:		%{name}
Summary:	Text-based addressbook program for mutt
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
URL:		http://abook.sourceforge.net/
Source:		http://abook.sourceforge.net/devel/%{name}-%{version}%{beta}.tar.gz
Patch:      http://abook.sourceforge.net/patches/abook_vcard_import.patch
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Abook is a text-based addressbook program designed for use with the mutt 
mail client.

%prep
%setup -q -n %{name}-%{version}%{beta}
%patch -p 1

%build
%configure2_5x
%make

%install
%makeinstall

%find_lang %name

chmod 644 AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/abook
%{_mandir}/man*/abook*.*
#%{_mandir}/man5/abook.conf.5*



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.6.0-0.pre2.5mdv2011.0
+ Revision: 664788
- rebuild

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-0.pre2.4mdv2011.0
+ Revision: 616485
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-0.pre2.3mdv2010.0
+ Revision: 436623
- rebuild

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-0.pre2.2mdv2009.1
+ Revision: 349457
- add vcard import patch
- new version

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.5.6-1mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import abook


* Sun Sep 03 2006 Jerome Soyer <saispo@mandriva.org> 0.5.6-1mdv2007.0
- new release 0.5.6

* Mon Jun 26 2006 Lenny Cartier <lenny@mandriva.com> 0.5.5-2mdv2007.0
- rebuild

* Tue Mar 21 2006 Lenny Cartier <lenny@mandriva.com> 0.5.5-1mdk
- 0.5.5

* Mon Sep 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.4-1mdk
- New release 0.5.4

* Thu May 12 2005 Olivier Thauvin <nanardon@mandriva.org> 0.5.3-2mdk
- fix doc permissions

* Thu May 12 2005 Olivier Thauvin <nanardon@mandriva.org> 0.5.3-1mdk
- 0.5.3

* Sun Apr 03 2005 Michael Scherer <misc@mandrake.org> 0.5.2-2mdk
- Rebuild for readline


* Fri Apr 23 2004 Michael Scherer <misc@mandrake.org> 0.5.2-1mdk 
- 0.5.2
- clean Requires
- rpmbuildupdate aware

* Fri Nov 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.1-1mdk
- 0.5.1

* Wed Jul 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-2mdk
- buildrequires from Michael Scherer

* Tue Jul 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-1mdk
- 0.5.0

* Sat Dec 28 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.17-2mdk
- rebuild for rpm and glibc

* Fri Jun 14 2002 Alexander Skwar <ASkwar@DigitalProjects.com> 0.4.17-1mdk
- 0.4.17

* Mon Mar 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.4.16-1mdk
- 0.4.16

* Mon Nov 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.15-1mdk
- 0.4.15

* Thu Jun 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.13-1mdk
- updated to 0.4.13

* Thu Mar 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.12-1mdk
- updated to 0.4.12

* Thu Jan 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.11-1mdk
- updated to 0.4.11

* Sat Dec 16 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.4.10-1mdk
 - first mandrake version

* Wed Sep 20 2000 Gustavo Niemeyer <niemeyer@conectiva.com>
- First package.
