echo "Actualizando sistema"
apt-get update -y
apt-get upgrade -y
echo "Actualizacion terminada"
echo "Instalando requerimientos"
apt-get install python
apt-get install python3-pip
apt-get install bash
apt-get install git
apt-get install python-pip
pip install colorama
echo "Requerimientos instalados"
cd /home
cd Hack-Tools
python3 Hack-Tools.py

