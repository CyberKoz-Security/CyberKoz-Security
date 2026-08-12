# Persistent External SSD Mount by UUID

## Goal

Avoid relying on changing device names such as `/dev/sdb2` or `/dev/sdc2` when a removable SSD stores a VMware virtual machine.

## Why UUID Is Better

Linux `/dev/sdX` names can change when devices are reconnected. A filesystem UUID is designed to identify the filesystem consistently.

## Safe Preparation

First identify the external SSD and its UUID:

```bash
lsblk -f
```

Use placeholders in public documentation:

```text
UUID=<EXTERNAL_SSD_UUID>
Mount point=<MOUNT_POINT>
Filesystem=ntfs
```

Create the mount point if needed:

```bash
sudo mkdir -p <MOUNT_POINT>
```

## Example `/etc/fstab` Pattern

For a removable NTFS SSD, a cautious entry can use `nofail` so the host can still boot when the SSD is disconnected:

```text
UUID=<EXTERNAL_SSD_UUID> <MOUNT_POINT> ntfs3 defaults,nofail,x-systemd.device-timeout=5 0 0
```

Before editing `/etc/fstab`, make a backup:

```bash
sudo cp /etc/fstab /etc/fstab.backup
```

After editing, test the configuration without rebooting:

```bash
sudo mount -a
```

Then verify:

```bash
findmnt <MOUNT_POINT>
```

## Recovery

If `mount -a` reports an error, restore the backup or correct the entry before rebooting:

```bash
sudo cp /etc/fstab.backup /etc/fstab
```

## VMware Verification

After the SSD is mounted, confirm the VM configuration is reachable:

```bash
find <MOUNT_POINT> -name '*.vmx'
```

## Safety Notes

- Never edit `/etc/fstab` blindly.
- Confirm the UUID and filesystem type with `lsblk -f` first.
- Use `nofail` for removable storage so an absent SSD does not block normal boot.
- Shut down the VM and unmount the SSD before physically disconnecting it.
- Do not publish the real UUID if it is unnecessary for the learning objective.
