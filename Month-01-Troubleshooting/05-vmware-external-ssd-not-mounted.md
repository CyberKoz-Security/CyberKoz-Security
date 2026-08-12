# VMware Cannot Open Windows VM on External SSD

## Symptom

VMware Workstation displayed an error similar to:

```text
Unable to open /mnt/kenzo/VMware/ShieldX-Win10/ShieldX-Win10.vmx
File not found
```

The Windows VM was stored on an external SSD rather than on the internal Kali disk.

## Investigation

The first check verified whether the external SSD mount point was active:

```bash
mount | grep kenzo
ls -lah /mnt/kenzo
find /mnt/kenzo -name '*.vmx'
```

The mount command returned no result, `/mnt/kenzo` was empty, and no `.vmx` file could be found.

`lsblk -f` confirmed that the external NTFS SSD was physically detected but had no mount point.

## Root Cause

The external SSD was connected but not mounted at `/mnt/kenzo`. VMware remembered the VM path correctly, but the underlying filesystem was unavailable.

## Fix

After identifying the correct block device with:

```bash
lsblk -f
```

the NTFS partition was mounted:

```bash
sudo mount /dev/sdX2 /mnt/kenzo
```

`/dev/sdX2` must be replaced with the current device name shown by `lsblk`.

## Verification

```bash
find /mnt/kenzo -name '*.vmx'
```

returned the expected Windows VM configuration file:

```text
/mnt/kenzo/VMware/ShieldX-Win10/ShieldX-Win10.vmx
```

VMware could then open and run the VM normally.

## Lesson Learned

When a VM is stored on removable storage, a VMware 'file not found' error may be a storage-availability problem rather than a corrupted VM. Verify the mount point before recreating or reinstalling anything.
