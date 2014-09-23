#! /bin/bash
export http_proxy="http://proxy.iiit.ac.in
echo $http_proxy
export https_proxy="http://proxy.iiit.ac.in
echo $https_proxy
apt-get install apache2
apt-get install php5
apt-get purge nodejs npm
apt-get install -y python-software-properties python g++ make software-properties-common
add-apt-repository ppa:chris-lea/node.js
apt-get update
apt-get install nodejs
npm config set https-proxy http://proxy.iiit.ac.in:8080
npm config set proxy http://proxy.iiit.ac.in:8080
npm install phantomjs
cp /node_modules/phantomjs/lib/phantom/bin/phantomjs /usr/bin
cd /var/www/
git clone https://github.com/jayanthsagar/performace_testing.git
chmod -R 775 performace_testing/





