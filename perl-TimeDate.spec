%define		pdir	Time
%define		pnam	Date

%include	/usr/lib/rpm/macros.perl

Summary:	perl5 TimeDate distribution
Name:		perl-TimeDate
Version:	2.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	b1d91153ac971347aee84292ed886c1c
URL:		http://search.cpan.org/dist/TimeDate/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl5 TimeDate distribution.

%prep
%setup -qn %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%check
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Date/Format.pm
%dir %{perl_vendorlib}/Date/Language
%{perl_vendorlib}/Date/Language/*.pm
%{perl_vendorlib}/Date/Language.pm
%{perl_vendorlib}/Date/Parse.pm
%{perl_vendorlib}/Time/Zone.pm
%{_mandir}/man3/Date::*.3pm*
%{_mandir}/man3/Time::*.3pm*

