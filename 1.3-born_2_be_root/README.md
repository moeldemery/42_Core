*This project has been created as part of the 42 curriculum by meldemir.*

# Born2beRoot

## Project Description
Born2beRoot is a System Administration project centered on the deployment of a hardened Debian 12 server. The project demonstrates proficiency in virtualization, LUKS-encrypted LVM partitioning, and the enforcement of rigorous security protocols. The server operates without a Graphical User Interface (GUI), requiring all configurations—including network security, complex user permissions, and automated monitoring services—to be managed via the command line.

## OS Choice: Debian 12.5 (Stable)
Based on the subject's recommendation, Debian was chosen over Rocky Linux.
- Pros: Extremely stable, lightweight, and uses the efficient apt package manager. It is the community standard for stability and ease of learning.
- Cons: Features more conservative (older) software versions compared to RHEL-based systems like Rocky.

## Main Design Choices

### 1. Partitioning (LVM & Encryption)
- LVM (Logical Volume Manager): Used to allow dynamic resizing of partitions.
- LUKS Encryption: Encrypts the physical volume to protect data at rest.
- Structure: Separate volumes were created for root, home, var, tmp, etc., to isolate system data and prevent a single log or user from crashing the system.

### 2. Security Policies
- Hostname: meldemir42.
- Password Policy: Enforced Passwords expire in "/etc/login.defs"
    PASS_MAX_DAYS (30): The maximum number of days a password can be used. After this, the user is forced to change it.
    PASS_MIN_DAYS (2): The minimum number of days that must pass before a user is allowed to change their password again.
    PASS_WARN_AGE (7): The number of days before expiration that the user begins receiving warning messages. 
- Password require a minimum length of 10 characters with mandatory complexity (Upper, Lower, Numbers).
- Sudo: Configured in /etc/sudoers.d/ to require TTY mode, limit attempts to 3, and log all I/O to /var/log/sudo/.
- Firewall (UFW): Strictly limited to ports 4242 (SSH) and 80 (HTTP/WordPress).

### 3. Services
- SSH: Hardened by disabling root login and changing the default port to 4242.
- Monitoring Script: A bash script (monitoring.sh) reporting system health every 10 minutes via cron.

## Mandatory Comparisons

- Debian vs Rocky Linux: Debian is community-driven and uses .deb/apt. Rocky Linux is an enterprise-grade RHEL clone using .rpm/dnf. Debian is generally more user-friendly for beginners.
- AppArmor vs SELinux: AppArmor (Debian) is path-based and easier to configure. SELinux (Rocky) is label-based, offering more granular but complex security controls.
- UFW vs firewalld: UFW is a simplified frontend for iptables on Debian. firewalld is more complex, using zones and services, and is the default for Rocky.
- VirtualBox vs UTM: VirtualBox is a cross-platform Type-2 hypervisor. UTM is a QEMU-based alternative optimized for Apple Silicon (M-series) Macs.

## Instructions

### Installation
1. Initialize a VM in VirtualBox with 1024MB RAM.
2. Follow the manual partitioning steps (Encrypted LVM).
3. Install GRUB on the primary drive (/dev/sda).

### SSH Connectivity
- Connect from the host: ssh meldemir@localhost -p 4242.
- Port forwarding: Host 4242 -> Guest 4242.

## Bonus Part
- WordPress: Fully functional on Port 80 using Lighttpd, MariaDB, and PHP.
- Docker: Running Odoo 18.0 linked to a PostgreSQL 15 container.

## Monitoring Script Logic
The monitoring.sh script utilizes the following logic:
- Architecture: uname -a.
- CPU: Gathers physical/virtual cores from /proc/cpuinfo.
- Memory/Disk: Calculates usage percentages using free --mega and df -m with awk.
- Sudo: Counts executed commands using journalctl -q _COMM=sudo | grep COMMAND | wc -l.

## Resources
- Debian Documentation: www.debian.org
- Sudoers Manual: man7.org
- Docker & Odoo Link Guide: docs.docker.com

## CheatSheet
#### partitions
- see all           => lsblk
#### users/Groups
- Add User          => sudo adduser "username" "groupname"
                       sudo useradd -m -s /bin/bash -G sudo -c "Full Name" username + sudo passwd username
- Add Group         => sudo addgroup "groupname"
                       sudo groupadd "groupname"
- View User List    => cat /etc/passwd
- View All Groups   => cat /etc/group
- View Group List   => getent group "groupname"
- Mod user/Group 	=> sudo usermod "name" -aG "groupname" (add group)
- Delete user/Group => sudo groupdel/userdel "name"
#### ssh
- Check ssh            => sudo service ssh status
- Edit default config  => sudo nano etc/ssh/sshd_config 
    (root+port) 
