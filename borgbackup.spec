%global srcname borgbackup
%global sum A deduplicating backup program

Name:           python-%{srcname}
Version:        1.0.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  python3-devel, openssl-devel, lz4-devel, fuse-devel, libacl-devel

%description
BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

%package -n python3-%{srcname}
Requires:       python3-msgpack
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
An python module which provides a convenient borgbackup.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%{python3_sitearch}/*
%{_bindir}/borg

%changelog
* Tue Dec 01 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-1
- Added dependency python3-msgpack

* Tue Dec 01 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-1
- Initial Packaging for the BorgBackup Project

