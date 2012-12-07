%define	major 1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Name:		adns
Version:	1.4
Release:	%mkrel 10
Group:		Networking/Other
License:	GPLv2+
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.bz2
Source1:	README.Mandriva
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
	* It is reasonably easy to use for simple programs which just want
	to translate names to addresses, look up MX records, etc.
	* It can be used in an asynchronous, non-blocking, manner. Many
	queries can be handled simultaneously.
	* Responses are decoded automatically into a natural representation
	for a C program - there is no need to deal with DNS packet
	formats.
	* Sanity checking (eg, name syntax checking, reverse/forward
	correspondence, CNAME pointing to CNAME) is performed
	automatically.
	* Time-to-live, CNAME and other similar information is returned in
	an easy-to-use form, without getting in the way.
	* There is no global state in the library; resolver state is an
	opaque data structure which the client creates explicitly. A
	program can have several instances of the resolver.
	* Errors are reported to the application in a way that distinguishes
	the various causes of failure properly.
	* Understands conventional resolv.conf, but this can overridden by
	environment variables.
	* Flexibility. For example, the application can tell adns to: ignore
	environment variables (for setuid programs), disable sanity checks
	eg to return arbitrary data, override or ignore resolv.conf in
	favour of supplied configuration, etc.
	* Believed to be correct ! For example, will correctly back off to
	TCP in case of long replies or queries, or to other nameservers if
	several are available. It has sensible handling of bad responses
	etc.

%package -n %{libname}
Group:		System/Libraries
Summary:	Libraries needed to run applications using adns

%description -n	%{libname}
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
    * It is reasonably easy to use for simple programs which just want
      to translate names to addresses, look up MX records, etc.
    * It can be used in an asynchronous, non-blocking, manner. Many
      queries can be handled simultaneously.
    * Responses are decoded automatically into a natural representation
      for a C program - there is no need to deal with DNS packet
      formats.
    * Sanity checking (eg, name syntax checking, reverse/forward
      correspondence, CNAME pointing to CNAME) is performed
      automatically.
    * Time-to-live, CNAME and other similar information is returned in
      an easy-to-use form, without getting in the way.
    * There is no global state in the library; resolver state is an
      opaque data structure which the client creates explicitly. A
      program can have several instances of the resolver.
    * Errors are reported to the application in a way that distinguishes
      the various causes of failure properly.
    * Understands conventional resolv.conf, but this can overridden by
      environment variables.
    * Flexibility. For example, the application can tell adns to: ignore
      environment variables (for setuid programs), disable sanity checks
      eg to return arbitrary data, override or ignore resolv.conf in
      favour of supplied configuration, etc.
    * Believed to be correct ! For example, will correctly back off to
      TCP in case of long replies or queries, or to other nameservers if
      several are available. It has sensible handling of bad responses
      etc.

This package contains all of adns libraries.

%package -n %{develname}
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel < 1.4

%description -n	%{develname}
adns is a resolver library for C (and C++) programs. In contrast with
the existing interfaces, gethostbyname et al and libresolv, it has the
following features:
    * It is reasonably easy to use for simple programs which just want
      to translate names to addresses, look up MX records, etc.
    * It can be used in an asynchronous, non-blocking, manner. Many
      queries can be handled simultaneously.
    * Responses are decoded automatically into a natural representation
      for a C program - there is no need to deal with DNS packet
      formats.
    * Sanity checking (eg, name syntax checking, reverse/forward
      correspondence, CNAME pointing to CNAME) is performed
      automatically.
    * Time-to-live, CNAME and other similar information is returned in
      an easy-to-use form, without getting in the way.
    * There is no global state in the library; resolver state is an
      opaque data structure which the client creates explicitly. A
      program can have several instances of the resolver.
    * Errors are reported to the application in a way that distinguishes
      the various causes of failure properly.
    * Understands conventional resolv.conf, but this can overridden by
      environment variables.
    * Flexibility. For example, the application can tell adns to: ignore
      environment variables (for setuid programs), disable sanity checks
      eg to return arbitrary data, override or ignore resolv.conf in
      favour of supplied configuration, etc.
    * Believed to be correct ! For example, will correctly back off to
      TCP in case of long replies or queries, or to other nameservers if
      several are available. It has sensible handling of bad responses
      etc.

This package contains static libraries and header files need for development.

%prep
%setup -q
# make it lib64 aware
perl -pi -e "/^lib_dir=/ and s,/lib,/%{_lib}," settings.make.in

cp %{SOURCE1} README.Mandriva

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README TODO changelog README.Mandriva
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-8mdv2011.0
+ Revision: 662756
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-7mdv2011.0
+ Revision: 603173
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean spec

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-6mdv2010.1
+ Revision: 518984
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Rebuild for fix warning

* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2010.0
+ Revision: 454169
- document CVE-2008-1447 / CVE-2008-4100 poisoning vulnerability in README.Mandriva (suse)

* Mon Aug 10 2009 Funda Wang <fwang@mandriva.org> 1.4-3mdv2010.0
+ Revision: 414151
- fix install

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2010.0
+ Revision: 413546
- fix build
- rebuild

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4-1mdv2009.1
+ Revision: 331487
- update to new version 1.4
 - spec file clean

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdv2009.1
+ Revision: 316490
- rebuild

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 1.3-4mdv2009.0
+ Revision: 275946
- apply devel policy
- check major

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 220346
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.3-2mdv2008.1
+ Revision: 148428
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org> 1.3-1mdv2007.0
+ Revision: 55883
- 1.3
- Import adns

* Thu Dec 15 2005 Arnaud de Lorbeau <devel@mandriva.com> 1.1-5mdk
- rebuild

* Tue Oct 12 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1-4mdk
- merge lost fixes from 10.0-branch:
  * lib64 fixes

* Sun Jun 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.1-3mdk
- more spec file fixes (forgot to run rpmlint...)

* Sun Jun 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.1-2mdk
- rebuilt against new deps and with gcc v3.4.x
- use the %%configure2_5x macro
- added P0
- misc spec file fixes

* Thu Apr 29 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.1-1mdk
- new release

