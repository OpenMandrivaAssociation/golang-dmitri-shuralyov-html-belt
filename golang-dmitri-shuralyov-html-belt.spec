 # Run tests in check section
%bcond_without check

%global goipath         dmitri.shuralyov.com/html/belt
%global commit          f7d459c86be0d89cab0b8a0694d6f9a5586cd184
%global scm             git

%global common_description %{expand:
Collection of HTML components for shared use by multiple web apps.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Collection of HTML components for shared use by multiple web apps
License:        BSD
URL:            %{gourl}
# git clone dmitri.shuralyov.com/html/belt
# cd belt
# git archive --format tar.gz --prefix belt-%%{commit}/ %%{commit} > belt-%%{commit}.tar.gz
Source0:        belt-%{commit}.tar.gz
Source1:        https://dmitri.shuralyov.com/LICENSE

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n belt-%{commit}
cp %{S:1} .


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026gitf7d459c
- Bump to commit f7d459c86be0d89cab0b8a0694d6f9a5586cd184

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf6fb90f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitf6fb90f
- First package for Fedora

