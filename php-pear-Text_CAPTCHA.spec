%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	CAPTCHA
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generation of CAPTCHA imgaes
Summary(pl):	%{_pearname} - generowanie obrazów CAPTCHA
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	78c7fca0516b0fbc57aa1e91b15e8f97
URL:		http://pear.php.net/package/Text_CAPTCHA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gd
Requires:	php-pear
Requires:	php-pear-Image_Text
Requires:	php-pear-Text_Password
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of CAPTCHA (completely automated public Turing test to
tell computers and humans apart) images.

In PEAR status of this package is: %{_status}.

%description -l pl
Implementacja obrazów CAPTCHA (ca³kowicie zautomatyzowanego
publicznego testu Turinga do odró¿nienia ludzi od komputerów).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
