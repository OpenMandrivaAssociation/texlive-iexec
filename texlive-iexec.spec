Name:		texlive-iexec
Version:	64908
Release:	2
Summary:	Execute shell commands and input their output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iexec
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iexec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With the help of the \iexec command, you can execute a shell
command and then input its output into your document. This
package also lets you use any special symbols inside your
command.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/iexec
%{_texmfdistdir}/tex/latex/iexec
%doc %{_texmfdistdir}/doc/latex/iexec

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
