Name:           front-app
Version:        1.1
Release:        1%{?dist}
Summary:        UI app

License:        MIT
URL:            google.com
 
Requires:       nginx

%define missing_doc_files_terminate_build 0

%description
Devops Lineate course

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/www/app/
cp -r ~/rpmbuild/SOURCES/dist/ui/* $RPM_BUILD_ROOT/var/www/app/
mkdir -p $RPM_BUILD_ROOT/etc/nginx/sites-available/
cp -r ~/rpmbuild/SOURCES/app.com.conf $RPM_BUILD_ROOT/etc/nginx/sites-available/


%files
%defattr(0644, root, root)
/etc/nginx/sites-available/app.com.conf
/var/www/app/

%post
mkdir -p $RPM_BUILD_ROOT/etc/nginx/sites-available/
if [ ! -L /etc/nginx/sites-enabled/app.com.conf ];
then
 ln -s /etc/nginx/sites-available/app.com.conf etc/nginx/sites-enabled/app.com.conf
fi
systemctl restart nginx



%changelog
* Sat Nov 11 2023 osboxes.org
- 
