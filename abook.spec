%define name	abook
%define version	0.6.0
%define beta	pre2
%define release	%mkrel 0.%{beta}.6

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
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	gcc-c++, gcc, gcc-cpp


%description
Abook is a text-based addressbook program designed for use with the mutt 
mail client.

%prep
%setup -q -n %{name}-%{version}%{beta}
%patch -p 1

%build
export CC=gcc
export CXX=g++
%configure
%make

%install
%makeinstall

%find_lang %name

chmod 644 AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO


%files -f %name.lang
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/abook
%{_mandir}/man*/abook*.*

