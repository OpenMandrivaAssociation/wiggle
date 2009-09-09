%define	name wiggle
%define	version	0.6
%define	release	%mkrel 8

Summary: 	A tool for applying patches with conflicts
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
License: 	GPL
Group:		Text tools
Source:		http://cgi.cse.unsw.edu.au/~neilb/source/wiggle/wiggle-%{version}.tar.bz2
#Patch:		wiggle-p.patch.bz2
Patch1:		wiggle-fix-build.patch
Url:		http://cgi.cse.unsw.edu.au/~neilb/source/wiggle
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	groff-for-man

%description
Wiggle is a program for applying patches that 'patch' cannot
apply due to conflicting changes in the original.
Wiggle will always apply all changes in the patch to the original.
If it cannot find a way to cleanly apply a patch, it inserts it
in the original in a manner similar to 'merge', and report an
unresolvable conflict.  Such a conflict will look like:

%prep
%setup -q
#patch -p1
%patch1 -p1
bzip2 DOC/diff.ps

%build
%make OptDbg="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man1
install -m755 wiggle %buildroot/%{_bindir}/wiggle
install -m644 wiggle.1 %buildroot/%{_mandir}/man1/wiggle.1

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE TODO notes DOC/diff.ps.bz2
%doc p p.help
%attr (755,root,root) %{_bindir}/wiggle
%{_mandir}/man1/wiggle.1*

