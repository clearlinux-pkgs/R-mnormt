#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mnormt
Version  : 2.1.1
Release  : 56
URL      : https://cran.r-project.org/src/contrib/mnormt_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mnormt_2.1.1.tar.gz
Summary  : The Multivariate Normal and t Distributions, and Their Truncated
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-mnormt-lib = %{version}-%{release}
Requires: R-mnormt-license = %{version}-%{release}
BuildRequires : buildreq-R

%description
distribution function of d-dimensional normal and "t" random variables,
  possibly truncated (on one side or two sides),  and for generating random 
  vectors sampled from these distributions, except sampling from the truncated
  "t". Moments of arbitrary order of a multivariate truncated normal are
  computed, and converted to cumulants up to order 4. 
  Probabilities are computed via non-Monte Carlo methods; different routines 
  are used in the case d=1, d=2, d=3, d>3, if d denotes the dimensionality.

%package lib
Summary: lib components for the R-mnormt package.
Group: Libraries
Requires: R-mnormt-license = %{version}-%{release}

%description lib
lib components for the R-mnormt package.


%package license
Summary: license components for the R-mnormt package.
Group: Default

%description license
license components for the R-mnormt package.


%prep
%setup -q -n mnormt
cd %{_builddir}/mnormt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664208453

%install
export SOURCE_DATE_EPOCH=1664208453
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-mnormt
cp %{_builddir}/mnormt/COPYING %{buildroot}/usr/share/package-licenses/R-mnormt/17e3b0eea99abffe6ac71e65627413236e0b117a || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mnormt/CITATION
/usr/lib64/R/library/mnormt/DESCRIPTION
/usr/lib64/R/library/mnormt/INDEX
/usr/lib64/R/library/mnormt/Meta/Rd.rds
/usr/lib64/R/library/mnormt/Meta/features.rds
/usr/lib64/R/library/mnormt/Meta/hsearch.rds
/usr/lib64/R/library/mnormt/Meta/links.rds
/usr/lib64/R/library/mnormt/Meta/nsInfo.rds
/usr/lib64/R/library/mnormt/Meta/package.rds
/usr/lib64/R/library/mnormt/NAMESPACE
/usr/lib64/R/library/mnormt/NEWS.Rd
/usr/lib64/R/library/mnormt/R/mnormt
/usr/lib64/R/library/mnormt/R/mnormt.rdb
/usr/lib64/R/library/mnormt/R/mnormt.rdx
/usr/lib64/R/library/mnormt/help/AnIndex
/usr/lib64/R/library/mnormt/help/aliases.rds
/usr/lib64/R/library/mnormt/help/mnormt.rdb
/usr/lib64/R/library/mnormt/help/mnormt.rdx
/usr/lib64/R/library/mnormt/help/paths.rds
/usr/lib64/R/library/mnormt/html/00Index.html
/usr/lib64/R/library/mnormt/html/R.css
/usr/lib64/R/library/mnormt/notice-Genz

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mnormt/libs/mnormt.so
/usr/lib64/R/library/mnormt/libs/mnormt.so.avx2
/usr/lib64/R/library/mnormt/libs/mnormt.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-mnormt/17e3b0eea99abffe6ac71e65627413236e0b117a
