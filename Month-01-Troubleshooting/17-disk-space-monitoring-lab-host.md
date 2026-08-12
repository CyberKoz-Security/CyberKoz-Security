# Host Disk Space Monitoring

## Scenario

The Kali host had limited remaining free space while also storing tools, captures, logs, and at least one virtual machine.

## Investigation

Check filesystem capacity:

```bash
df -h
```

Identify large top-level directories before deleting anything:

```bash
du -h --max-depth=1 ~ | sort -hr
```

## Risk

A nearly full host filesystem can cause:

- Package installation failures
- Log write failures
- VM snapshot failures
- Wazuh/indexing problems if relevant data is stored there
- Incomplete PCAP captures

## Safe Response

Do not delete files blindly. First identify large consumers such as old ISO images, package caches, unused downloads, stale snapshots, or duplicate VM data.

## Verification

Re-run:

```bash
df -h
```

and confirm that enough free space exists for the planned workload.

## Lesson Learned

Capacity is part of system health. Troubleshooting should distinguish between a storage problem and an application problem before changing application configuration.
