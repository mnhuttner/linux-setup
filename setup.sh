
yum -y install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
yum -y update

yum -y install https://sourceforge.net/projects/etherape/files/etherape/0.9.14/etherape-0.9.14-obs.centos700.26.1.x86_64.rpm

yum -y install https://kojipkgs.fedoraproject.org//packages/system-config-lvm/1.1.18/1.fc19/noarch/system-config-lvm-1.1.18-1.fc19.noarch.rpm

for i in $(cat packages.txt) ; do
  yum -y install $i
done

