# Privacy-Safe Evidence Publication Guide

Screenshots and logs can strengthen a portfolio, but they can also expose secrets. Use this guide before publishing any Month 1 evidence.

## Safe Evidence Checklist

Before publishing a screenshot or log:

- Crop to the smallest area that proves the result.
- Remove passwords, passphrases, PATs, tokens, API keys, cookies, recovery codes, and Wazuh-generated credentials.
- Never show an SSH private key or full private-key path containing sensitive user information.
- Replace personal usernames with placeholders when the username is not part of the learning objective.
- Mask exact lab IP addresses unless they are documentation-only RFC 5737 examples.
- Mask device UUIDs, serial numbers, MAC addresses, and unnecessary hardware identifiers.
- Remove browser tabs, bookmarks, email addresses, cloud-account details, and personal files from screenshots.
- Do not publish private repository URLs or evidence copied from restricted projects.
- Review terminal history visible above and below the command you intend to show.
- Re-open the exported image and verify the redaction is actually baked into the image.

## Preferred Placeholder Style

```text
<LAB_USER>
<WINDOWS_USER>
<WINDOWS_IP>
<UBUNTU_IP>
<MOUNT_POINT>
<EXTERNAL_SSD_UUID>
<WAZUH_ADMIN_PASSWORD>
```

## Good Evidence

A good screenshot proves one thing clearly, for example:

- a service is active,
- a VM configuration file is visible after mounting storage,
- a Wireshark filter returns the expected protocol,
- Wazuh shows a sanitized event,
- an SSH connection succeeds without exposing credentials.

## Avoid

- full desktop screenshots when a cropped terminal result is sufficient,
- screenshots containing password prompts plus typed secrets,
- unredacted IP-address tables,
- full browser sessions,
- raw private keys,
- exported logs containing personal or unrelated data.

## Evidence Naming

Use descriptive names without sensitive values:

```text
01-wazuh-services-running.png
02-external-ssd-mounted.png
03-ssh-key-auth-success.png
04-wireshark-dns-filter.png
```

## Rule

If the learning objective can be demonstrated without publishing a sensitive value, do not publish that value.
