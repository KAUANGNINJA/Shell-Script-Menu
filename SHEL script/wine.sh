sudo rm /var/lib/dpkg/lock-frontend ; 
sudo rm /var/cache/apt/archives/lock ;
sudo apt update ;
sudo apt upgrade -y ;

#Instalando o wine e utils
sudo dpkg --add-architecture i386 ;
sudo apt-get update -y ;
sudo apt install wine -y ;
sudo apt install wine64 -y ;
sudo apt install wine32 -y ;
sudo apt install winbind -y ;
sudo apt install winetricks -y ;