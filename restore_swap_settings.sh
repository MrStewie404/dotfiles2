#!/bin/bash

# 1. Восстановление zswap
echo "options zswap enabled=1 max_pool_percent=60 compressor=zstd" | sudo tee /etc/modprobe.d/zswap.conf
sudo dracut -f

# 2. Создание swap-файла (23 ГБ)
sudo swapoff /var/swap/swapfile 2>/dev/null
sudo dd if=/dev/zero of=/var/swap/swapfile bs=1G count=23 status=progress
sudo chmod 600 /var/swap/swapfile
sudo mkswap /var/swap/swapfile
sudo swapon /var/swap/swapfile

# 3. Добавление swap в fstab
echo "/var/swap/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab

# 4. Настройка swappiness
echo "vm.swappiness=30" | sudo tee /etc/sysctl.d/99-swap.conf
sudo sysctl -p /etc/sysctl.d/99-swap.conf

# 5. Проверка
echo -e "\n\033[1;32mГотово! Проверьте настройки:\033[0m"
swapon --show
free -h
cat /sys/module/zswap/parameters/enabled
