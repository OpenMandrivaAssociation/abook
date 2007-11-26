%define name	abook
%define version	0.5.6
%define release	%mkrel 1

Name:		%{name}
Summary:	Text-based addressbook program for mutt
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
BuildRequires:	ncurses-devel readline-devel
URL:		http://abook.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/abook/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Abook is a text-based addressbook program designed for use with the mutt 
mail client.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%find_lang %name

chmod 644 AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README THANKS TODO
%{_bindir}/abook
%{_mandir}/man*/abook*.*
#%{_mandir}/man5/abook.conf.5*

