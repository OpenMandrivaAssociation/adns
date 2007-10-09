%define	name	adns
%define	version	1.3
%define	release	%mkrel 1
%define	major	1
%define libname	%mklibname %{name} %{major}

Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.chiark.greenend.org.uk/~ian/adns/
License:	GPL
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.bz2
Group:		Networking/Other
Requires: 	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%package -n	%{libname}
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

%package -n	%{libname}-devel
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libadns-devel
Provides:	adns-devel
Obsoletes:	adns-devel

%description -n	%{libname}-devel
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

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_libdir}

%makeinstall

#make prefix=$RPM_BUILD_ROOT%{_prefix} install
(set -e
 cd %{buildroot}%{_libdir}
 ln -s libadns.so.? libadns.so
)
 
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README TODO changelog
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a


