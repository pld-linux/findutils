#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	GNU Find Utilities (find, xargs)
Summary(de):	GNU-Suchprogramme (find, xargs)
Summary(es):	Utilitarios de b�squeda de la GNU
Summary(fr):	Utilitaires de recherche de GNU (find, xargs)
Summary(pl):	Narz�dzia GNU do odnajdywania plik�w (find, xargs)
Summary(pt_BR):	Utilit�rios de procura da GNU
Summary(tr):	GNU dosya arama ara�lar�
Name:		findutils
Version:	4.2.26
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/File
# development versions at ftp://alpha.gnu.org/gnu/findutils/
Source0:	ftp://ftp.gnu.org/gnu/findutils/%{name}-%{version}.tar.gz
# Source0-md5:	9ac4e62937b1fdc4eb643d1d4bf117d3
#Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	e76388b0c3218eec3557d05ccd6d6515
Patch0:		%{name}-info.patch
Patch1:		%{name}-selinux.patch
Patch2:		%{name}-man-selinux.patch
Patch3:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/findutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The findutils package contains programs which will help you locate
files on your system. The find utility searches through a hierarchy of
directories looking for files which match a certain set of criteria
(such as a filename pattern). The locate utility searches a database
(create by updatedb) to quickly find a file matching a given pattern.
The xargs utility builds and executes command lines from standard
input arguments (usually lists of file names generated by the find
command).

%description -l de
Das findutils-Paket enth�lt Programme, die dabei helfen, Dateien auf
Ihrem System zu finden. Das Find-Utility durchsucht die
Verzeichnishierarchie nach Dateien, die zu bestimmten Kriterien (z.B.
Dateiname) passen. Das locate-Utility durchsucht eine Datenbank
(erzeugt durch updatedb), um die Dateien schneller finden zu k�nnen.
xargs konstruiert Kommandozeilen von der Standardeingabe (z.B.
Dateilisten, die von find erzeugt werden), und f�hrt sie aus.

%description -l es
Este paquete contiene programas para ay�dalo a localizar archivos en
tu sistema. El programa find puede pesquisar, a trav�s de una
jerarqu�a de directorios, buscando por archivos que obedezcan a un
cierto conjunto de criterios (como nombre de archivo modelo).

%description -l fr
Ce package contient des programmes pour vous aider � localiser des
fichiers sur votre syst�me. Le programme find peut rechercher �
travers une hi�rarchie de r�pertoires des fichiers conformes �
certains crit�res (comme un type de nom).

%description -l pl
W pakiecie znajduj� si� narz�dzia pozwalaj�ce na poszukiwanie
okre�lonych plik�w. Program find s�u�y do poszukiwania w drzewie
katalog�w plik�w o okre�lonych parametrach, jak nazwa, uprawnienia,
typ czy data ostatniej modyfikacji.

%description -l pt_BR
Esse pacote cont�m programas para ajud�-lo a localizar arquivos em seu
sistema. O programa find pode procurar atrav�s de uma hierarquia de
diret�rios procurando por arquivos que obede�am um certo conjunto de
crit�rios (como nome de arquivo modelo).

%description -l tr
Bu pakette yer alan yaz�l�mlar sisteminizde yer alan dosyalar�
bulabilmeniz i�in haz�rlanm��lard�r. find program� ile belirli
�zellikleri olan bir yaz�l�m� bir dizin hiyerar�isi alt�nda
arayabilirsiniz.

%prep
%setup -q
%patch3 -p1
%patch0 -p1
%{?with_selinux:%patch1 -p1}
# patch2 is applied in install stage

rm -f po/stamp-po

%build
%{__aclocal} -I gnulib/m4 -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{?with_selinux:patch -p0 -d $RPM_BUILD_ROOT%{_mandir} < %{PATCH2}}

# xargs is wanted in /bin
install -d $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT%{_bindir}/xargs $RPM_BUILD_ROOT/bin

# unpackaged locate
rm -f $RPM_BUILD_ROOT%{_bindir}/{locate,updatedb} \
	$RPM_BUILD_ROOT%{_libdir}/{bigram,code,frcode} \
	$RPM_BUILD_ROOT%{_mandir}/{,*/}man?/{locate.1,updatedb.1,locatedb.5}*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/find
%attr(755,root,root) /bin/xargs

%{_mandir}/man1/[fx]*
%lang(de) %{_mandir}/de/man1/[fx]*
%lang(es) %{_mandir}/es/man1/[fx]*
%lang(fi) %{_mandir}/fi/man1/[fx]*
%lang(fr) %{_mandir}/fr/man1/[fx]*
%lang(hu) %{_mandir}/hu/man1/[fx]*
%lang(it) %{_mandir}/it/man1/[fx]*
%lang(ja) %{_mandir}/ja/man1/[fx]*
%lang(nl) %{_mandir}/nl/man1/[fx]*
%lang(pl) %{_mandir}/pl/man1/[fx]*
%lang(zh_CN) %{_mandir}/zh_CN/man1/[fx]*
%{_infodir}/find.info*
