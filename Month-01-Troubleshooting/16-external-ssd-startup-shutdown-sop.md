# External SSD VM Startup and Shutdown SOP

## Scenario

A VMware guest is stored on an external NTFS SSD. VMware cannot access the guest if the drive is disconnected or not mounted.

## Startup Procedure

1. Connect the external SSD before starting the VM.
2. Verify detection:

```bash
lsblk -f
```

3. Identify the NTFS partition by label or UUID rather than assuming a device name such as `/dev/sdb2`.
4. Mount the partition to the expected mount point:

```bash
sudo mount <NTFS_PARTITION> <MOUNT_POINT>
```

5. Verify the VMware configuration file is visible:

```bash
find <MOUNT_POINT> -name "*.vmx"
```

6. Start VMware and power on the guest.

## Shutdown Procedure

1. Shut down the Windows guest cleanly.
2. Close VMware.
3. Ensure no process is using the external filesystem.
4. Unmount it:

```bash
sudo umount <MOUNT_POINT>
```

5. Physically disconnect the SSD only after a successful unmount.

## Important

Never unplug the external SSD while the VM is running or suspended. VMware may still be writing to the virtual disk.

## Lesson Learned

External VM storage behaves like removable infrastructure. Correct mounting and clean unmounting are part of VM lifecycle management.
