# ShieldX SOC Journey - Month 1 Closure

## Status

**Month 1: Completed**

The Month 1 foundation phase concluded with the lab operational and the major troubleshooting incidents converted into reusable documentation.

## Foundation Covered

- Linux fundamentals and administration
- Filesystem navigation and permissions
- Users, groups and ACL concepts
- Processes, services and system logs
- Networking fundamentals and troubleshooting
- SSH and public-key authentication concepts
- Wireshark packet analysis
- tcpdump fundamentals
- Netcat fundamentals
- Nmap introductory use in the authorized lab
- Wazuh SIEM deployment and basic investigation
- VMware lab operation and recovery
- Windows endpoint lab preparation

## Lab Model

- Kali Linux - analyst workstation / virtualization host
- Ubuntu VM - Wazuh server
- Windows 10 VM - endpoint lab
- VMware Workstation - virtualization platform
- External SSD - removable storage for selected VM files

Exact account names, IP addresses, UUIDs, credentials and private infrastructure values are intentionally omitted.

## Troubleshooting Archive

The knowledge base contains numbered runbooks covering Wazuh, SSH, Git, VMware, NTFS/external storage, Windows lab maintenance, networking and Wireshark.

Start with:

- [Main troubleshooting index](README.md)
- [Category navigation](CATEGORIES.md)
- [Lab health verification SOP](09-lab-health-verification-sop.md)
- [Security sanitization rules](SECURITY-SANITIZATION.md)
- [Evidence publication guide](EVIDENCE-GUIDE.md)

## Privacy Controls

The public repository includes an automated privacy-audit workflow. It is designed to catch common secret markers, unexpected literal IP addresses, UUID-like identifiers in documentation and sensitive key filenames before future public changes are treated as complete.

Automation complements manual review; it does not replace it.

## Month 1 Operational Principle

```text
Observe
  -> collect evidence
  -> verify assumptions
  -> isolate the failing layer
  -> identify root cause
  -> apply the smallest safe fix
  -> verify again
  -> restore known-good state
  -> document safely
```

## Transition

Month 2 begins with Windows Internals and deeper SOC investigation. Month 1 remains the foundation and troubleshooting reference rather than a topic to repeatedly restart.
