Name:           etherape
Version:        0.9.7 
Release:        5%{?dist}
Summary:        Graphical network monitor for Unix

Group:          Applications/System
License:        GPL
URL:            http://etherape.sourceforge.net/
Source0:        http://umn.dl.sourceforge.net/sourceforge/etherape/%{name}-%{version}.tar.gz
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
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
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

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/services

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
