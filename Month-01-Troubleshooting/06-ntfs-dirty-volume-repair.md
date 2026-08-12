# NTFS Dirty Volume and MFT/MFTMirr Mismatch

## Symptom

Mounting an external NTFS SSD on Kali failed with errors such as:

```text
wrong fs type, bad option, bad superblock...
```

Kernel logs reported that the volume was dirty, and an `ntfs-3g` attempt reported an `$MFTMirr` / `$MFT` mismatch.

## Investigation

```bash
lsblk -f
which ntfs-3g
sudo dmesg | tail -20
```

The drive was correctly identified as NTFS and the helper was installed, so the problem was filesystem consistency rather than a missing driver.

## Root Cause

The NTFS volume was left in an inconsistent state. Linux refused to mount it normally to reduce the risk of further filesystem damage.

## Fix

Connect the SSD to a Windows system and run an elevated filesystem repair against the correct drive letter:

```cmd
chkdsk <DRIVE_LETTER>: /f
```

Confirm the drive letter carefully before running the command. After CHKDSK completes, safely eject the disk and reconnect it to Kali.

## Verification

```bash
lsblk -f
sudo mount <NTFS_PARTITION> <MOUNT_POINT>
find <MOUNT_POINT> -name '*.vmx'
```

The volume should mount without filesystem errors and the VM configuration file should be visible again.

## Lesson Learned

Do not force-mount an NTFS filesystem that reports metadata inconsistency. Read the kernel error first and repair the filesystem with the native Windows tool when appropriate.
