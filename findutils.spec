Summary:     GNU Find Utilities (find, xargs, and locate)
Summary(de): GNU-Suchprogramme (find, xargs und locate)
Summary(fr): Utilitaires de recherche de GNU (find, xargs, et locate)
Summary(pl): GNU narzêdzia do odnajdywania plików (find, xargs i locate)
Summary(tr): GNU dosya arama araçlarý
Name:        findutils
Version:     4.1
Release:     28
Copyright:   GPL
Group:       Utilities/File
Group(pl):   Narzêdzia/Pliki
Source0:     ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:     updatedb.cron
Source2:     xargs.1.pl
Patch0:      findutils.patch
Patch1:      findutils-info.patch
Prereq:      /sbin/install-info
Requires:    mktemp
Buildroot:   /tmp/%{name}-%{version}-root

%description
This package contains programs to help you locate files on your system. The
find program can search through a hierarchy of directories looking for files
matching a certain set of criteria (such as a filename pattern). The locate
program searches a database (create by updatedb) to quickly find a file
matching a given pattern.

%description -l de
Dieses Paket enthält Programme zum Suchen von Dateien auf
dem System. Das Programm 'find' kann eine Verzeichnisstruktur
durchsuchen und Dateien finden, die den Suchkritierien entsprechen
(z.B. einem Dateinamenmuster). Das Programm 'locate' durchsucht
eine Datenbank (durch updatedb erstellt), um eine Datei, die dem
Suchmuster entspricht, zu finden.

%description -l fr
Ce package contient des programmes pour vous aider à localiser
des fichiers sur votre système. Le programme find peut rechercher
à travers une hiérarchie de répertoires des fichiers conformes à
certains critères (comme un type de nom). Le programme locatecherche 
une base de données (crée par updatedb) pour trouver rapidement
un fichier correspondant au type demandé.

%description -l pl
W pakiecie znajduj± siê narzêdzia pozwalaj±ce na poszukiwanie okre¶lonych
plików. Program find s³u¿y do przeszukania drzewa katalogów za plikami o
okre¶lonych parametrach, jak nazwa, uprawnienia, typ, data ostatniej
modyfikacji. Program locate lokalizuje pliki korzystaj±c z utworzonej
poleceniem updatedb bazy danych, dziêki czemu jest znacznie szybszy od find.

%description -l tr
Bu pakette yer alan yazýlýmlar sisteminizde yer alan dosyalarý bulabilmeniz
için hazýrlanmýþlardýr. find programý ile belirli özellikleri olan bir
yazýlýmý bir dizin hiyerarþisi altýnda arayabilirsiniz. locate yazýlýmý ise,
updatedb tarafýndan hazýrlanan bir veri tabaný üzerinde, belirtilen
dosyalarý arar.

%prep
%setup -q
%patch0 -p1 
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--exec-prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib/findutils,man/{man[15],pl/man1}} \
	$RPM_BUILD_ROOT/etc/cron.daily

make 	prefix=$RPM_BUILD_ROOT/usr \
	exec_prefix=$RPM_BUILD_ROOT/usr \
	install
	
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily
install %{SOURCE2} $RPM_BUILD_ROOT/usr/man/pl/man1/xargs.1

gzip -9fn $RPM_BUILD_ROOT/usr/info/find.info* \
	$RPM_BUILD_ROOT/usr/man/{man[15]/*,pl/man1/*} \
	NEWS README TODO ChangeLog

%post
/sbin/install-info /usr/info/find.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
    /sbin/install-info --delete /usr/info/find.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README,TODO,ChangeLog}.gz
%attr(750,root,root) %config /etc/cron.daily/updatedb.cron
%attr(755,root,root) /usr/bin/*

%dir /usr/lib/findutils
%attr(755,root,root) /usr/lib/findutils/*

/usr/info/find.info*
/usr/man/man[15]/*

%lang(pl) /usr/man/pl/man1/*

%changelog
* Tue Apr  5 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [4.1-28]
- revision up to 28,
- added Group(pl),
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- removed 'rm -rf $RPM_BUILD_ROOT' from %build,
- simplifications in %install,
- standarized {un}registering info pages (added findutils-info.patch),
- added more documentation,
- added pl man page for xargs(1L),
- added gzipping documentation and man pages.

* Sun Oct  4 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.26]
- changed way passing $RPM_OPT_FLAGS.

* Fri Jun 12 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.1.26d]
- added pl translation (made by Piotr Dembiñski <hektor@kki.net.pl>),
- macro %%{name}-%%{version} in Source,
- minor modifications of spec file.

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- updated updatedb cron script to not look for $TMPNAME.n (which was
  a relic anyway)
- added -b parameters to all of the patches

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Mar 09 1998 Michael K. Johnson <johnsonm@redhat.com>
- make updatedb.cron use mktemp correctly
- make updatedb use mktemp

* Sun Nov 09 1997 Michael K. Johnson <johnsonm@redhat.com>
- nobody should own tmpfile
- ignore /net

* Wed Nov 05 1997 Michael K. Johnson <johnsonm@redhat.com>
- made updatedb.cron do a better job of cleaning up after itself.

* Tue Oct 28 1997 Donald Barnes <djb@redhat.com>
- fixed 64 bit-ism in getline.c, patch tacked on to end of glibc one

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- added patch for glibc 2.1

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot support

* Tue Oct 14 1997 Michael K. Johnson <johnsonm@redhat.com>
- made updatedb.cron work even if "nobody" can't read /root
- use mktemp in updatedb.cron

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- added missing info pages
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built with glibc

* Mon Apr 21 1997 Michael K. Johnson <johnsonm@redhat.com>
- fixed updatedb.cron
