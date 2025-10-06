#specfile originally created for Fedora, modified for Moblin Linux
Summary: The GNU line editor
Name: ed
Version: 1.22.2
Release: 1
License: GPLv2
Source: %{name}-%{version}.tar.gz
URL:    http://www.gnu.org/software/ed/

%description
Ed is a line-oriented text editor, used to create, display, and modify
text files (both interactively and via shell scripts).  For most
purposes, ed has been replaced in normal usage by full-screen editors
(emacs and vi, for example).

Ed was the original UNIX editor, and may be used by some programs.  In
general, however, you probably don't need to install it and you probably
won't use it.

%prep
%autosetup -n %{name}-%{version}

%build
# Custom configure script; not Autoconf, so we do not use %%configure macro
./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --datarootdir=%{_datadir} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --program-prefix=%{?_program_prefix} \
    CC="${CC-gcc}" \
    CPPFLAGS="${CPPFLAGS}" \
    CFLAGS="${CFLAGS}" \
    LDFLAGS="${LDFLAGS}"
%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_infodir}/*

%files
%license COPYING
%doc ChangeLog NEWS README AUTHORS
%{_bindir}/*
%doc %{_mandir}/*/*

