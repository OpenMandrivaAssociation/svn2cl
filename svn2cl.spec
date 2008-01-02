%define name svn2cl
%define version 0.9
%define release %mkrel 2

Summary: Generator of ChangeLog(s) from `svn log` output
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: svn2cl-0.8-accum.patch
Patch1: svn2cl-0.6-authors.patch
Patch2: svn2cl-fix-stripping.patch
License: GPL
Group: Development/Other
Url: http://ch.tudelft.nl/~arthur/svn2cl/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libxslt-proc
BuildArch: noarch

%description
svn2cl is a simple xsl transformation and shellscript wrapper for generating a
classic GNU-style ChangeLog from a subversion repository log. It is made from
several changelog-like scripts using common xslt constructs found in different
places.

%prep
%setup -q
%patch0 -p1 -b .accum
%patch1 -p1 -b .authors
%patch2 -p1 -b .strip
chmod 0644 ChangeLog NEWS README TODO authors.xml
chmod 0755 convert_authors.pl
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 svn2cl.sh $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_datadir}/%{name}/svn2cl.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 644 svn2cl.xsl svn2html.css svn2html.xsl $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 svn2cl.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO authors.xml convert_authors.pl
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/*/*


