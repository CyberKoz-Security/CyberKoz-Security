# VMware Default VM Location vs Existing VM Location

## Symptom

VMware Preferences showed a default virtual-machine location such as:

```text
/mnt/kenzo/VMware
```

while an existing Ubuntu VM was stored at a different path such as:

```text
/home/shieldx/vmware/Ubuntu-Lab/Ubuntu-Lab.vmx
```

This raised concern that the Ubuntu VM might no longer boot.

## Root Cause

The VMware preference controls the default storage location for newly created virtual machines. It does not automatically move or rewrite the paths of existing VMs.

## Investigation

The actual VM path was verified from VMware and from the filesystem.

Useful checks:

```bash
find ~/vmware -name '*.vmx'
find /mnt/kenzo -name '*.vmx'
```

## Fix

No repair was necessary. The existing Ubuntu VM remained registered at its original internal-SSD location, while the Windows VM was intentionally stored on the external SSD.

## Verification

Both `.vmx` files could be located at their expected paths, and the corresponding VMs could be opened when their backing storage was available.

## Lesson Learned

A software 'default location' is a creation preference, not necessarily the current location of existing assets. Always verify the actual configuration-file path before moving or recreating a VM.
