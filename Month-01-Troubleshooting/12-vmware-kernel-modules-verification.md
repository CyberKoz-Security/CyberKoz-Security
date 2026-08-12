# VMware Kernel Module Verification

## Symptom

VMware may fail to start virtual machines or networking after a host kernel update or reboot if required kernel modules are not loaded.

## Investigation

Check the VMware version:

```bash
vmware --version
```

Check loaded VMware-related modules:

```bash
lsmod | grep vm
```

Typical modules include `vmmon`, `vmnet`, and VMware communication modules.

## Root Cause Pattern

A VMware installation can be present while its kernel modules are missing, incompatible with the current kernel, or not loaded.

## Fix Approach

Do not reinstall virtual machines. Repair or rebuild the VMware host modules for the running kernel, then verify they load successfully.

## Verification

- VMware opens without a module error.
- The expected modules appear in `lsmod`.
- Virtual machines start.
- VMware virtual networking interfaces are present.

## Lesson Learned

Separate the virtualization application from its host kernel integration. A working GUI does not prove the hypervisor modules are healthy.
