Summary: Generator of ChangeLog(s) from `svn log` output
Name: svn2cl
Version: 0.13
Release: 2
Source0: http://ch.tudelft.nl/~arthur/svn2cl/%name-%version.tar.gz
Patch0: svn2cl-0.12-accum.patch
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
%patch0 -p0 -b .accum
%patch1 -p1 -b .authors
%patch2 -p0 -b .strip

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


%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.13-1mdv2012.0
+ Revision: 700553
- 0.13

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12-1.2mdv2011.0
+ Revision: 615052
- the mass rebuild of 2010.1 packages

* Tue Dec 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.12-0.2mdv2010.1
+ Revision: 472235
- Fix accum patch
- Update to 0.12

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.11-3mdv2010.0
+ Revision: 445268
- rebuild

* Sun Mar 01 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11-2mdv2009.1
+ Revision: 346836
- Readd patches which were silently dropped in the previous release:
  they are used by software in Mandriva's svn
- Fix license
- SPEC file clean-ups

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.11-1mdv2009.1
+ Revision: 332891
- New upstream release

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2009.0
+ Revision: 269396
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 0.10-1mdv2009.0
+ Revision: 208489
- New version 0.10

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.9-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 18 2007 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2008.0
+ Revision: 89520
- patch 2: fix auto guessing path to strip

* Thu Apr 19 2007 Olivier Blin <blino@mandriva.org> 0.9-1mdv2008.0
+ Revision: 14989
- 0.9


* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 0.8-2mdv2007.0
+ Revision: 102585
- fix accum option (thanks Pixel for the report)

* Thu Dec 28 2006 Olivier Blin <oblin@mandriva.com> 0.8-1mdv2007.1
+ Revision: 102380
- 0.8
- Import svn2cl

* Thu Jun 22 2006 Olivier Blin <oblin@mandriva.com> 0.6-3mdv2007.0
- Patch0: don't remove first entry of previous log in --accum mode
  (looks like svn log has a new dates handling behavior)

* Mon Mar 20 2006 Olivier Blin <oblin@mandriva.com> 0.6-2mdk
- Patch0: add --accum option
- Patch1: add doc about authors file and perl script to convert
  colon-separated authors file to XML
- package authors.xml example file and convert_authors.pl script

* Wed Mar 15 2006 Olivier Blin <oblin@mandriva.com> 0.6-1mdk
- initial Mandriva release

