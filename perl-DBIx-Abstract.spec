#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Abstract
Summary:	DBIx::Abstract - DBI SQL abstraction
Summary(pl):	DBIx::Abstract - abstrakcja DBI SQL
Name:		perl-DBIx-Abstract
Version:	1.004
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides methods for doing manipulating database tables.
It provides methods for all of the more important SQL commands (like
SELECT, INSERT, REPLACE, UPDATE, DELETE).

%description -l pl
Ten modu� udost�pnia metody do obs�ugi tabel baz danych. Zawiera
metody do wszystkich wa�niejszych polece� SQL (takich jak SELECT,
INSERT, REPLACE, UPDATE, DELETE).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor 
%{__make}

# test require local SQL server access
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*