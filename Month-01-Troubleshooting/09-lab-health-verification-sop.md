# ShieldX Lab Health Verification SOP

## Purpose

Use this checklist before major labs or after a reboot to confirm that the SOC environment is healthy before troubleshooting application-level issues.

## 1. Kali Host Verification

```bash
hostnamectl
df -h
free -h
uptime
ip -br addr
```

Confirm the expected OS/hostname, sufficient disk space, healthy available RAM/swap, reasonable load, and expected interfaces.

## 2. Internet and DNS

Test raw IP reachability and DNS separately using known safe test destinations:

```bash
ping -c 4 <KNOWN_EXTERNAL_IP>
ping -c 4 <KNOWN_DOMAIN>
```

## 3. VMware Verification

```bash
vmware --version
lsmod | grep vm
```

Confirm VMware is installed and its required host modules are available.

## 4. External Windows VM Storage

Before starting a VM stored on removable media:

```bash
lsblk -f
mount | grep <MOUNT_POINT_NAME>
```

If detected but not mounted:

```bash
sudo mount <CURRENT_NTFS_PARTITION> <MOUNT_POINT>
```

Verify:

```bash
find <MOUNT_POINT> -name '*.vmx'
```

## 5. Ubuntu/Wazuh VM Verification

After booting the Wazuh server:

```bash
hostname -I
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status filebeat --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

## 6. Windows VM Verification

Confirm:

- Windows boots normally
- Network connectivity works
- OpenSSH is available when required
- Wazuh agent connectivity is healthy when required

## 7. Troubleshooting Order

1. Is the system powered on?
2. Is the expected network configuration present?
3. Is the host reachable?
4. Is the service running?
5. Is the port listening?
6. Is a firewall blocking traffic?
7. Are authentication settings correct?
8. What do the logs say?
9. Capture packets when lower-level checks do not explain the issue.

## Core Principle

Do not assume the cause. Establish a known-good baseline, collect evidence, isolate the failing layer, apply the smallest safe fix, and verify again.
