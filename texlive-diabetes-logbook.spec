Name:		texlive-diabetes-logbook
Version:	54810
Release:	1
Summary:	A logbook for people with type one diabetes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/diabetes-logbook
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diabetes-logbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/diabetes-logbook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Initally a logbook for me, a person with type one diabetes
mellitus, this evolved over time into a TeX project, making it
prettier and/or easier to use. I've made it simple to use,
while not forgoing the document's beauty or the speed of input.
The logbook, with slight commenting out and editing, could be
used as a journal by anybody, although the template and
graphing functionality are set up for people using insulin
injections and blood glucose teststrips, as well as
counting/estimating carbs, protein, and fat. Note: The names of
the package's files are not constructed using the long
"diabetes-logbook", but the acronym "dmlb" (for "diabetes
mellitus log book").

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/diabetes-logbook
%doc %{_texmfdistdir}/doc/latex/diabetes-logbook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
