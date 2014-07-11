%define	major 1
%define libname	%mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Name:		adns
Version:	1.4
Release:	17
Group:		Networking/Other
License:	GPLv2+
Url:		http://www.chiark.greenend.org.uk/~ian/adns/
Source0:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.chiark.greenend.org.uk/users/ian/adns/%{name}-%{version}.tar.gz.sig
Source2:	README.Mandriva

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
Summary:	Libraries needed to run applications using adns
Group:		System/Libraries

%description -n	%{libname}
This package contains all of adns libraries.

%package -n %{devname}
Summary:	Advanced, easy to use, asynchronous-capable DNS client library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains static libraries and header files need for development.

%prep
%setup -q
# make it lib64 aware
sed -i -e "/^lib_dir=/ and s,/lib,/%{_lib}," settings.make.in

cp %{SOURCE2} README.Mandriva

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

rm -f %{buildroot}/%{_libdir}/*.a

%files
%doc README TODO changelog README.Mandriva
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so

