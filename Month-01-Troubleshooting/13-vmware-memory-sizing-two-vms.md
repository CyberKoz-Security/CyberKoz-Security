# VMware Memory Sizing for a Small SOC Lab

## Scenario

A Kali Linux host runs an Ubuntu Wazuh VM and a Windows endpoint VM at the same time.

## Problem

Allocating too much memory to each guest can leave the host without enough RAM, causing swapping, freezes, or poor SIEM performance.

## Investigation

Check host memory before starting VMs:

```bash
free -h
```

Check load:

```bash
uptime
```

Review each VM's configured RAM in VMware before powering on both guests.

## Safe Approach

Use balanced allocations that leave enough memory for the host and VMware overhead. Exact values depend on the machine, workload, and Wazuh index size.

Avoid treating configured guest RAM as free capacity: the host OS, browser, Wireshark, and other tools also need memory.

## Verification

After both VMs start:

```bash
free -h
```

Confirm the host still has usable available memory and is not heavily swapping.

## Lesson Learned

Capacity planning is part of lab reliability. A technically valid VM configuration can still be operationally poor if the host is starved of resources.
