Summary:	Yidish dictionary for aspell
Summary(pl):	S³ownik jidysz dla aspella
Name:		aspell-yi
Version:	0.01.1
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/yi/aspell6-yi-%{version}-%{subv}.tar.bz2
# Source0-md5:	9d514384bf00cfb9ceb0d5f78f998d93
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.60.0
Requires:	aspell >= 0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yidish dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik jidysz (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-yi-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
