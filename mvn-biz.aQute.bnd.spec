#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-biz.aQute.bnd
Version  : 1
Release  : 2
URL      : https://repo.maven.apache.org/maven2/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.jar
Source0  : https://repo.maven.apache.org/maven2/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.jar
Source1  : https://repo.maven.apache.org/maven2/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-biz.aQute.bnd-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-biz.aQute.bnd package.
Group: Data

%description data
data components for the mvn-biz.aQute.bnd package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.jar
/usr/share/java/.m2/repository/biz/aQute/bnd/biz.aQute.bnd/4.0.0/biz.aQute.bnd-4.0.0.pom
