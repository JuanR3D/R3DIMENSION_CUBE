DISPLAY=:0 xrandr
sudo nano /usr/share/X11/xorg.conf.d/90-monitor.conf
sudo service KlipperScreen restart
DISPLAY=:0 xinput
DISPLAY=:0 xrandr
sudo nano /usr/share/X11/xorg.conf.d/90-monitor.conf
sudo service KlipperScreen restart
sudo nano /usr/share/X11/xorg.conf.d/90-monitor.conf
DISPLAY=:0 xinput
DISPLAY=:0 xinput set-prop "BIQU BTT-HDMI7" 'Coordinate Transformation Matrix' -1 0 1 0 -1 1 0 0 1
sudo service KlipperScreen Restart
sudo service KlipperScreen restart
DISPLAY=:0 xinput set-prop "BIQU BTT-HDMI7" 'Coordinate Transformation Matrix' 	1 0 0 0 1 0 0 0 1
DISPLAY=:0 xinput set-prop "BIQU BTT-HDMI7" 'Coordinate Transformation Matrix' 	-1 0 1 0 -1 1 0 0 1
sudo nano /etc/udev/rules.d/51-touchscreen.rules
sudo reboot
sudo nano /etc/udev/rules.d/51-touchscreen.rules
DISPLAY=:0 xinput set-prop "BIQU BTT-HDMI7" 'Coordinate Transformation Matrix' 	-1 0 1 0 -1 1 0 0 1
sudo nano /etc/udev/rules.d/51-touchscreen.rules
sudo reboot
sudo nano /etc/udev/rules.d/51-touchscreen.rules
cat /var/log/Xorg.0.log
sudo nano /usr/share/X11/xorg.conf.d/40-libinput.conf
sudo reboot
DISPLAY=:0 xinput
sudo nano /usr/share/X11/xorg.conf.d/40-libinput.conf
sudo dfu-util -d 0483:df11 -R -a 0 -s 0x8000000:leave -D ./M8P_V2_H723_bootloader.bin
lsusb
sudo dfu-util -d 0483:df11 -R -a 0 -s 0x8000000:leave -D ./M8P_V2_H723_bootloader.bin
sudo nmtui
sudo timedatectl 
sudo timedatectl set-timezone Europe/Madrid
sudo timedatectl 
cd klipper
make menuconfig
~/klippy-env/bin/python ~/klipper/scripts/canbus_query.py can0
sudo apt-get update && sudo apt-get install git -y
cd ~ && git clone https://github.com/dw-0/kiauh.git 
./kiauh/kiauh.sh
cd ~
git clone https://github.com/pedrolamas/klipper-virtual-pins.git
./klipper-virtual-pins/install.sh
cd ~
git clone https://github.com/shiftingtech/Moonraker-loader.git
sudo ln -sf ~/Moonraker-loader/assets/89-moonraker-loader.rules /etc/udev/rules.d 
sudo ln -sf ~/Moonraker-loader/assets/*.sh /usr/local/sbin 
sudo ln -sf ~/Moonraker-loader/assets/*.sh /usr/local/sbin
sudo reboot
./kiauh/kiauh.sh
sudo cp /home/biqu/bootsplash.armbian /usr/lib/firmware/
sudo service klipper restart
sudo reboot
cd ~
git clone https://github.com/pedrolamas/klipper-virtual-pins.git
./klipper-virtual-pins/install.sh
sudo service klipper restart
./kiauh/kiauh.sh
sudo rm -rf /home/biqu/klipper
./kiauh/kiauh.sh
sudo service klipper restasrt
sudo service klipper restart
./kiauh/kiauh.sh
sudo reboot
cd ~
git clone https://github.com/pedrolamas/klipper-virtual-pins.git
./klipper-virtual-pins/install.sh
rm -rf ~/klipper-virtual-pins
rm ~/klipper/klippy/extras/virtual_pins.py
sudo systemctl restart klipper
sudo service klipper restart
cd ~
git clone https://github.com/pedrolamas/klipper-virtual-pins.git
./klipper-virtual-pins/install.sh
sudo service klipper restart
