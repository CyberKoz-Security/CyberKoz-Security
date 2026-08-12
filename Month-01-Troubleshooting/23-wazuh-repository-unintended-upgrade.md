# Wazuh Repository Caused an Unintended Upgrade

## Symptom

A normal package upgrade unexpectedly upgraded Wazuh components when the goal was to perform a clean reinstall later.

## Root Cause

The Wazuh package repository was still configured, so the package manager considered Wazuh components eligible for upgrade.

## Investigation

Check installed packages and configured repositories before major maintenance:

```bash
dpkg -l | grep wazuh
```

Review repository files under the system package-manager configuration before running broad upgrade commands.

## Safe Recovery Pattern

1. Stop affected Wazuh services.
2. Purge the unintended packages if a clean rebuild is the objective.
3. Remove stale configuration/data directories only after confirming they are no longer needed.
4. Remove or disable the repository if it should not participate in future upgrades.
5. Verify with package queries before reinstalling.

## Verification

Confirm that the intended package state matches the maintenance plan before running the installer again.

## Lesson Learned

Repository configuration is part of change control. A generic system upgrade can modify security tooling if its repository remains enabled.
