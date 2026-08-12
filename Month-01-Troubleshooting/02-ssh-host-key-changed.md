# SSH Remote Host Identification Changed

## Symptom

SSH from Kali to the Windows 10 lab endpoint failed with:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
Host key verification failed.
```

## Root Cause

Kali had an older SSH host key stored for the same IP address. The Windows endpoint had been rebuilt or its SSH host key had changed, so the key presented by the current server no longer matched the entry in `~/.ssh/known_hosts`.

## Investigation

SSH identified the exact offending line and suggested removing the stale host entry.

```bash
ssh-keygen -f ~/.ssh/known_hosts -R 192.168.18.76
```

## Fix

The stale host-key entry was removed. SSH was attempted again, and the new ED25519 fingerprint was reviewed before accepting it.

```bash
ssh wikf@192.168.18.76
```

After confirming the new fingerprint belonged to the intended lab host, the prompt was accepted with `yes`.

## Verification

SSH reported that the new key had been permanently added to `known_hosts`, and the connection proceeded to authentication.

## Security Lesson

Never blindly ignore a host-key mismatch. In a real environment, the same warning can indicate a man-in-the-middle attack. First verify whether the host was rebuilt, reinstalled, or intentionally had its SSH keys changed. Only then remove the stale entry and trust the new key.
