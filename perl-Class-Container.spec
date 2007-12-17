%define module	Class-Container
%define name	perl-%{module}
%define version	0.12
%define release	%mkrel 3

Summary:	Glues object frameworks together transparently
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRequires:	perl-Params-Validate

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for "HTML::Mason", in
which the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and
several other objects must create each other transparently, passing the
appropriate parameters to the right class, possibly substituting other
subclasses for any of these objects.

%prep

%setup -q -n %{module}-%{version}

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

