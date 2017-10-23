Name: python-paramiko
Summary: SSH2 protocol for Python
Version: 1.9.0
Release: 0
License: LGPL-2.1
Group: System Environment/Libraries
URL: https://github.com/paramiko/paramiko
Source: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
BuildArch: noarch
BuildRequires: python-devel
BuildRequires:  python-setuptools
Requires: python-crypto

Provides: paramiko
Obsoletes: paramiko <= %{version}-%{release}

%description
Paramiko is a module for python that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines.  the module works
by taking a socket-like object that you pass in, negotiating with the remote
server, authenticating (using a password or a given private key), and opening
flow-controled "channels" to the server, which are returned as socket-like
objects. you are responsible for verifying that the server's host key is the
one you expected to see, and you have control over which kinds of encryption
or hashing you prefer (if you care), but all of the heavy lifting is done by
the paramiko module.

%prep
%setup -q
cp %{SOURCE1001} .

%build
/usr/bin/python2 setup.py build

%install
/usr/bin/python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{python_sitelib}/*
%exclude %{python_sitelib}/paramiko/*.pyc

%changelog
