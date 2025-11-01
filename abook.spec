Name:		abook
Summary:	Text-based addressbook program for mutt
Version:	0.6.2
# This matches the 0.6.2 tag
%define git a243d4a18a64f4ee188191a797b34f60d4ff852f
Release:	1
License:	GPL
Group:		Networking/Mail
URL:		https://abook.sourceforge.net/
Source:		https://sourceforge.net/code-snapshots/git/a/ab/abook/git.git/abook-git-%{git}.zip
Patch0:		abook-compile.patch
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	autoconf make
BuildRequires:	gettext
BuildSystem:	autotools

%description
Abook is a text-based addressbook program designed for use with the mutt 
mail client.

%install -a
%find_lang %{name}

chmod 644 AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO

%files -f %name.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/abook
%{_mandir}/man*/abook*.*

