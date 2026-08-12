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

Confirm:

- Expected hostname and OS
- Sufficient disk space
- Healthy available RAM and swap
- Reasonable system load
- Expected network interfaces and IP addresses

## 2. Internet and DNS

```bash
ping -c 4 8.8.8.8
ping -c 4 google.com
```

The first tests raw IP reachability; the second also validates DNS resolution.

## 3. VMware Verification

```bash
vmware --version
lsmod | grep vm
```

Confirm VMware is installed and required VMware kernel modules are available.

## 4. External Windows VM Storage

Before starting the Windows VM stored on the external SSD:

```bash
lsblk -f
mount | grep kenzo
```

If the SSD is detected but not mounted, identify its current partition name and mount it:

```bash
sudo mount /dev/sdX2 /mnt/kenzo
```

Verify:

```bash
find /mnt/kenzo -name '*.vmx'
```

## 5. Ubuntu/Wazuh VM Verification

After booting Ubuntu, verify its IP and core Wazuh services:

```bash
hostname -I
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status filebeat --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

## 6. Windows VM Verification

Confirm the external SSD is mounted first, then start the VM and verify:

- Windows boots normally
- Network connectivity works
- OpenSSH service is available when required
- Wazuh agent is connected when required

## 7. Troubleshooting Order

When something fails, work from the lowest/simple layer upward:

1. Is the system powered on?
2. Is the correct IP configured?
3. Is the host reachable?
4. Is the service running?
5. Is the port listening?
6. Is a firewall blocking traffic?
7. Are credentials/keys correct?
8. What do the logs say?
9. Capture packets only when lower-level checks do not explain the issue.

## Core Principle

Do not assume the cause. Establish a known-good baseline, collect evidence, isolate the failing layer, apply the smallest safe fix, and verify again.
