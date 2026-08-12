# VMware Default VM Location vs Existing VM Location

## Symptom

VMware Preferences showed one default location for new virtual machines while an existing VM was stored at a different path, raising concern that the existing VM might no longer boot.

## Root Cause

The VMware preference controls the default storage location for newly created virtual machines. It does not automatically move or rewrite the paths of existing VMs.

## Investigation

Verify the real configuration-file locations instead of assuming the default path represents every VM:

```bash
find <INTERNAL_VM_DIRECTORY> -name '*.vmx'
find <EXTERNAL_VM_MOUNT> -name '*.vmx'
```

## Fix

No repair is required if the existing `.vmx` files are present and VMware can access the backing storage. Keep each VM registered at its real location.

## Verification

Locate each `.vmx` file and confirm the corresponding VM opens when its storage is available.

## Lesson Learned

A software `default location` is a creation preference, not necessarily the current location of existing assets. Verify the actual configuration-file path before moving or recreating a VM.
