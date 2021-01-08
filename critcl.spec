#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : critcl
Version  : 3.1.18.1
Release  : 6
URL      : file:///insilications/build/clearlinux/packages/critcl/critcl-3.1.18.1.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/critcl/critcl-3.1.18.1.tar.gz
Summary  : zlib compression library
Group    : Development/Tools
License  : LGPL-2.0+
Requires: critcl-bin = %{version}-%{release}
Requires: critcl-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : gcc-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : pkgconfig(tcl)
BuildRequires : pkgconfig(tk)
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : tcllib
BuildRequires : tcllib-dev
BuildRequires : tk
BuildRequires : tk-dev
BuildRequires : tk-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ZLIB DATA COMPRESSION LIBRARY
zlib 1.2.5 is a general purpose data compression library.  All the code is
thread safe.  The data format used by the zlib library is described by RFCs
(Request for Comments) 1950 to 1952 in the files
http://www.ietf.org/rfc/rfc1950.txt (zlib format), rfc1951.txt (deflate format)
and rfc1952.txt (gzip format).

%package bin
Summary: bin components for the critcl package.
Group: Binaries

%description bin
bin components for the critcl package.


%package dev
Summary: dev components for the critcl package.
Group: Development
Requires: critcl-lib = %{version}-%{release}
Requires: critcl-bin = %{version}-%{release}
Provides: critcl-devel = %{version}-%{release}
Requires: critcl = %{version}-%{release}

%description dev
dev components for the critcl package.


%package lib
Summary: lib components for the critcl package.
Group: Libraries

%description lib
lib components for the critcl package.


%prep
%setup -q -n critcl
cd %{_builddir}/critcl

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610087724
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
#
export CXXFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
#
export FCFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
export FFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
export CFFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
#
export LDFLAGS="-O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fno-exceptions -pthread -static-libstdc++ -static-libgcc"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
echo "tclsh"
echo "tclsh"


%install
export SOURCE_DATE_EPOCH=1610087724
rm -rf %{buildroot}
%buildtcl_script_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/critcl

