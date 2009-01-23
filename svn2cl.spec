%define name svn2cl
%define version 0.11
%define release %mkrel 1

Summary: Generator of ChangeLog(s) from `svn log` output
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ch.tudelft.nl/~arthur/svn2cl/%name-%version.tar.gz
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
sed -i -e 's|^XSL="$dir/|XSL="%{_datadir}/svn2cl/|' svn2cl.sh
chmod 0644 ChangeLog NEWS README TODO authors.xml
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
%doc ChangeLog NEWS README TODO authors.xml
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/*/*
