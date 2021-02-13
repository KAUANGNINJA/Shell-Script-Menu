sudo rm /var/lib/dpkg/lock-frontend ; 
sudo rm /var/cache/apt/archives/lock ;
sudo apt update ;
sudo apt upgrade -y ;

sudo add-apt-repository ppa: lutris-team / lutris ;
sudo apt update ;
sudo apt install lutris -y ;
