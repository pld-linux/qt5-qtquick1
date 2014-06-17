#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtquick1
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qtscript_ver		%{version}
%define		qttools_ver		%{version}
%define		qtwebkit_ver		%{version}
%define		qtxmlpatterns_ver	%{version}
Summary:	The Qt5 Quick1 (Qt5Declarative) library
Summary(pl.UTF-8):	Biblioteka Qt5 Quick1 (Qt5Declarative)
Name:		qt5-%{orgname}
Version:	5.3.0
Release:	1
License:	LGPL v2 with Digia Qt LGPL Exception v1.1 or GPL v3
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	cd6ffd4a29f7050f71670e7afec09e5d
URL:		http://qt-project.org/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Designer-devel >= %{qttools_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qtbase_ver}
BuildRequires:	Qt5Script-devel >= %{qtscript_ver}
BuildRequires:	Qt5Sql-devel >= %{qtbase_ver}
BuildRequires:	Qt5WebKit-devel >= %{qtwebkit_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	Qt5XmlPatterns-devel >= %{qtxmlpatterns_ver}
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Quick1 (Qt5Declarative) library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 Quick1 (Qt5Declarative).

%package -n Qt5Declarative
Summary:	The Qt5 Quick1 (Qt5Declarative) library
Summary(pl.UTF-8):	Biblioteka Qt5 Quick1 (Qt5Declarative)
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Script >= %{qtscript_ver}
Requires:	Qt5Sql >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Requires:	Qt5XmlPatterns >= %{qtxmlpatterns_ver}
Obsoletes:	qt5-qtquick1

%description -n Qt5Declarative
Qt5 Quick1 (Qt5Declarative) library - an older version of Quick
library.

%description -n Qt5Declarative -l pl.UTF-8
Biblioteka Qt5 Quick1 (Qt5Declarative) - starsza wersja biblioteki
Quick.

%package -n Qt5Declarative-devel
Summary:	Qt5 Quick1 (Qt5Declarative) library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Quick1 (Qt5Declarative) - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Declarative = %{version}-%{release}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Script-devel >= %{qtscript_ver}
Requires:	Qt5Sql-devel >= %{qtbase_ver}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}
Requires:	Qt5XmlPatterns-devel >= %{qtxmlpatterns_ver}
Obsoletes:	qt5-qtquick1-devel

%description -n Qt5Declarative-devel
Qt5 Quick1 (Qt5Declarative) library - development files.

%description -n Qt5Declarative-devel -l pl.UTF-8
Biblioteka Qt5 Quick1 (Qt5Declarative) - pliki programistyczne.

%package -n Qt5Declarative-plugin-webkit
Summary:	WebKit plugin for Qt5 Quick1 library
Summary(pl.UTF-8):	Wtyczka WebKit dla biblioteki Qt5 Quick1
Group:		X11/Libraries
Requires:	Qt5Declarative = %{version}-%{release}
Requires:	Qt5WebKit >= %{qtwebkit_ver}
Obsoletes:	Qt5Declarative-webkit

%description -n Qt5Declarative-plugin-webkit
WebKit plugin for Qt5 Quick1 library.

%description -n Qt5Declarative-plugin-webkit -l pl.UTF-8
Wtyczka WebKit dla biblioteki Qt5 Quick1.

%package -n Qt5Designer-plugin-qdeclarativeview
Summary:	QDeclarativeView (Quick1) plugin for Qt5 Designer
Summary(pl.UTF-8):	Wtyczka QDeclarativeView (Quick1) dla Qt5 Designera
Group:		X11/Libraries
Requires:	Qt5Declarative = %{version}-%{release}
Requires:	Qt5Designer >= %{qttools_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}
Obsoletes:	Qt5Designer-qdeclarativeview

%description -n Qt5Designer-plugin-qdeclarativeview
QDeclarativeView (Quick1) plugin for Qt5 Designer.

%description -n Qt5Designer-plugin-qdeclarativeview -l pl.UTF-8
Wtyczka QDeclarativeView (Quick1) dla Qt5 Designera.

%package doc
Summary:	Qt5 Quick1 (Qt5Declarative) documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Quick1 (Qt5Declarative) w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Quick1 (Qt5Declarative) documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 Quick1 (Qt5Declarative) w formacie
HTML.

%package doc-qch
Summary:	Qt5 Quick1 (Qt5Declarative) documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Quick1 (Qt5Declarative) w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 Quick1 (Qt5Declarative) documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 Quick1 (Qt5Declarative) w formacie QCH.

