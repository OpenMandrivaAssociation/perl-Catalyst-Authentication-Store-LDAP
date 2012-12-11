%define upstream_name    Catalyst-Authentication-Store-LDAP
%define upstream_version 1.012

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	LDAP authentication storage backend
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Net::LDAP::Server::Test)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This plugin implements the the Catalyst::Authentication manpage v.10 API.
Read that documentation first if you are upgrading from a previous version
of this plugin.

This plugin uses 'Net::LDAP' to let your application authenticate against
an LDAP directory. It has a pretty high degree of flexibility, given the
wide variation of LDAP directories and schemas from one system to another.

It authenticates users in two steps:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.12.0-2mdv2011.0
+ Revision: 680717
- mass rebuild

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.12.0-1mdv2011.0
+ Revision: 586765
- new version

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.11.0-1mdv2011.0
+ Revision: 553576
- update to 1.011

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.8.0-1mdv2010.1
+ Revision: 532138
- update to 1.008

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.7.0-1mdv2010.1
+ Revision: 526425
- update to 1.007

* Tue Dec 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.6.0-1mdv2010.1
+ Revision: 478787
- update to 1.006

* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.500-1mdv2010.1
+ Revision: 474564
- spec cleanup

  + Buchan Milne <bgmilne@mandriva.org>
    - import perl-Catalyst-Authentication-Store-LDAP


* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.1005-1mdv
- initial mdv release, generated with cpan2dist

