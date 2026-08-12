# NTFS Dirty Volume and MFT/MFTMirr Mismatch

## Symptom

Mounting the external SSD on Kali failed with errors including:

```text
wrong fs type, bad option, bad superblock...
```

Kernel logs showed:

```text
ntfs3(...): volume is dirty and "force" flag is not set!
```

An `ntfs-3g` mount attempt also reported:

```text
$MFTMirr does not match $MFT
Failed to mount: Input/output error
```

## Investigation

The filesystem type and helper availability were checked:

```bash
lsblk -f
which ntfs-3g
sudo dmesg | tail -20
```

The device was correctly identified as NTFS, and `ntfs-3g` was installed. The kernel logs pointed to NTFS metadata inconsistency rather than a missing driver.

## Root Cause

The NTFS volume had been left in an inconsistent/dirty state. The NTFS Master File Table metadata and its mirror did not match, so Linux refused to mount the filesystem normally to avoid further damage.

## Fix

The external SSD was connected to a Windows system and repaired with an elevated Command Prompt:

```cmd
chkdsk D: /f
```

The actual drive letter must be confirmed before running the command.

After CHKDSK completed successfully, the drive was safely disconnected from Windows and reconnected to Kali.

## Verification

Back on Kali:

```bash
lsblk -f
sudo mount /dev/sdX2 /mnt/kenzo
find /mnt/kenzo -name '*.vmx'
```

The NTFS volume mounted without error and the Windows VM configuration file became accessible again.

## Lesson Learned

Do not force-mount an NTFS filesystem that reports metadata inconsistency. Read the kernel error first, repair the filesystem with the native Windows `chkdsk /f` tool when appropriate, and verify clean mounting afterward.
