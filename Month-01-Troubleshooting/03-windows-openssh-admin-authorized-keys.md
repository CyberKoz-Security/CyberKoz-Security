# Windows OpenSSH Administrator Public-Key Authentication

## Symptom

Passwordless SSH to a Windows lab host continued to ask for a password even though the public key had been added to the user's normal `authorized_keys` file.

## Investigation

The OpenSSH service was running, but the target account belonged to the local Administrators group. Windows OpenSSH can use this centralized key file for administrator accounts:

```text
C:\ProgramData\ssh\administrators_authorized_keys
```

## Root Cause

Administrator accounts can be matched by the `Match Group administrators` section in `sshd_config`, causing OpenSSH to use the centralized administrators key file instead of the per-user file.

## Fix

Place only the public key in:

```text
C:\ProgramData\ssh\administrators_authorized_keys
```

Restrict permissions:

```powershell
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /grant "Administrators:F"
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /grant "SYSTEM:F"
Restart-Service sshd
```

## Verification

From the client:

```bash
ssh <WINDOWS_USER>@<WINDOWS_IP>
```

The connection should complete without prompting for the Windows account password when the key configuration is correct.

## Security Note

Never publish the private key, account password, or any secret key material. Public documentation should contain only placeholders and general procedure.

## Lesson Learned

When troubleshooting Windows public-key authentication, always check whether the target account is an administrator and inspect the relevant `sshd_config` match rules.
