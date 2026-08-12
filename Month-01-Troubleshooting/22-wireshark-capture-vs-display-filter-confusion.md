# Wireshark Capture Filter vs Display Filter Confusion

## Symptom

A filter works in one place in Wireshark but fails in another.

## Root Cause

Wireshark uses different syntaxes for capture filters and display filters.

## Examples

Capture filter (before packets are recorded):

```text
port 22
host <LAB_IP>
```

Display filter (after packets are captured):

```text
tcp.port == 22
ip.addr == <LAB_IP>
```

## Troubleshooting

If Wireshark rejects a filter, first ask whether it is being entered in the capture-filter field or display-filter field.

## Lesson Learned

Capture filters decide what gets recorded. Display filters decide what is shown from an existing capture. Mixing the two syntaxes is a common beginner error.
