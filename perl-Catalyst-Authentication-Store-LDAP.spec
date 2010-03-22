%define upstream_name    Catalyst-Authentication-Store-LDAP
%define upstream_version 1.007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    LDAP authentication storage backend
License:    GPL or Artistic
Group:      Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Catalyst::Plugin::Authentication)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(Net::LDAP::Server::Test)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst
