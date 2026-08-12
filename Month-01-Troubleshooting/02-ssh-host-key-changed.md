# SSH Remote Host Identification Changed

## Symptom

SSH from the analyst workstation to a Windows lab endpoint failed with:

```text
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
Host key verification failed.
```

## Root Cause

The client had an older SSH host key stored for the same lab endpoint. The target system had been rebuilt or its SSH host key had changed, so the newly presented key no longer matched the entry in `~/.ssh/known_hosts`.

## Investigation

SSH identifies the offending host entry. After verifying that the lab system was intentionally rebuilt or had legitimate key changes, remove only that stale entry:

```bash
ssh-keygen -f ~/.ssh/known_hosts -R <WINDOWS_IP>
```

## Fix

Reconnect using placeholders rather than publishing real lab identifiers:

```bash
ssh <WINDOWS_USER>@<WINDOWS_IP>
```

Review the new fingerprint and accept it only after confirming it belongs to the intended lab endpoint.

## Verification

SSH reports that the new key was added to `known_hosts`, and the connection proceeds to authentication.

## Security Lesson

Never blindly ignore a host-key mismatch. In a real environment, the same warning can indicate a man-in-the-middle attack. Verify the reason for the key change before trusting the replacement key.
