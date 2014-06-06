# TODO:
# - cleanup
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtquick1
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qtscript_ver		%{version}
%define		qttools_ver		%{version}
%define		qtxmlpatterns_ver	%{version}
Summary:	The Qt5 Quick1 (Qt5Declarative) library
Summary(pl.UTF-8):	Biblioteka Qt5 Quick1 (Qt5Declarative)
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	4535ff78b5a9a18ffba702298a48e22e
URL:		http://qt-project.org/
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-qtbase-devel >= %{qtbase_ver}
BuildRequires:	qt5-qtdeclarative-devel >= %{qtdeclarative_ver}
BuildRequires:	qt5-qtscript-devel >= %{qtscript_ver}
BuildRequires:	qt5-qtxmlpatterns-devel >= %{qtdeclarative_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
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
Obsoletes:	qt5-qtquick1

%description -n Qt5Declarative
Qt5 Quick1 (Qt5Declarative) library FIXME.

%description -n Qt5Declarative -l pl.UTF-8
Biblioteka Qt5 Quick1 (Qt5Declarative).

%package -n Qt5Declarative-devel
Summary:	Qt5 Quick1 (Qt5Declarative) library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Quick1 (Qt5Declarative) - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	qt5-qtquick1-devel

%description -n Qt5Declarative-devel
Qt5 Quick1 (Qt5Declarative) library - development files.

%description -n Qt5Declarative-devel -l pl.UTF-8
Biblioteka Qt5 Quick1 (Qt5Declarative) - pliki programistyczne.

%package doc
Summary:	Qt5 Quick1 (Qt5Declarative) documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Quick1 (Qt5Declarative) w formacie HTML
Group:		Documentation
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

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

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

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Declarative -p /sbin/ldconfig
%postun	-n Qt5Declarative -p /sbin/ldconfig

%files -n Qt5Declarative
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Declarative.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Declarative.so.5
%attr(755,root,root) %{qt5dir}/bin/*
%attr(755,root,root) %{qt5dir}/imports
%attr(755,root,root) %{qt5dir}/plugins/*

%files -n Qt5Declarative-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Declarative.so
%{_libdir}/libQt5Declarative.prl
%{_includedir}/qt5/QtDeclarative
%{_pkgconfigdir}/Qt5Declarative.pc
%{_libdir}/cmake/Qt5Declarative
%{qt5dir}/mkspecs/modules/*.pri

%files examples -f examples.files
