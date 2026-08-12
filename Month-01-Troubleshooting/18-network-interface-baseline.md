# Network Interface Baseline Checks

## Purpose

Before troubleshooting VMware guests or SOC tools, verify that the host networking layer is healthy.

## Commands

```bash
ip -br addr
ip route
```

Optional connectivity checks:

```bash
ping -c 4 <DEFAULT_GATEWAY>
ping -c 4 <KNOWN_EXTERNAL_IP>
```

Then test DNS separately:

```bash
getent hosts <KNOWN_DOMAIN>
```

## What to Look For

- Physical interface state
- Expected host IP addressing
- VMware virtual adapters such as host-only/NAT interfaces if they are part of the design
- A valid default route
- Separation of raw IP connectivity from DNS resolution

## Lesson Learned

Do not blame a guest VM or application until the host network baseline is known-good. Layered troubleshooting saves time and reduces unnecessary changes.
