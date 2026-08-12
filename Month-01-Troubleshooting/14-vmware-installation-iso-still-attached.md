# VMware Installation ISO Still Attached

## Scenario

After Ubuntu or Windows installation, the virtual CD/DVD device may still point to the original installation ISO.

## Risk

This usually does not break an installed VM, but it can cause confusing boot behavior, unnecessary media prompts, or accidental booting into the installer if boot order changes.

## Safe Fix

1. Shut down the guest cleanly.
2. Open the VM settings.
3. Select the CD/DVD device.
4. Uncheck `Connected` and `Connect at power on`, or remove the ISO reference while keeping the virtual CD/DVD device.
5. Do not delete the VM disk.

## Verification

Power on the VM and confirm it boots from its virtual hard disk normally.

## Lesson Learned

Treat installation media like a physical installer DVD: it is useful during installation but should not remain logically inserted forever unless there is a reason.
