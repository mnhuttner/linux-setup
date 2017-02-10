set -x

pkill ssh-agent
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
ssh -vT git@github.com
for i in ansible-test docker-whale github.sh git-scripts jenkins-setup linux-setup ansible-tower-setup ; do
  git clone git@github.com:/mnhuttner/$i $I
done

