#set -x

yum -y remove docker docker-selinux
yum -y install yum-utils
yum-config-manager --add-repo https://docs.docker.com/engine/installation/linux/repo_files/centos/docker.repo
yum makecache fast
yum -y install docker-engine
yum list docker-engine.x86_64  --showduplicates |sort -r|grep '^docker'|head -1
VER=$(yum list docker-engine.x86_64  --showduplicates |sort -r|grep '^docker'|head -1|awk '{ print $2 }')
yum -y install docker-engine-$VER
systemctl start docker
docker run hello-world
# clean
docker stop $(docker ps -a -q) 2>/dev/null
docker rm $(docker ps -a -q)
docker rmi --force $(docker images -q)