%files dev
%defattr(-,root,root,-)
/usr/include/critcl_callback/callback.h
/usr/include/critcl_callback/critcl_callback.decls
/usr/include/critcl_callback/critcl_callbackDecls.h
/usr/include/critcl_callback/critcl_callbackStubLib.h
/usr/lib/tcl8.6/critcl-app3.1.18/critcl.tcl
/usr/lib/tcl8.6/critcl-app3.1.18/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-app3.1.18/runtime.tcl
/usr/lib/tcl8.6/critcl-app3.1.18/tea/Config.in
/usr/lib/tcl8.6/critcl-app3.1.18/tea/Makefile.in
/usr/lib/tcl8.6/critcl-app3.1.18/tea/aclocal.m4
/usr/lib/tcl8.6/critcl-app3.1.18/tea/configure.in
/usr/lib/tcl8.6/critcl-app3.1.18/tea/tclconfig/README.txt
/usr/lib/tcl8.6/critcl-app3.1.18/tea/tclconfig/install-sh
/usr/lib/tcl8.6/critcl-app3.1.18/tea/tclconfig/tcl.m4
/usr/lib/tcl8.6/critcl-bitmap1.0.1/bitmap.tcl
/usr/lib/tcl8.6/critcl-bitmap1.0.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-class1.1.1/class.h
/usr/lib/tcl8.6/critcl-class1.1.1/class.tcl
/usr/lib/tcl8.6/critcl-class1.1.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-cutil0.2.1/allocs/critcl_alloc.h
/usr/lib/tcl8.6/critcl-cutil0.2.1/asserts/critcl_assert.h
/usr/lib/tcl8.6/critcl-cutil0.2.1/cutil.tcl
/usr/lib/tcl8.6/critcl-cutil0.2.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-cutil0.2.1/trace/critcl_trace.h
/usr/lib/tcl8.6/critcl-cutil0.2.1/trace/trace.c
/usr/lib/tcl8.6/critcl-emap1.2/emap.tcl
/usr/lib/tcl8.6/critcl-emap1.2/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-enum1.1/enum.tcl
/usr/lib/tcl8.6/critcl-enum1.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-iassoc1.1/iassoc.tcl
/usr/lib/tcl8.6/critcl-iassoc1.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-literals1.3/literals.tcl
/usr/lib/tcl8.6/critcl-literals1.3/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-platform1.0.15/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-platform1.0.15/platform.tcl
/usr/lib/tcl8.6/critcl-util1.1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl-util1.1/util.tcl
/usr/lib/tcl8.6/critcl3.1.18/Config
/usr/lib/tcl8.6/critcl3.1.18/critcl.tcl
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/cdata.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/header.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/pkginit.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/pkginitend.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/pkginittk.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/preload.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/storageclass.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/stubs.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/stubs_e.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/X.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/Xatom.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/Xfuncproto.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/Xlib.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/Xutil.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/cursorfont.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/keysym.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/keysymdef.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/X11/tkIntXlibDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tcl.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tclDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tclPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tk.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tkDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.4/tkPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/X.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/Xatom.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/Xfuncproto.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/Xlib.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/Xutil.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/cursorfont.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/keysym.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/keysymdef.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/X11/tkIntXlibDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tcl.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tclDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tclPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tk.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tkDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.5/tkPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/X.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/Xatom.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/Xfuncproto.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/Xlib.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/Xutil.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/cursorfont.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/keysym.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/keysymdef.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/X11/tkIntXlibDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tcl.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tclDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tclPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tk.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tkDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tcl8.6/tkPlatDecls.h
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tclAppInit.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tkstubs.c
/usr/lib/tcl8.6/critcl3.1.18/critcl_c/tkstubs_noconst.c
/usr/lib/tcl8.6/critcl3.1.18/license.terms
/usr/lib/tcl8.6/critcl3.1.18/pkgIndex.tcl
/usr/lib/tcl8.6/critcl_callback1/critcl-rt.tcl
/usr/lib/tcl8.6/critcl_callback1/license.terms
/usr/lib/tcl8.6/critcl_callback1/pkgIndex.tcl
/usr/lib/tcl8.6/critcl_callback1/teapot.txt
/usr/lib/tcl8.6/critcl_md5c0.12/critcl-rt.tcl
/usr/lib/tcl8.6/critcl_md5c0.12/license.terms
/usr/lib/tcl8.6/critcl_md5c0.12/pkgIndex.tcl
/usr/lib/tcl8.6/critcl_md5c0.12/teapot.txt
/usr/lib/tcl8.6/dict841/dict.tcl
/usr/lib/tcl8.6/dict841/pkgIndex.tcl
/usr/lib/tcl8.6/lassign841.0.1/lassign.tcl
/usr/lib/tcl8.6/lassign841.0.1/pkgIndex.tcl
/usr/lib/tcl8.6/lmap841/lmap.tcl
/usr/lib/tcl8.6/lmap841/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_container1/container.tcl
/usr/lib/tcl8.6/stubs_container1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_decl1/gen_decl.tcl
/usr/lib/tcl8.6/stubs_gen_decl1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_header1/gen_header.tcl
/usr/lib/tcl8.6/stubs_gen_header1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_init1/gen_init.tcl
/usr/lib/tcl8.6/stubs_gen_init1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_lib1/gen_lib.tcl
/usr/lib/tcl8.6/stubs_gen_lib1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_macro1/gen_macro.tcl
/usr/lib/tcl8.6/stubs_gen_macro1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_gen_slot1/gen_slot.tcl
/usr/lib/tcl8.6/stubs_gen_slot1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_genframe1/genframe.tcl
/usr/lib/tcl8.6/stubs_genframe1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_reader1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_reader1/reader.tcl
/usr/lib/tcl8.6/stubs_writer1/pkgIndex.tcl
/usr/lib/tcl8.6/stubs_writer1/writer.tcl

%files lib
%defattr(-,root,root,-)
/usr/lib/tcl8.6/critcl_callback1/linux-x86_64/callback.so
/usr/lib/tcl8.6/critcl_md5c0.12/linux-x86_64/md5c.so