%package examples
Summary:	Qt5 Quick1 (Qt5Declarative) examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 Quick1 (Qt5Declarative)
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Quick1 (Qt5Declarative) examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 Quick1 (Qt5Declarative).

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

# enable docs
%{__sed} -i -e '/^# SUBDIRS += doc/s/^# //' src/src.pro

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
install -d $RPM_BUILD_ROOT%{_bindir}
for f in qml1plugindump qmlviewer ; do
	ln -sf ../%{_lib}/qt5/bin/$f $RPM_BUILD_ROOT%{_bindir}/${f}-qt5
done

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/declarative

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Declarative -p /sbin/ldconfig
%postun	-n Qt5Declarative -p /sbin/ldconfig

%files -n Qt5Declarative
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt dist/changes-*
%attr(755,root,root) %{_libdir}/libQt5Declarative.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Declarative.so.5
%attr(755,root,root) %{_bindir}/qml1plugindump-qt5
%attr(755,root,root) %{_bindir}/qmlviewer-qt5
%attr(755,root,root) %{qt5dir}/bin/qml1plugindump
%attr(755,root,root) %{qt5dir}/bin/qmlviewer
%dir %{qt5dir}/imports
%{qt5dir}/imports/builtins.qmltypes
%dir %{qt5dir}/imports/Qt
%dir %{qt5dir}/imports/Qt/labs
%dir %{qt5dir}/imports/Qt/labs/folderlistmodel
%attr(755,root,root) %{qt5dir}/imports/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
%{qt5dir}/imports/Qt/labs/folderlistmodel/plugins.qmltypes
%{qt5dir}/imports/Qt/labs/folderlistmodel/qmldir
%dir %{qt5dir}/imports/Qt/labs/gestures
%attr(755,root,root) %{qt5dir}/imports/Qt/labs/gestures/libqmlgesturesplugin.so
%{qt5dir}/imports/Qt/labs/gestures/plugins.qmltypes
%{qt5dir}/imports/Qt/labs/gestures/qmldir
%dir %{qt5dir}/imports/Qt/labs/particles
%attr(755,root,root) %{qt5dir}/imports/Qt/labs/particles/libqmlparticlesplugin.so
%{qt5dir}/imports/Qt/labs/particles/plugins.qmltypes
%{qt5dir}/imports/Qt/labs/particles/qmldir
%dir %{qt5dir}/imports/Qt/labs/shaders
%attr(755,root,root) %{qt5dir}/imports/Qt/labs/shaders/libqmlshadersplugin.so
%{qt5dir}/imports/Qt/labs/shaders/plugins.qmltypes
%{qt5dir}/imports/Qt/labs/shaders/qmldir
%dir %{qt5dir}/plugins/qml1tooling
%attr(755,root,root) %{qt5dir}/plugins/qml1tooling/libqmldbg_inspector.so
%attr(755,root,root) %{qt5dir}/plugins/qml1tooling/libqmldbg_tcp_qtdeclarative.so

%files -n Qt5Declarative-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Declarative.so
%{_libdir}/libQt5Declarative.prl
%{_includedir}/qt5/QtDeclarative
%{_pkgconfigdir}/Qt5Declarative.pc
%dir %{_libdir}/cmake/Qt5Declarative
%{_libdir}/cmake/Qt5Declarative/Qt5DeclarativeConfig*.cmake
%{_libdir}/cmake/Qt5Declarative/Qt5Declarative_QTcpServerConnection.cmake
%{_libdir}/cmake/Qt5Declarative/Qt5Declarative_QtQuick1Plugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_declarative.pri
%{qt5dir}/mkspecs/modules/qt_lib_declarative_private.pri

%files -n Qt5Declarative-plugin-webkit
%defattr(644,root,root,755)
%dir %{qt5dir}/imports/QtWebKit
%attr(755,root,root) %{qt5dir}/imports/QtWebKit/libqmlwebkitplugin.so
%{qt5dir}/imports/QtWebKit/plugins.qmltypes
%{qt5dir}/imports/QtWebKit/qmldir

%files -n Qt5Designer-plugin-qdeclarativeview
%defattr(644,root,root,755)
%attr(755,root,root) %{qt5dir}/plugins/designer/libqdeclarativeview.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QDeclarativeViewPlugin.cmake

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtdeclarative

%if %{with qch}
%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtdeclarative.qch
%endif

%files examples -f examples.files
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
