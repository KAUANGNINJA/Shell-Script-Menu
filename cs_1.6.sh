sudo rm /var/lib/dpkg/lock-frontend ; 
sudo rm /var/cache/apt/archives/lock ;
sudo apt update ;
sudo apt upgrade -y ;

sudo wget http://files.gs2us.com/cs_16.exe ;
sudo chmod 777 cs_16.exe ;
