%define commit 7e38c66c091657dcc5d8b2ba902d6ce37db8040d
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define date 20150328

Summary:	A wrapper script for tc-play for pain free management of tc-play containers
Name:		tcplay-helper
Version:	0~git%{date}
Release:	1
License:	MIT
Group:		File tools
URL:		https://github.com/robertmuil/%{name}
Source0:	https://github.com/robertmuil/%{name}/archive/%{commit}/%{name}-%{shortcommit}.zip

Requires:	tcplay

%description
tcplay-helper lets you easily manage truecrypt containers with tc-play. The
script currently supports creating, mounting and unmounting tc-play
containers. Usage is simple and the only requirement is that tcplay is
installed on the system.

NOTE: tcplay-helper is still a work in progress. Its been tested primarily
with containers formatted as ext4.

%files
%{_bindir}/%{name}
%doc README.rst
%doc LICENSE

%prep
%setup -q -n %{name}-%{version}

%build
# Nothing to do here

%install
# binary
%__install -dm 0755 %{buildroot}%{_bindir}/
%__install -pm 0755 build/%{name} %{buildroot}%{_bindir}/

