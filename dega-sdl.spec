Summary: Dega is a Sega Master System emulator
Name: dega-sdl
Version: 1.12
Release: 24%{?dist}
License: Distributable
Group: Applications/Emulators
URL: http://www.emulinks.de/emus/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.emulinks.de/emus/dega-%{version}.tar.gz
Patch0: dega-1.12-execstack.patch
Patch1: dega-1.12-Makefile.patch
# This is to build only for i386/i686 on plague
ExclusiveArch: i686
BuildRequires: SDL-devel >= 1.2.0, nasm, gcc-c++

%description
Dega/SDL is a Linux port to the original Dega Sega 
Master System / Mark III / Game Gear emulator for DOS. 

%prep
%setup -q -n dega-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Using Fedora OPTFLAGS
sed -i 's/^OPTFLAGS=/#OPTFLAGS=/' Makefile

%build
export OPTFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 dega %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{_bindir}/dega
%doc README dega.txt ChangeLog

%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.12-13
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.12-8
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Feb 12 2012 Andrea Musuruane <musuruan@gmail.com> 1.12-7
- patched Makefile to link against libm

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Fix default arch

* Sat Mar 28 2009 Andrea Musuruane <musuruan@gmail.com> 1.12-5
- fixed ExclusiveArch for F11

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.12-4
- rebuild for buildsys cflags issue

* Sat Jul 26 2008 Andrea Musuruane <musuruan@gmail.com> 1.12-3
- used a workaround to build only for i386 on plague

* Mon Sep 17 2007 Andrea Musuruane <musuruan@gmail.com> 1.12-2
- added missing %%{?dist} tag in the release field
- using standard Fedora flags for compiling

* Sun Sep 16 2007 Andrea Musuruane <musuruan@gmail.com> 1.12-1
- updated to upstream version 1.12
- removed no longer used patch
- removed %%{?dist} tag from changelog

* Mon Nov 13 2006 Andrea Musuruane <musuruan@gmail.com> 1.07-2
- changed the License tag to "Distributable"
- Source tag now links upstream source package
- no longer using %%{version} in Patch0 (to apply the exact same patch
  to a future version)
- replaced %%{__sed} with sed in %%prep
- added a patch from Hans de Goede to fix unnecessary claims to require 
  an execstack, no longer breaking SELinux

* Sun Nov 12 2006 Andrea Musuruane <musuruan@gmail.com> 1.07-1
- compiled for Fedora Core 6
- changed Group to match a Fedora RPM group
- added full URL to Source tag
- changed BuildRoot to meet Fedora guidelines
- removed Prefix tag
- removed unneeded allegro dependency
- added ExclusiveArch
- cleaned %%prep section
- converted dega.txt to UNIX end-of-line-encoding
- added %%{?_smp_mflags} to make invocation to speed up SMP builds

* Sun Sep 26 2004 Sebastien Corot <scorot@libertysurf.fr>
- first spec file
- compiled for SuSE Linux 9.1
