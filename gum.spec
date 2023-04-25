
%define		vendor_version	0.10.0

Summary:	A tool for glamorous shell scripts
Name:		gum
Version:	0.10.0
Release:	0.1
License:	MIT
Group:		Applications
Source0:	https://github.com/charmbracelet/gum/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5eded4e315659eabce6a3e7d69dc02c2
Source1:	%{name}-vendor-%{vendor_version}.tar.xz
# Source1-md5:	b96ac690406c114b8c70a3bc0b3defb4
URL:		https://github.com/charmbracelet/gum
BuildRequires:	golang
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
A tool for glamorous shell scripts. Leverage the power of Bubbles and
Lip Gloss in your scripts and aliases without writing any Go code!

%prep
%setup -q -a1

%{__mv} %{name}-%{vendor_version}/vendor .
%{__mkdir} .go-cache

%build
%__go build -v -mod=vendor -o target/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

cp -p target/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_examplesdir}/%{name}-%{version}
