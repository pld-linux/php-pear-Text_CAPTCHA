%define		_status		alpha
%define		_pearname	Text_CAPTCHA
Summary:	%{_pearname} - generation of CAPTCHA imgaes
Summary(pl.UTF-8):	%{_pearname} - generowanie obrazów CAPTCHA
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3c30c8650436ea2e961c29e9eedf0066
URL:		http://pear.php.net/package/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear >= 4:1.3-5
Requires:	php-pear-Text_Password
Suggests:	php(gd)
Suggests:	php-pear-Image_Text
Suggests:	php-pear-Numbers_Words
Suggests:	php-pear-Text_Figlet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Numbers/Words.*)' 'pear(Text/Figlet.*)' 'pear(Image/Text.*)'

%description
Implementation of CAPTCHA (completely automated public Turing test to
tell computers and humans apart) images.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja obrazów CAPTCHA (całkowicie zautomatyzowanego
publicznego testu Turinga do odróżnienia ludzi od komputerów).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/CAPTCHA.php
%{php_pear_dir}/Text/CAPTCHA/*
