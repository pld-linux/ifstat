Summary:	InterFace STATistics
Summary(pl):	Program do zbieranai statystyk ruchu na interfejsach sieciowych
Name:		ifstat
Version:	1.0
Release:	1
License:	GPL
Group:		Applications
Vendor:		Gaël Roualland <gael.roualland@dial.oleane.com>
Source0:	http://gael.roualland.free.fr/ifstat/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gael.roualland.free.fr/ifstat/
BuildRequires:	autoconf
BuildRequires:	:	automake
BuildRequires:	ucd-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ifstat(1) is a little tool to report interface activity like
vmstat/iostat do. In addition, ifstat can poll remote hosts through
SNMP. It will also be used for localhost if no other known method
works (You need to have SNMP agent running for this though).

%description -l pl
ifstat(1) jest ma³ym narzêdziem które s³u¿y do pobierania informacji o
ruchu na interfejsach sieciowych podobnie do narzêdzi vmstat/iostat.
Dodatkowo za pomoc± ifstat poprzez protokó³ SNMP mo¿na tak¿e pobieraæ
informacje z zdalnie z innych komputerów o ile jest tam pracuj±cy SNMP
agent.

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
