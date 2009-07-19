
%define realname   Catalyst-Authentication-Store-LDAP
%define version    0.1005
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    LDAP authentication storage backend
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Catalyst::Plugin::Authentication)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(Net::LDAP::Server::Test)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
This plugin implements the the Catalyst::Authentication manpage v.10 API.
Read that documentation first if you are upgrading from a previous version
of this plugin.

This plugin uses 'Net::LDAP' to let your application authenticate against
an LDAP directory. It has a pretty high degree of flexibility, given the
wide variation of LDAP directories and schemas from one system to another.

It authenticates users in two steps:

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


