# Publication Safety and Sanitization Rules

This troubleshooting knowledge base is public-facing documentation. It intentionally excludes secrets and unnecessary identifying information.

## Never Publish

- Passwords or passphrases
- API tokens, PATs, session cookies, or recovery codes
- SSH private keys or private-key contents
- Wazuh-generated administrator credentials
- Windows or Linux account passwords
- Full personal usernames when they are not required for the lesson
- Personal email addresses unless already intentionally public
- Private repository URLs or restricted evidence
- Exact device UUIDs, serial numbers, or hardware identifiers unless there is a strong reason
- Screenshots containing credentials, tokens, private keys, personal files, or browser sessions

## Use Placeholders Instead

Examples:

```text
<LAB_USER>
<WINDOWS_USER>
<UBUNTU_SERVER>
<LAB_IP>
<EXTERNAL_SSD_UUID>
<WAZUH_ADMIN_PASSWORD>
```

## Safe Documentation Pattern

Document the troubleshooting method and command structure, not the secret values used in the lab.

For example, prefer:

```bash
ssh <WINDOWS_USER>@<WINDOWS_IP>
```

instead of publishing the real username and address.

## Evidence Standard

A public note should preserve enough technical detail to reproduce the troubleshooting logic while removing credentials, private keys, tokens, personal data, and unnecessary internal identifiers.
