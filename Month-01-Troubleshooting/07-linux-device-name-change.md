# External SSD Device Name Changed Between Connections

## Symptom

A mount command that previously worked with:

```bash
sudo mount /dev/sdb2 /mnt/kenzo
```

later failed with a block-device lookup error.

## Investigation

The current block-device layout was checked with:

```bash
lsblk -f
sudo fdisk -l
```

The external SSD, previously assigned `/dev/sdb2`, was now assigned `/dev/sdc2`.

## Root Cause

Linux `/dev/sdX` names are assigned dynamically based on device discovery order. Reconnecting removable storage can change a drive from `sdb` to `sdc`, `sdd`, and so on.

## Fix

The current device name was identified before mounting:

```bash
lsblk -f
```

Then the correct partition was mounted:

```bash
sudo mount /dev/sdc2 /mnt/kenzo
```

## Verification

```bash
mount | grep kenzo
find /mnt/kenzo -name '*.vmx'
```

The expected VM path was visible again.

## Better Long-Term Practice

Use a stable filesystem identifier such as UUID or LABEL for persistent mounts instead of relying on `/dev/sdX` names.

Example UUID observed in the lab:

```text
127258AC725895F7
```

A future `/etc/fstab` entry can mount the external SSD consistently at `/mnt/kenzo`, but persistent mount configuration should be tested carefully to avoid boot delays when the removable drive is absent.

## Lesson Learned

Device names describe the current discovery order, not permanent identity. Always verify removable storage with `lsblk -f` before acting on a remembered `/dev/sdX` path.
