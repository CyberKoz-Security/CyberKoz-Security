# ShieldX SOC Journey - Month 1 Troubleshooting Knowledge Base

This directory documents real troubleshooting incidents encountered during Month 1 of the ShieldX SOC lab journey. Each note records the symptom, investigation path, root cause, fix, verification, and lesson learned.

> Scope: authorized home lab only. Sensitive values, credentials, private keys, tokens, personal account details, exact lab addresses, device UUIDs, and unnecessary infrastructure identifiers are intentionally excluded or replaced with placeholders.

## Start Here

- [Category navigation](CATEGORIES.md) - find a guide by technology or problem type.
- [Security and sanitization rules](SECURITY-SANITIZATION.md) - what must never be published.
- [Privacy-safe evidence guide](EVIDENCE-GUIDE.md) - how to prepare screenshots and logs safely.

## Troubleshooting Guides

1. [Wazuh clean reinstall and Filebeat leftovers](01-wazuh-clean-reinstall-filebeat-leftovers.md)
2. [SSH remote host identification changed](02-ssh-host-key-changed.md)
3. [Windows OpenSSH administrator public-key authentication](03-windows-openssh-admin-authorized-keys.md)
4. [Git initialized in the wrong directory](04-git-initialized-in-home-directory.md)
5. [VMware cannot open Windows VM on external SSD](05-vmware-external-ssd-not-mounted.md)
6. [NTFS dirty volume and MFT/MFTMirr mismatch](06-ntfs-dirty-volume-repair.md)
7. [External SSD device name changed between connections](07-linux-device-name-change.md)
8. [VMware default location vs actual existing VM path](08-vmware-default-location-vs-existing-vm.md)
9. [Month 1 lab health verification SOP](09-lab-health-verification-sop.md)
10. [PowerShell prompt copy/paste errors](10-powershell-prompt-copy-paste-errors.md)
11. [Wazuh service verification workflow](11-wazuh-service-verification.md)
12. [VMware kernel module verification](12-vmware-kernel-modules-verification.md)
13. [VMware memory sizing for two-VM lab](13-vmware-memory-sizing-two-vms.md)
14. [VMware installation ISO still attached](14-vmware-installation-iso-still-attached.md)
15. [Windows persistence-lab account cleanup](15-windows-persistence-lab-account-cleanup.md)
16. [External SSD VM startup and shutdown SOP](16-external-ssd-startup-shutdown-sop.md)
17. [Host disk-space monitoring](17-disk-space-monitoring-lab-host.md)
18. [Network-interface baseline checks](18-network-interface-baseline.md)
19. [VMware Tools popup is not a VM boot failure](19-vmware-tools-popup-not-an-error.md)
20. [Wireshark SSH stream appears unreadable](20-wireshark-ssh-stream-looks-unreadable.md)
21. [Wireshark TLS Client Hello is missing](21-wireshark-client-hello-missing.md)
22. [Wireshark capture-filter vs display-filter confusion](22-wireshark-capture-vs-display-filter-confusion.md)
23. [Wazuh repository caused an unintended package upgrade](23-wazuh-repository-unintended-upgrade.md)
24. [Persistent external SSD mount by UUID](24-persistent-external-ssd-mount-by-uuid.md)

## Automated Privacy Audit

The repository now includes:

```text
scripts/audit_public_content.py
.github/workflows/privacy-audit.yml
```

The workflow checks public tracked files on pushes and pull requests for common private-key markers, GitHub/AWS token patterns, unexpected literal IPv4 addresses, UUID-like identifiers in documentation, and sensitive key filenames.

Automation is an additional safety layer, not a replacement for human review.

## Troubleshooting Method Used

The recurring workflow used throughout Month 1 was:

1. Observe the symptom.
2. Collect evidence.
3. Verify assumptions.
4. Isolate the failing layer.
5. Identify the root cause.
6. Apply the smallest safe fix.
7. Verify the fix.
8. Restore the lab to a known-good state when the exercise is finished.
9. Document the outcome without publishing secrets.

This approach is intentionally tool-agnostic and reusable for SOC triage, Linux administration, Windows troubleshooting, networking, SIEM maintenance, packet analysis, and virtualization issues.

## Documentation Standard

Each future troubleshooting note should answer:

- What was the symptom?
- What evidence was collected?
- What assumptions were ruled out?
- What was the root cause?
- What was changed?
- How was the fix verified?
- What should be done differently next time?
- Has all sensitive information been removed before publication?
