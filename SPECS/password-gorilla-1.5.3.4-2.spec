Buildroot: /home/staff/jdunn/devel/alien/password-gorilla-1.5.3.4
Name: password-gorilla
Version: 1.5.3.4
Release: 2
Summary: cross-platform password manager
License: see /usr/share/doc/password-gorilla/copyright
Distribution: Debian
Group: Converted/x11

%define _rpmdir ../
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%define _unpackaged_files_terminate_build 0

%post
#!/bin/sh
set -e
# Automatically added by dh_installmenu
if [ "$1" = "configure" ] && [ -x "`which update-menus 2>/dev/null`" ]; then
	update-menus
fi
# End automatically added section


%postun
#!/bin/sh
set -e
# Automatically added by dh_installmenu
if [ -x "`which update-menus 2>/dev/null`" ]; then update-menus ; fi
# End automatically added section


%description
The Password Gorilla helps you manage your logins. It stores all your
user names and passwords, along with login information and other
notes, in a securely encrypted file. A single "master password" is
used to protect the file. This way, you only need to remember the
single master password, instead of the many logins that you use.

If you want to log in to a service or Web site, the Password Gorilla
copies your user name and password to the clipboard, so that you can
easily paste it into your Web browser or other application. Because
the password does not appear on the screen, Password Gorilla is safe
to use in the presence of others.

The convenience of Password Gorilla allows you to choose different,
non-intuitive passwords for each service. An integrated random
password generator can provide one-time passwords, tunable to various
services' policies.

Password Gorilla is a tcl/tk application which can run on Linux and
Windows, and the files written are supposed to be compatible between
platforms. This is important for collaboration in heterogenous
environments.


(Converted from a deb package by alien version unknown.)

%files
%dir "/"
%dir "/usr/"
%dir "/usr/share/"
%dir "/usr/share/icons/"
%dir "/usr/share/icons/hicolor/"
%dir "/usr/share/icons/hicolor/48x48/"
"/usr/share/icons/hicolor/48x48/password-gorilla.png"
%dir "/usr/share/icons/hicolor/16x16/"
"/usr/share/icons/hicolor/16x16/password-gorilla.png"
%dir "/usr/share/icons/hicolor/32x32/"
"/usr/share/icons/hicolor/32x32/password-gorilla.png"
%dir "/usr/share/applications/"
"/usr/share/applications/password-gorilla.desktop"
%dir "/usr/share/pixmaps/"
"/usr/share/pixmaps/password-gorilla.xpm"
%dir "/usr/share/doc/"
%dir "/usr/share/doc/password-gorilla/"
"/usr/share/doc/password-gorilla/changelog.Debian.gz"
"/usr/share/doc/password-gorilla/copyright"
"/usr/share/doc/password-gorilla/changelog.gz"
%dir "/usr/share/man/"
%dir "/usr/share/man/man1/"
"/usr/share/man/man1/password-gorilla.1.gz"
%dir "/usr/share/password-gorilla/"
%dir "/usr/share/password-gorilla/twofish/"
"/usr/share/password-gorilla/twofish/f32-critcl.tcl"
"/usr/share/password-gorilla/twofish/twofish.tcl"
"/usr/share/password-gorilla/twofish/pkgIndex.tcl"
"/usr/share/password-gorilla/twofish/twotest.tcl"
%dir "/usr/share/password-gorilla/blowfish/"
"/usr/share/password-gorilla/blowfish/blowfish.tcl"
"/usr/share/password-gorilla/blowfish/pkgIndex.tcl"
"/usr/share/password-gorilla/blowfish/blowtest.tcl"
"/usr/share/password-gorilla/viewhelp.tcl"
%dir "/usr/share/password-gorilla/msgs/"
"/usr/share/password-gorilla/msgs/de.msg"
"/usr/share/password-gorilla/msgs/ru.msg"
%dir "/usr/share/password-gorilla/tooltip/"
"/usr/share/password-gorilla/tooltip/tooltip.tcl"
"/usr/share/password-gorilla/tooltip/tipstack.tcl"
"/usr/share/password-gorilla/tooltip/pkgIndex.tcl"
%dir "/usr/share/password-gorilla/pwsafe/"
"/usr/share/password-gorilla/pwsafe/pwsafe-db.tcl"
"/usr/share/password-gorilla/pwsafe/pwsafe-v2.tcl"
"/usr/share/password-gorilla/pwsafe/pwsafe.tcl"
"/usr/share/password-gorilla/pwsafe/pwtest.tcl"
"/usr/share/password-gorilla/pwsafe/pwsafe-io.tcl"
"/usr/share/password-gorilla/pwsafe/pkgIndex.tcl"
"/usr/share/password-gorilla/pwsafe/pwsafe-int.tcl"
"/usr/share/password-gorilla/pwsafe/pwsafe-v3.tcl"
"/usr/share/password-gorilla/non-modal.tcl"
"/usr/share/password-gorilla/help.txt"
"/usr/share/password-gorilla/isaac.tcl"
"/usr/share/password-gorilla/gorilla.tcl"
%dir "/usr/share/menu/"
"/usr/share/menu/password-gorilla"
%dir "/usr/bin/"
"/usr/bin/password-gorilla"
"/usr/share/doc/password-gorilla/help.txt"
"/usr/share/password-gorilla/LICENSE.txt"
