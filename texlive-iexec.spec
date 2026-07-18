%global tl_name iexec
%global tl_revision 79681

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.16.1
Release:	%{tl_revision}.1
Summary:	Execute shell commands and input their output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/iexec
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With the help of the \iexec command, you can execute a shell command and
then input its output into your document. This package also lets you use
any special symbols inside your command.

