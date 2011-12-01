%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Python bindings for gtkextra
Name: python-gtkextra
Version: 1.1.0
Release: 10%{?dist}
# FIXME: the license is not quite clear, using the most restrictive license
# for this field.  See
# http://sourceforge.net/tracker/index.php?func=detail&aid=1941652&group_id=35371&atid=414148
License: GPLv2
URL: http://python-gtkextra.sourceforge.net
Group: Development/Libraries
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: python-gtkextra-1.1.0-update.patch
Patch1: python-gtkextra-1.1.0-codegenmoved.patch
# https://sourceforge.net/tracker/?func=detail&aid=2805069&group_id=35371&atid=414148
Patch2: python-gtkextra-1.1.0-Makefile.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: gtk+extra-devel, pygtk2-devel, python-devel
# For autoreconf
BuildRequires: autoconf, automake, libtool
Requires: pygtk2, pkgconfig

%description
This package provides a Python interface to the GtkExtra2 widget set for GTK2.

%prep
%setup -q
%patch0 -p1 -b .update
%patch1 -p1 -b .codegenmoved
%patch2 -p1 -b .Makefile
autoreconf -fi

%build

%configure --disable-numpy
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# Install __init__.py and _config.py to %{python_sitearch}
make install DESTDIR=$RPM_BUILD_ROOT \
	pygtkextradir='$(pyexecdir)/gtk-2.0/gtkextra'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{python_sitearch}/gtk-2.0/gtkextra
%exclude %{python_sitearch}/gtk-2.0/gtkextra/_gtkextramodule.la
%{_libdir}/pkgconfig/python-gtkextra.pc
%{_datadir}/pygtk/2.0/defs/gtkextra*.defs

%changelog
* Thu Oct 15 2009 Miloslav Trmač <mitr@redhat.com> - 1.1.0-10
- Add dist tag

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Miloslav Trmač <mitr@redhat.com> - 1.1.0-8
- Fix build on rawhide

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  9 2009 Miloslav Trmač <mitr@redhat.com> - 1.1.0-6
- More general fix for the codegen move

* Wed Jan 07 2009 Caolán McNamara <caolanm@redhat.com> - 1.1.0-5
- codegen moved from pygtk to pygobject, fix to rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1.0-4
- Rebuild for Python 2.6

* Sat Apr 19 2008 Miloslav Trmač <mitr@redhat.com> - 1.1.0-3
- Make it actually work on 64-bit systems

* Fri Apr 18 2008 Miloslav Trmač <mitr@redhat.com> - 1.1.0-2
- Fix build on 64-bit systems

* Mon Apr 14 2008 Miloslav Trmač <mitr@redhat.com> - 1.1.0-1
- Clean up for package review.

* Fri Oct 19 2007 Miloslav Trmač <mitr@redhat.com> - 1.1.0-0.mitr.1
- Initial package.
