%define gcj_support 1

%define	name	gemo-utilities
%define	version	20070201
%define	release	%mkrel 4
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
BuildRequires:	jpackage-utils java-devel ant %{jarlibs}
Requires:	%{jarlibs}
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%else
BuildArch: noarch
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gemo Utilities

%prep
%setup -q
#make sure that we don't use precompiled java package if shipped
rm -rf lib

%build
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


