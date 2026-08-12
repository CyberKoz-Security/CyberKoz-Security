# Windows OpenSSH Administrator Public-Key Authentication

## Symptom

Passwordless SSH from Kali to the Windows 10 lab host continued to ask for a password even though the public key had been added to:

```text
C:\Users\wIKF\.ssh\authorized_keys
```

## Investigation

The OpenSSH service was running, and the user-level `authorized_keys` file existed. The Windows OpenSSH configuration contained a special rule for members of the local Administrators group:

```text
AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```

The target account was confirmed to be a member of the local Administrators group.

## Root Cause

For administrator accounts, Windows OpenSSH uses the centralized file:

```text
C:\ProgramData\ssh\administrators_authorized_keys
```

instead of the normal per-user `authorized_keys` path.

## Fix

The Kali ED25519 public key was placed in:

```text
C:\ProgramData\ssh\administrators_authorized_keys
```

File permissions were restricted using `icacls` so that only Administrators and SYSTEM had full control.

```powershell
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /grant "Administrators:F"
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /grant "SYSTEM:F"
Restart-Service sshd
```

## Verification

From Kali:

```bash
ssh wikf@192.168.18.76
```

The login completed without prompting for the Windows account password.

## Lesson Learned

When troubleshooting public-key authentication on Windows, always check whether the account is an administrator and inspect the `Match Group administrators` section in `sshd_config`. Windows may intentionally use a different key file for privileged users.
