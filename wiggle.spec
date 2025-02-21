%define	name wiggle
%define	version	0.9
%define release	2

Summary: 	A tool for applying patches with conflicts
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
License: 	GPL
Group:		Text tools
Source0:	http://neil.brown.name/wiggle/%{name}-%{version}.tar.gz
Patch1:		wiggle-fix-build.patch
Url:		https://neil.brown.name/wiggle
BuildRequires:	groff-for-man
BuildRequires:	ncurses-devel

%description
Wiggle is a program for applying patches that 'patch' cannot
apply due to conflicting changes in the original.
Wiggle will always apply all changes in the patch to the original.
If it cannot find a way to cleanly apply a patch, it inserts it
in the original in a manner similar to 'merge', and report an
unresolvable conflict.  Such a conflict will look like:

%prep
%setup -q
bzip2 DOC/diff.ps


# Don't add Neil Brown's default sign off line to every patch
sed -i '/$CERT/,+4s,^,#,' p || die "sed failed on p"



%build
%make

%install
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1
install -m755 wiggle %buildroot/%{_bindir}/wiggle
install -m644 wiggle.1 %buildroot/%{_mandir}/man1/wiggle.1

%files
%doc ANNOUNCE TODO notes DOC/diff.ps.bz2
%doc p p.help
%attr (755,root,root) %{_bindir}/wiggle
%{_mandir}/man1/wiggle.1*



%changelog
* Thu Jun 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9-1
+ Revision: 805628
- version update 0.9

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.6-8mdv2010.0
+ Revision: 434752
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.6-7mdv2009.0
+ Revision: 261984
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6-6mdv2009.0
+ Revision: 255989
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2008.1
+ Revision: 135619
- patch 1: fix build
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import wiggle

