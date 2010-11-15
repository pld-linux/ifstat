Summary:	InterFace STATistics
Summary(pl.UTF-8):	Program do zbierania statystyk ruchu na interfejsach sieciowych
Name:		ifstat
Version:	1.1
Release:	4
License:	GPL
Group:		Applications
Source0:	http://gael.roualland.free.fr/ifstat/%{name}-%{version}.tar.gz
# Source0-md5:	b655642c33a626cfe976792fbcd9b6e1
Patch0:		%{name}-DESTDIR.patch
URL:		http://gael.roualland.free.fr/ifstat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	net-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ifstat(1) is a little tool to report interface activity like
vmstat/iostat do. In addition, ifstat can poll remote hosts through
SNMP. It will also be used for localhost if no other known method
works (You need to have SNMP agent running for this though).

%description -l pl.UTF-8
ifstat(1) jest małym narzędziem, które służy do pobierania informacji
o ruchu na interfejsach sieciowych podobnie do narzędzi vmstat/iostat.
Dodatkowo za pomocą ifstat poprzez protokół SNMP można także pobierać
informacje zdalnie z innych komputerów, o ile jest tam pracujący agent
SNMP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-proc=/proc/net/dev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO HISTORY
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
