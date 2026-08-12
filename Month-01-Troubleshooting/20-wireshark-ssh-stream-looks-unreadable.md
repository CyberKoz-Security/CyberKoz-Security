# Wireshark SSH Stream Looks Unreadable

## Symptom

`Follow TCP Stream` on an SSH connection shows binary or unreadable data instead of the commands typed during the session.

## Root Cause

SSH encrypts application data after key exchange. Wireshark can reconstruct the TCP conversation but cannot normally read the protected SSH payload without appropriate session secrets.

## Investigation

Filter the connection:

```text
tcp.port == 22
```

Select an SSH/TCP packet and use:

```text
Follow -> TCP Stream
```

## Expected Result

Early protocol banners may be visible, while most session content appears encrypted/unreadable.

## SOC Value Despite Encryption

An analyst can still examine:

- Source and destination addresses
- Client/server ports
- Connection start and end
- Packet volume
- Timing
- Session duration
- TCP resets/retransmissions

## Lesson Learned

Unreadable SSH payload is usually evidence that encryption is working, not evidence that Wireshark is broken.
