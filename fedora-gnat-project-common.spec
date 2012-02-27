Name:           fedora-gnat-project-common
Version:        3.4
Release:        1%{?dist}
Summary:        Files shared by Ada libraries
Summary(sv):    Gemensamma filer för adabibliotek

Group:          System Environment/Libraries
License:        Copyright only
URL:            https://fedorahosted.org/released/fedora-gnat-project-common
Source1:        https://fedorahosted.org/released/fedora-gnat-project-common/download/fedora-gnat-project-common-%{version}.tar.gz
BuildArch:      noarch

Requires:       gcc-gnat setup
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=613407:
Requires:       libgnat-static
# macros.gnat requires __global_ldflags:
Requires:       redhat-rpm-config >= 9.1.0-13

%description
The fedora-gnat-project-common package contains files that are used by the GNAT
project files of multiple Ada libraries, and also GNAT-specific RPM macros.

%description -l sv
Paketet fedora-gnat-project-common innehåller filer som används av
GNAT-projektfilerna för flera adabibliotek, samt GNAT-specifika RPM-makron.

%global _GNAT_project_dir /usr/lib/gnat
# This is the directory where GNAT looks for project files by default, even on
# 64-bit systems.
# _GNAT_project_dir is defined here and copied from here to macros.gnat so that
# this package won't build-require itself.


%prep
%setup -q -T -b 1


%build
exec_prefix=%{_exec_prefix} bindir=%{_bindir} libexecdir=%{_libexecdir} includedir=%{_includedir} GNAT_project_dir=%{_GNAT_project_dir} ./configure


%install
mkdir --parents %{buildroot}%{_GNAT_project_dir} %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{_sysconfdir}/rpm/
cp -p directories.gpr %{buildroot}%{_GNAT_project_dir}/
cp -p gnat-project.sh gnat-project.csh %{buildroot}%{_sysconfdir}/profile.d/
cp -p macros.gnat %{buildroot}%{_sysconfdir}/rpm/


%files
%doc LICENSE
%{_GNAT_project_dir}
%config(noreplace) %{_sysconfdir}/profile.d/*
%config(noreplace) %{_sysconfdir}/rpm/*


%changelog
* Mon Feb 27 2012 Björn Persson <bjorn@rombobjörn.se> - 3.4-1
- Upgraded to version 3.4.
- Some compiler flags have been added to prevent dangerous suppression of
  important checks and avoid unnecessary build failures.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Björn Persson <bjorn@rombobjörn.se> - 3.3-1
- Upgraded to version 3.3 with GNAT_arches.

* Wed Aug 03 2011 Björn Persson <bjorn@rombobjörn.se> - 3.2-1
- Upgraded to version 3.2 with partial support for __global_ldflags.

* Sun May 22 2011 Björn Persson <bjorn@rombobjörn.se> - 3.1-1.1
- Removed some obsolete stuff.

* Tue May 03 2011 Björn Persson <bjorn@rombobjörn.se> - 3.1-1
- Upgraded to version 3.1.
- A configuration step has been added, so fewer directory names are hard-coded.
- There are now separate RPM macros with parameters for different tools in the
  GNAT toolchain.

* Wed Mar 03 2011 Björn Persson <bjorn@rombobjörn.se> - 2.2-1
- Updated to version 2.2 which is compatible with GPRbuild (bug 691558).

* Wed Feb 09 2011 Björn Persson <bjorn@rombobjörn.se> - 2.1-1
- Updated to version 2.1 with directories.gpr.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Björn Persson <bjorn@rombobjörn.se> - 1.2-2
- Worked around bug 613407.

* Tue Aug 04 2009 Björn Persson <bjorn@rombobjörn.se> - 1.2-1
- Updated to version 1.2 with a more complete list of processor architectures.

* Thu Jul 23 2009 Björn Persson <bjorn@rombobjörn.se> - 1.1-3
- Added a BuildRoot tag even though it's unnecessary.
- Removed a macro reference from the previous changelog entry.
- Silenced some RPMlint warnings.

* Fri Jul 03 2009 Björn Persson <bjorn@rombobjörn.se> - 1.1-2
- Renamed the package to fedora-gnat-project-common.
- There is now an "upstream" project at Fedora Hosted.
- Added a license file.
- Replaced "/etc" with _sysconfdir.

* Wed Jul 01 2009 Björn Persson <bjorn@rombobjörn.se> - 1-1
- ready to be submitted for review
