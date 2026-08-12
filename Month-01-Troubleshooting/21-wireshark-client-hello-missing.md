# Wireshark TLS Client Hello Missing

## Symptom

A TLS capture contains mostly `Application Data` packets and no obvious `Client Hello` or `Server Hello`.

## Root Cause

The capture often started after the TLS session had already been established, or the browser reused an existing connection.

## Investigation

- Confirm the display filter is appropriate, such as `tls`.
- Check whether the capture began before the browser initiated the connection.
- Consider existing persistent browser connections.

## Fix for a Clean Lab Capture

1. Start a fresh capture first.
2. Then initiate a new connection or browser request.
3. If necessary, close/reopen the browser or use a fresh test connection in the authorized lab.
4. Stop the capture and inspect the handshake packets.

## Lesson Learned

Packet capture timing matters. A packet analyzer can only display events that were actually captured.
