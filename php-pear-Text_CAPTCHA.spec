%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	CAPTCHA
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generation of CAPTCHA imgaes
Summary(pl):	%{_pearname} - generowanie obraz�w CAPTCHA
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7af4ef3c566d57e633af4a7c86ed97fc
URL:		http://pear.php.net/package/Text_CAPTCHA/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of CAPTCHA (completely automated public Turing test to
tell computers and humans apart) images.

In PEAR status of this package is: %{_status}.

%description -l pl
Implementacja obraz�w CAPTCHA (ca�kowicie zautomatyzowanego
publicznego testu Turinga do odr�nienia ludzi od komputer�w).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Driver

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/Driver/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Driver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
