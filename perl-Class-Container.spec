%define upstream_name	 Class-Container
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Glues object frameworks together transparently
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRequires:	perl-Params-Validate
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and
several other objects must create each other transparently, passing the
appropriate parameters to the right class, possibly substituting other
subclasses for any of these objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/Container.pm
%{_mandir}/*/*
