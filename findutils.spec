Summary:	GNU Find Utilities (find, xargs, and locate)
Summary(de):	GNU-Suchprogramme (find, xargs und locate)
Summary(fr):	Utilitaires de recherche de GNU (find, xargs, et locate)
Summary(pl):	GNU narzêdzia do odnajdywania plików (find, xargs i locate)
Summary(tr):	GNU dosya arama araçlarý
Name:		findutils
Version:	4.1
Release:	33
Copyright:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	ftp://prep.ai.mit.edu/pub/gnu/findutils/%{name}-%{version}.tar.gz
Source1:	updatedb.cron
Patch0:		findutils-info.patch
Patch1:		findutils-basename.patch
Patch2:		findutils-glibc.patch
patch3:		findutils-glibc21.patch
Patch4:		findutils-xargsoverflow.patch
Patch5:		findutils-pl_manpages.patch
BuildRequires:	texinfo
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package contains programs to help you locate files on your system. The
find program can search through a hierarchy of directories looking for files
matching a certain set of criteria (such as a filename pattern).

%description -l de
Dieses Paket enthält Programme zum Suchen von Dateien auf
dem System. Das Programm 'find' kann eine Verzeichnisstruktur
durchsuchen und Dateien finden, die den Suchkritierien entsprechen
(z.B. einem Dateinamenmuster).

%description -l fr
Ce package contient des programmes pour vous aider à localiser
des fichiers sur votre système. Le programme find peut rechercher
à travers une hiérarchie de répertoires des fichiers conformes à
certains critères (comme un type de nom).

%description -l pl
W pakiecie znajduj± siê narzêdzia pozwalaj±ce na poszukiwanie okre¶lonych
plików. Program find s³u¿y do przeszukania drzewa katalogów za plikami o
okre¶lonych parametrach, jak nazwa, uprawnienia, typ, data ostatniej
modyfikacji.

%description -l tr
Bu pakette yer alan yazýlýmlar sisteminizde yer alan dosyalarý bulabilmeniz
için hazýrlanmýþlardýr. find programý ile belirli özellikleri olan bir
yazýlýmý bir dizin hiyerarþisi altýnda arayabilirsiniz.

%prep
%setup  -q
%patch0 -p1 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoconf
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}
	
install pl/*.1  $RPM_BUILD_ROOT%{_mandir}/pl/man1

gzip -9fn $RPM_BUILD_ROOT%{_infodir}/find.info* \
	$RPM_BUILD_ROOT%{_mandir}/{man?/*,pl/man1/*} \
	NEWS README TODO ChangeLog

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/find
%attr(755,root,root) %{_bindir}/xargs

%{_mandir}/man1/find.1*
%{_mandir}/man1/xargs.1*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/find.info*
