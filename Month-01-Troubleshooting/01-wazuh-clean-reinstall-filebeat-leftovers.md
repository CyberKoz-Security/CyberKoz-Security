# Wazuh Clean Reinstall Blocked by Filebeat Leftovers

## Symptom

A fresh Wazuh all-in-one installation failed with an installer message indicating that Filebeat was already installed, even though package checks showed no active Filebeat package.

## Environment

- Ubuntu VM used as the Wazuh server
- Wazuh 4.14.x all-in-one deployment

## Investigation

Package-level checks did not show Filebeat as installed, so the investigation moved to service and filesystem remnants.

Useful checks included:

```bash
dpkg -l | grep filebeat
apt list --installed 2>/dev/null | grep filebeat
which filebeat
find /etc /var /usr /run /sys -iname '*filebeat*' 2>/dev/null
```

The remaining artifacts included service links, runtime/service traces, data/log directories, and cached package material.

## Root Cause

The previous Filebeat installation had been removed at the package level, but residual service/data artifacts remained. The Wazuh installer detected these leftovers and refused to continue as a clean deployment.

## Fix

The stale Filebeat service links and remaining Filebeat data/configuration directories were removed. The system was rebooted before rerunning the Wazuh installer.

Examples of areas that were reviewed/cleaned:

```text
/etc/systemd/system/multi-user.target.wants/filebeat.service
/etc/rc*.d/
/var/lib/filebeat
/var/log/filebeat
/etc/filebeat
/usr/share/filebeat
```

After reboot, the Wazuh all-in-one installer was run again and completed successfully.

## Verification

The successful deployment was verified by checking the core services:

```bash
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status filebeat --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

Expected state: `active (running)`.

## Lesson Learned

Package removal does not always equal complete application cleanup. During reinstall troubleshooting, check packages, services, symlinks, data directories, logs, and cached artifacts before concluding that a product is fully removed.
