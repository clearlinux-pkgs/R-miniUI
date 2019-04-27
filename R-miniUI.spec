#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-miniUI
Version  : 0.1.1.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/miniUI_0.1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/miniUI_0.1.1.1.tar.gz
Summary  : Shiny UI Widgets for Small Screens
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-htmltools
BuildRequires : R-httpuv
BuildRequires : R-mime
BuildRequires : R-shiny
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
# miniUI
Provides UI widget and layout functions for writing Shiny apps that work well on small screens. Designed to work especially well for creating Shiny Gadgets.

%prep
%setup -q -c -n miniUI

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552884614

%install
export SOURCE_DATE_EPOCH=1552884614
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miniUI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miniUI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miniUI
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  miniUI || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/miniUI/DESCRIPTION
/usr/lib64/R/library/miniUI/INDEX
/usr/lib64/R/library/miniUI/Meta/Rd.rds
/usr/lib64/R/library/miniUI/Meta/features.rds
/usr/lib64/R/library/miniUI/Meta/hsearch.rds
/usr/lib64/R/library/miniUI/Meta/links.rds
/usr/lib64/R/library/miniUI/Meta/nsInfo.rds
/usr/lib64/R/library/miniUI/Meta/package.rds
/usr/lib64/R/library/miniUI/NAMESPACE
/usr/lib64/R/library/miniUI/R/miniUI
/usr/lib64/R/library/miniUI/R/miniUI.rdb
/usr/lib64/R/library/miniUI/R/miniUI.rdx
/usr/lib64/R/library/miniUI/help/AnIndex
/usr/lib64/R/library/miniUI/help/aliases.rds
/usr/lib64/R/library/miniUI/help/miniUI.rdb
/usr/lib64/R/library/miniUI/help/miniUI.rdx
/usr/lib64/R/library/miniUI/help/paths.rds
/usr/lib64/R/library/miniUI/html/00Index.html
/usr/lib64/R/library/miniUI/html/R.css
/usr/lib64/R/library/miniUI/www/miniUI.css
