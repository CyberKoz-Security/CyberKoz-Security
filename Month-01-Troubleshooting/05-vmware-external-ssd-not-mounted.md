# VMware Cannot Open Windows VM on External SSD

## Symptom

VMware Workstation displayed a file-not-found error for a Windows VM stored on an external SSD.

## Investigation

Check whether the expected external-drive mount point is active:

```bash
mount | grep <MOUNT_POINT_NAME>
ls -lah <MOUNT_POINT>
find <MOUNT_POINT> -name '*.vmx'
```

Then verify the removable drive itself:

```bash
lsblk -f
```

## Root Cause

The external SSD was physically connected but not mounted at the path VMware expected. VMware remembered the VM path correctly, but the underlying filesystem was unavailable.

## Fix

Identify the correct current block device:

```bash
lsblk -f
```

Then mount the NTFS partition:

```bash
sudo mount <NTFS_PARTITION> <MOUNT_POINT>
```

## Verification

```bash
find <MOUNT_POINT> -name '*.vmx'
```

Once the expected `.vmx` file is visible, VMware can open the guest again.

## Lesson Learned

When a VM is stored on removable storage, a VMware `file not found` error may be a storage-availability problem rather than a corrupted VM. Verify the mount point before recreating or reinstalling anything.
