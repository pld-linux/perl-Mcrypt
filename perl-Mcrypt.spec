#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Mcrypt
Summary:	Mcrypt - Perl extension for the Mcrypt cryptography library
Summary(pl.UTF-8):	Mcrypt - moduł Perla do obsługi biblioteki kryptograficznej Mcrypt
Name:		perl-Mcrypt
Version:	2.5.7.0
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JE/JESUS/%{pdir}-%{version}.tar.gz
# Source0-md5:	f75b606e27a8297752e1a7ac8d993ae6
URL:		http://search.cpan.org/dist/Mcrypt/
BuildRequires:	libmcrypt-devel >= 2.5.7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module wraps the libmcrypt encryption library for easy and
convenient use from within perl. Encryption and decryption using a
variety of algorithms is as easy as a few simple lines of perl.

%description -l pl.UTF-8
Moduł ten opakowuje bibliotekę libmcrypt w celu łatwego jej
wykorzystania w Perlu.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/Mcrypt.pm
%dir %{perl_vendorarch}/auto/Mcrypt
%attr(755,root,root) %{perl_vendorarch}/auto/Mcrypt/*.so
%{_mandir}/man3/*
