#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mnormt
Version  : 1.5.5
Release  : 19
URL      : https://cran.r-project.org/src/contrib/mnormt_1.5-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mnormt_1.5-5.tar.gz
Summary  : The multivariate Normal and T distributions.
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-mnormt-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
distribution function of multivariate normal and "t" random variables,
  and for generating random vectors sampled from these distributions.  
  Probabilities are computed via non-Monte Carlo methods; different routines 
  are used in the case d=1, d=2, d>2, if d denotes the number of dimensions.

%package lib
Summary: lib components for the R-mnormt package.
Group: Libraries

%description lib
lib components for the R-mnormt package.


%prep
%setup -q -c -n mnormt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552930075

%install
export SOURCE_DATE_EPOCH=1552930075
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mnormt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mnormt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mnormt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  mnormt || :


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
/usr/lib64/R/library/mnormt/NEWS
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mnormt/libs/mnormt.so
/usr/lib64/R/library/mnormt/libs/mnormt.so.avx2
/usr/lib64/R/library/mnormt/libs/mnormt.so.avx512
