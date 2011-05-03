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

