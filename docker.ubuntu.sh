set -x

apt-get -y remove docker docker-selinux
apt-get install -y --no-install-recommends apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://apt.dockerproject.org/gpg | apt-key add -
apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D
add-apt-repository "deb https://apt.dockerproject.org/repo/ ubuntu-$(lsb_release -cs) main"
apt-get -y update
apt-get -y install docker-engine
service start docker
docker run hello-world
docker stop $(docker ps -a -q) 2>/dev/null
docker rm $(docker ps -a -q)
docker rmi --force $(docker images -q)

# not necessary in ubuntu apparently
#apt-cache madison docker-engine
#VER=$(apt-cache madison docker-engine |sort -r|grep '^docker'|head -1|awk '{ print $3 }')
#echo "VER=($VER)"
#apt-get -y install docker-engine-$VER

