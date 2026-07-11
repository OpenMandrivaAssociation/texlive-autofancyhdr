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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package automatically computes headlength for the fancyhdr package

