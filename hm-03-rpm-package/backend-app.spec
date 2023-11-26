Name:           backend-app
Version:        1.1
Release:        1%{?dist}
Summary:        backend-app

License:        MIT
URL:            google.com

Requires:       java

%define missing_doc_files_terminate_build 0

%description
Devops Lineate course

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/app/
cp -r ~/rpmbuild/SOURCES/dist/ops_school-0.0.1-SNAPSHOT-jar-with-dependencies.jar $RPM_BUILD_ROOT/app/
cp -r ~/rpmbuild/SOURCES/backend-app.service $RPM_BUILD_ROOT/app/backend-app.service

%files
%defattr(0644, root, root)
/app/ops_school-0.0.1-SNAPSHOT-jar-with-dependencies.jar
/app/backend-app.service

%post
sed "s/JAVA_HOME/$(echo $(which java | sed 's_/_\\/_g'))/g" $RPM_BUILD_ROOT/app/backend-app.service | sed "s/WORKING_DIRECTORY/$(echo $(echo $RPM_BUILD_ROOT/app/ | sed 's_/_\\/_g'))/g" | sudo tee /etc/systemd/system/backend-app.service
sudo systemctl start backend-app

%preun
sudo systemctl stop backend-app
sudo rm /etc/systemd/system/backend-app.service


%changelog
* Sat Nov 11 2023 osboxes.org
- 
