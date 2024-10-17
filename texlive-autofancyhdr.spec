Name:		texlive-autofancyhdr
Version:	54049
Release:	2
Summary:	Automatically compute headlength for fancyhdr package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autofancyhdr
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autofancyhdr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autofancyhdr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package automatically computes headlength for the fancyhdr
package

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/autofancyhdr
%doc %{_texmfdistdir}/doc/latex/autofancyhdr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
