%global tl_name autofancyhdr
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Automatically compute headlength for fancyhdr package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autofancyhdr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autofancyhdr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autofancyhdr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package automatically computes headlength for the fancyhdr package

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/autofancyhdr
%dir %{_datadir}/texmf-dist/tex/latex/autofancyhdr
%doc %{_datadir}/texmf-dist/doc/latex/autofancyhdr/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/autofancyhdr/README.md
%{_datadir}/texmf-dist/tex/latex/autofancyhdr/autofancyhdr.sty
