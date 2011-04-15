Name:           fedora-gnat-project-common
Version:        2.3
Release:        1%{?dist}
Summary:        Files shared by Ada libraries
Summary(sv):    Gemensamma filer för adabibliotek

Group:          System Environment/Libraries
License:        Copyright only
URL:            https://fedorahosted.org/released/fedora-gnat-project-common
Source1:        https://fedorahosted.org/released/fedora-gnat-project-common/download/fedora-gnat-project-common-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       gcc-gnat setup
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=613407:
Requires:       libgnat-static

%description
The fedora-gnat-project-common package contains files that are used by the GNAT
project files of multiple Ada libraries, and also GNAT-specific RPM macros.

%description -l sv
Paketet fedora-gnat-project-common innehåller filer som används av
GNAT-projektfilerna för flera adabibliotek, samt GNAT-specifika RPM-makron.

# Extract the GNAT project file location from the file of macro definitions so
# that this package won't build-require itself.
%global _GNAT_project_dir %(tar --extract --gzip --to-stdout --no-anchored --file=%{SOURCE1} macros.gnat | grep ^._GNAT_project_dir | sed 's/[^ ]* *//')


%prep
%setup -q -T -b 1


%build
# nothing to do


%install
rm -rf %{buildroot}
mkdir --parents %{buildroot}%{_GNAT_project_dir} %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{_sysconfdir}/rpm/
cp -p common.gpr directories.gpr %{buildroot}%{_GNAT_project_dir}/
cp -p gnat-project.sh gnat-project.csh %{buildroot}%{_sysconfdir}/profile.d/
cp -p macros.gnat %{buildroot}%{_sysconfdir}/rpm/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_GNAT_project_dir}
%config(noreplace) %{_sysconfdir}/profile.d/*
%config(noreplace) %{_sysconfdir}/rpm/*


%changelog
* Wed Apr 15 2011 Björn Persson <bjorn@rombobjörn.se> - 2.3-1
- Updated to version 2.3 to get binder files back in debuginfo packages.

* Wed Apr 03 2011 Björn Persson <bjorn@rombobjörn.se> - 2.2-1
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
