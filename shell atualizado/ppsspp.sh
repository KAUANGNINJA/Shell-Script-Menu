sudo rm /var/lib/dpkg/lock-frontend ; 
sudo rm /var/cache/apt/archives/lock ;
sudo apt update ;
sudo apt upgrade -y ;

sudo add-apt-repository ppa:ppsspp/stable ;
sudo apt-get update ;
sudo apt-get install ppsspp -y ;
sudo apt-get install ppsspp-sdl ;
