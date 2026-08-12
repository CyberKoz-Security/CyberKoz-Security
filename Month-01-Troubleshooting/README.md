# ShieldX SOC Journey — Month 1 Troubleshooting Knowledge Base

This directory documents real troubleshooting incidents encountered during Month 1 of the ShieldX SOC lab journey. Each note records the symptom, investigation path, root cause, fix, verification, and lesson learned.

> Scope: authorized home lab only. Sensitive values, credentials, private keys, and unnecessary infrastructure identifiers are intentionally excluded.

## Incidents

1. [Wazuh clean reinstall and Filebeat leftovers](01-wazuh-clean-reinstall-filebeat-leftovers.md)
2. [SSH remote host identification changed](02-ssh-host-key-changed.md)
3. [Windows OpenSSH administrator public-key authentication](03-windows-openssh-admin-authorized-keys.md)
4. [Git initialized in the wrong directory](04-git-initialized-in-home-directory.md)
5. [VMware cannot open Windows VM on external SSD](05-vmware-external-ssd-not-mounted.md)
6. [NTFS dirty volume and MFT/MFTMirr mismatch](06-ntfs-dirty-volume-repair.md)
7. [External SSD device name changed between boots](07-linux-device-name-change.md)
8. [VMware default VM location vs actual VM path](08-vmware-default-location-vs-existing-vm.md)
9. [Month 1 lab health verification SOP](09-lab-health-verification-sop.md)

## Troubleshooting Method Used

The recurring workflow used throughout Month 1 was:

1. Observe the symptom.
2. Collect evidence.
3. Verify assumptions.
4. Isolate the failing layer.
5. Identify the root cause.
6. Apply the smallest safe fix.
7. Verify the fix.
8. Document the outcome.

This approach is intentionally tool-agnostic and is reusable for SOC triage, Linux administration, Windows troubleshooting, networking, and virtualization issues.
