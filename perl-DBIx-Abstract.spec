#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	Abstract
Summary:	DBIx::Abstract - DBI SQL abstraction
Summary(pl):	DBIx::Abstract - abstrakcja DBI SQL
Name:		perl-DBIx-Abstract
Version:	1.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	230009d2613d3ad84a38c8589384003d
URL:		http://search.cpan.org/dist/DBIx-Abstract/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides methods for doing manipulating database tables.
It provides methods for all of the more important SQL commands (like
SELECT, INSERT, REPLACE, UPDATE, DELETE).

%description -l pl
Ten modu³ udostêpnia metody do obs³ugi tabel baz danych. Zawiera
metody do wszystkich wa¿niejszych poleceñ SQL (takich jak SELECT,
INSERT, REPLACE, UPDATE, DELETE).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
