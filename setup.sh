
yum -y install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
yum -y update

yum -y install https://sourceforge.net/projects/etherape/files/etherape/0.9.14/etherape-0.9.14-obs.centos700.26.1.x86_64.rpm

for i in $(cat packages.txt) ; do
  yum -y install $i
done

