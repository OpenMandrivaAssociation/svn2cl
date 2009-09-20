Summary: Generator of ChangeLog(s) from `svn log` output
Name: svn2cl
Version: 0.11
Release: %mkrel 3
Source0: http://ch.tudelft.nl/~arthur/svn2cl/%name-%version.tar.gz
Patch0: svn2cl-0.11-accum.patch
Patch1: svn2cl-0.11-authors.patch
Patch2: svn2cl-fix-stripping.patch
License: BSD
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
sed -i -e 's|^XSL="$dir/|XSL="%{_datadir}/svn2cl/|' svn2cl.sh
chmod 0644 ChangeLog NEWS README TODO authors.xml
chmod 0755 convert_authors.pl

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
install -m 755 svn2cl.sh %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/svn2cl.sh %{buildroot}%{_bindir}/%{name}
install -m 644 svn2cl.xsl svn2html.css svn2html.xsl %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -m 644 svn2cl.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README TODO authors.xml convert_authors.pl
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/*/*
