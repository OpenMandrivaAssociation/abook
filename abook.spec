Name:		abook
Summary:	Text-based addressbook program for mutt
Version:	0.6.1
# This matches the 0.6.1 tag
%define git 6b6a47393127efedca5a75d2adbc70947d37dfa1
Release:	1
License:	GPL
Group:		Networking/Mail
URL:		https://abook.sourceforge.net/
Source:		https://sourceforge.net/code-snapshots/git/a/ab/abook/git.git/abook-git-%{git}.zip
Patch0:		abook-compile.patch
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	autoconf make

%description
Abook is a text-based addressbook program designed for use with the mutt 
mail client.

%prep
%autosetup -p1 -n %{name}-git-%{git}
%configure

%build
%make_build

%install
%make_install

%find_lang %name
chmod 644 AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO

%files -f %name.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/abook
%{_mandir}/man*/abook*.*

