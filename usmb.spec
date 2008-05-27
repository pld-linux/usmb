Summary:	Unprivileged mounting of SMB/CIFS shares via FUSE
Name:		usmb
Version:	20080421
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	http://www.atmi41.dsl.pipex.com/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	0c89bee107e20f91f79fc823ae382ef2
Patch0:		%{name}-Makefile.patch
URL:		http://www.atmi41.dsl.pipex.com/code.html
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libsmbclient-devel >= 1:3.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
usmb lets you mount SMB/CIFS shares via FUSE, in the vein of the Map
Network Drive functionality in Windows. It differs from the other FUSE
SMB filesystems (fusesmb, SMB for FUSE) in that it doesn't have
Network Neighbourhood functionality: this means that you can mount
shares that you can't see via NetBIOS browsing.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR="%{_bindir}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog doc/*
%attr(755,root,root) %{_bindir}/*
