Name:           etherape
Version:        0.9.7 
Release:        11%{?dist}
Summary:        Graphical network monitor for Unix

Group:          Applications/System
License:        GPLv2+
URL:            http://etherape.sourceforge.net/
Source0:        http://umn.dl.sourceforge.net/sourceforge/etherape/%{name}-%{version}.tar.gz
Source1:        etherape.pam
Source2:        etherape.console
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libpcap-devel, libglade2-devel
BuildRequires:  gettext, desktop-file-utils, libgnomeui-devel 
BuildRequires:  scrollkeeper
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
EtherApe is a graphical network monitor modeled after etherman. 

%prep
%setup -q


%build
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/etherape
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/etherape
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
ln -s consolehelper $RPM_BUILD_ROOT/%{_bindir}/etherape

%find_lang %{name}
desktop-file-install --vendor "fedora"  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/etherape.desktop

rm $RPM_BUILD_ROOT/%{_datadir}/applications/etherape.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING FAQ NEWS OVERVIEW README README.bugs README.help README.thanks TODO


%{_bindir}/etherape
%{_sbindir}/etherape

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/services
%config(noreplace) %{_sysconfdir}/pam.d/etherape
%config(noreplace) %{_sysconfdir}/security/console.apps/etherape
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/doc
%dir %{_datadir}/%{name}/doc/%{name}
%dir %{_datadir}/%{name}/doc/%{name}/C
%{_datadir}/%{name}/doc/%{name}/C/etherape.xml
%dir %{_datadir}/%{name}/doc/%{name}/C/figures
%{_datadir}/%{name}/doc/%{name}/C/figures/appmain.png
%{_datadir}/%{name}/doc/%{name}/C/figures/capture_file_dlg.png
%{_datadir}/%{name}/doc/%{name}/C/figures/color_select_dlg.png
%{_datadir}/%{name}/doc/%{name}/C/figures/eth_toolbar.png
%{_datadir}/%{name}/doc/%{name}/C/figures/link_info.png
%{_datadir}/%{name}/doc/%{name}/C/figures/node_info.png
%{_datadir}/%{name}/doc/%{name}/C/figures/pref_colors_dlg.png
%{_datadir}/%{name}/doc/%{name}/C/figures/pref_diagram_dlg.png
%{_datadir}/%{name}/doc/%{name}/C/figures/pref_timings_dlg.png
%{_datadir}/%{name}/doc/%{name}/C/figures/proto_info.png
%{_datadir}/%{name}/doc/%{name}/C/figures/protocol_edit_dlg.png
%dir %{_datadir}/%{name}/glade
%{_datadir}/%{name}/glade/etherape.glade2
%{_datadir}/%{name}/glade/etherape.png
%{_datadir}/%{name}/glade/pause.xpm
%{_datadir}/%{name}/glade/play.xpm
%{_datadir}/%{name}/glade/stop.xpm
%{_datadir}/applications/fedora-etherape.desktop
%{_datadir}/pixmaps/etherape.png
%dir %{_datadir}/omf/etherape
%{_datadir}/omf/etherape/etherape-C.omf
%{_mandir}/man1/*

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :


%changelog
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.7-9
- fix license tag

* Sat Apr 19 2008 Michael Rice <errr@errr-online.com> - 0.9.7-8
- fix ln -s 

* Sat Apr 19 2008 Michael Rice <errr[AT]errr-online.com> - 0.9.7-7
- Fix #442131 problems running as non root

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.7-6
- Autorebuild for GCC 4.3

* Wed Apr 11 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-5
- Rebuild to get all matching version from FC-5 .. devel

* Mon Feb 12 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-4
- Fix desktop file install

* Sat Feb 10 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-3
- Add scrollkeeper post and postun script snips
- Fix dir ownership or pixmaps and omf
- Fix .desktop X category

* Wed Jan 31 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-2
- Fix dup BR's 
- add missing BR for libgnomeui-devel scrollkeeper
- removed %%{buildroot}. in choice of other

* Wed Jan 24 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-1
- Initial RPM release
