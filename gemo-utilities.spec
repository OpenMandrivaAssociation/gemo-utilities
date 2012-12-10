%define gcj_support 1

%define	name	gemo-utilities
%define	version	20070201
%define	release	10
%define	jarlibs	xalan-j2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Gemo Utilities
License:	LGPL
Group:		Development/Java
Url:		http://forge.objectweb.org/projects/activexml/
# from cvs
Source0:	%{name}-%{version}.tar.lzma
BuildRequires:	lzma
BuildRequires:	java-rpmbuild java-devel ant %{jarlibs}
Requires:	%{jarlibs}
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%else
BuildArch: noarch
%endif
BuildRequires:    locales-en

%description
Gemo Utilities

%prep
%setup -q
#make sure that we don't use precompiled java package if shipped
rm -rf lib

%build
export LC_ALL=ISO-8859-1
CLASSPATH=$(build-classpath %{jarlibs}) \
%{ant} dist -DDSTAMP=%{version}
%{jar} -i dist/%{name}-%{version}.jar

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_javadir}
install -m644 dist/%{name}-%{version}.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf %{buildroot}

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%{_javadir}/*.jar
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20070201-9mdv2011.0
+ Revision: 618447
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20070201-8mdv2010.0
+ Revision: 429190
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20070201-7mdv2009.0
+ Revision: 245880
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 20070201-5mdv2008.1
+ Revision: 120882
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 20070201-4mdv2008.0
+ Revision: 87377
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Sun Sep 09 2007 Pascal Terjan <pterjan@mandriva.org> 20070201-3mdv2008.0
+ Revision: 82803
- update to new version


* Sat Feb 03 2007 David Walluck <walluck@mandriva.org> 20070201-2mdv2007.0
+ Revision: 116036
- aot compile

  + Per Øyvind Karlsen <pkarlsen@mandriva.com>
    - d'oh, rm -rf in stead of rm -f lib
    - ensure that proper version is created based on snapshot date and not current date
      misc packaging fixes
    - do actually export CLASSPATH
    - Import gemo-utilities