- Edit config (port)   => sudo nano /etc/ssh/ssh_config
- restart ssh          => sudo service ssh restart
#### UFW
- enable => sudo ufw enable
- status => sudo ufw status
#### SUDO
-  /etc/sudoers.d/sudo_config 
        Defaults passwd_tries=3
        Defaults badpass_message="Bad Password"
        Defaults logfile="/var/log/sudo/sudo_config"
        Defaults log_input, log_output
        Defaults iolog_dir="/var/log/sudo"
        Defaults requiretty
        Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/bin:/sbin:/bin:/snap/bin"
- /etc/login.defs
        PASS_MAX_DAYS   30
        PASS_MIN_DAYS   2
        PASS_WARN_AGE   7
- /etc/pam.d/common-password
        minlen=10:          Sets the minimum number of characters required for a password.
        ucredit=-1:         Specifies that the password must include at least one uppercase letter.
        dcredit=-1:         Requires the presence of at least one digit in the password.
        lcredit=-1:         Ensures the password contains at least one lowercase letter.
        maxrepeat=3:        Limits the repetition of the same character to a maximum of 3 times consecutively.
        reject_username:    Prohibits the password from containing the username.
        difok=7:            Specifies that at least 7 characters in the new password must differ from the old password.
        enforce_for_root:   Enforces these password policies for the root user, enhancing security even for privileged accounts.

#### Script
        #!/bin/bash

        #1-architecture
        arch=$(uname -a)

        #2-CPU Physical
        cpuf=$(grep "physical id" /proc/cpuinfo | wc -l)

        #3-CPU Virtual
        cpuv=$(grep "processor" /proc/cpuinfo | wc -l)

        #4-RAM
        ram_total=$(free --mega | awk '$1 == "Mem:"{print $2}')
        ram_used=$(free --mega | awk '$1 == "Mem:"{print $3}')
        ram_perc=$(free --mega | awk '$1 == "Mem:"{printf("%.2f"), $3/$2*100}')

        #5-Disk
        disk_total=$(df -m | grep  "/dev/"|grep -v "/boot" | awk '{disk_t += $2} END {printf("%.1f"), disk_t/1024 }')
        disk_used=$(df -m |  grep  "/dev/"|grep -v "/boot" | awk '{disk_u += $3} END {print disk_u }')
        disk_perc=$(df -m |  grep  "/dev/"|grep -v "/boot" | awk '{disk_u += $3}{disk_t += $2} END {printf("%d"), disk_u/disk_t*100}')

        #6-CPU Load
        cpu_l=$(vmstat 1 2 | tail -1 | awk '{printf $15}')
        cpu_op=$(( 100 - $cpu_l ))
        cpu_fin=$(printf "%.1f" $cpu_op)

        #7-Last Booot
        lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')

        #8-LVM Use
        lvm_use=$(if [ $(lsblk | grep "lvm" | wc -l) -gt 0 ]; then echo yes; else echo no; fi)

        #9-TCP Connection
        tcpc=$(ss -ta | grep ESTAB | wc -l)

        #10-User log
        ulog=$(users | wc -w)

        #11-Network
        ip=$(ip a | grep enp | grep inet | awk '{print $2}' | cut -d\/ -f1)
        mac=$(ip a | grep -A1 enp | grep ether | awk '{print $2}')

        #12-SUDO
        cmdd=$(journalctl -q _COMM=sudo |  grep COMMAND | wc -l )

        echo " Architecture:    $arch
                CPU Physical:   $cpuf
                vCPU:           $cpuv
                Memory Usage:   $ram_used/$ram_total MB ($ram_perc%)
                Disk Usage:     $disk_used/$disk_total GB ($disk_perc%)
                CPU Load:       $cpu_fin%
                Last Boot:      $lb
                LVM Use:        $lvm_use
                Connection TCP: $tcpc
                User Log:       $ulog
                Network:        IP $ip ($mac)
                Sudo:           $cmdd cmd"

#### Cronjob
- sudo crontab -u root -e
- */10 * * * * sh /home/meldemir/monitoring.sh | wall 2> /dev/null
    - Frequency: Every 10 minutes.
    - Output: Sent to all active terminal sessions via wall.
    - Errors: Silently discarded to prevent cron-mail spam.

#### BONUS
- Docker

        sudo apt update
        sudo apt install docker-ce docker-ce-cli containerd.io
        sudo systemctl start docker
        sudo systemctl enable docker
- postgres Container

        sudo docker run -d \
          -e POSTGRES_USER=odoo \
          -e POSTGRES_PASSWORD=odoo_password \
          -e POSTGRES_DB=postgres \
          --name db \
          postgres:15

- Odoo Container

        sudo docker run -d \
          -p 8069:8069 \
          --name odoo \
          --link db:db \
          -e HOST=db \
          -e USER=odoo \
          -e PASSWORD=odoo_password \
          -t odoo:18.0

## AI Usage
AI was utilized for the following tasks:
- Bash Logic: Refining the awk and printf commands in monitoring.sh for accurate disk/RAM percentage formatting.
- Troubleshooting: Guided the implementation of libpam-pwquality flags to meet the 42 password policy requirements.
- Containerization: Assisted with the --link flag syntax for Docker container communication.

