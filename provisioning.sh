apt-get update
apt-get install python-pip git-core curl -y
apt-get install build-essential libevent-dev libpq-dev zlib1g-dev libssl-dev python-dev libxml2-dev libxslt1-dev -y
apt-get install firefox xvfb -y
# apt-get install postgresql-client -y
apt-get -y install libmemcached-dev
# apt-get -y install ruby-full rubygems ruby-sass ruby-compass
# wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
cd /vagrant
pip install -r reqs/dev.txt