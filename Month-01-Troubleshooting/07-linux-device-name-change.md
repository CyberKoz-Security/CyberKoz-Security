# External SSD Device Name Changed Between Connections

## Symptom

A mount command that previously worked with one `/dev/sdX` name later failed because the removable SSD had been assigned a different device name.

## Investigation

```bash
lsblk -f
sudo fdisk -l
```

The same external SSD appeared under a different `/dev/sdX` path after reconnecting it.

## Root Cause

Linux `/dev/sdX` names are assigned dynamically based on device discovery order. Reconnecting removable storage can change a drive from one letter to another.

## Fix

Always identify the current device first:

```bash
lsblk -f
```

Then mount the correct partition:

```bash
sudo mount <CURRENT_NTFS_PARTITION> <MOUNT_POINT>
```

## Verification

```bash
mount | grep <MOUNT_POINT_NAME>
find <MOUNT_POINT> -name '*.vmx'
```

## Better Long-Term Practice

Use a stable filesystem identifier such as UUID or LABEL for persistent mounts instead of relying on `/dev/sdX` names.

Example placeholder:

```text
UUID=<EXTERNAL_SSD_UUID>
```

Persistent mount configuration should be tested carefully so an absent removable drive does not create unnecessary boot problems.

## Lesson Learned

Device names describe current discovery order, not permanent identity. Verify removable storage before acting on a remembered `/dev/sdX` path.
