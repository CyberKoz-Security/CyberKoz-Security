#!/usr/bin/env python3
"""Fail when public portfolio files contain common secret or lab-identifier patterns."""

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

try:
    tracked_names = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
except (OSError, subprocess.CalledProcessError) as exc:
    raise SystemExit(f"Unable to list tracked files: {exc}")

text_suffixes = {".md", ".txt", ".yml", ".yaml", ".json", ".py", ".sh", ".ps1", ".gitignore"}
errors = []

secret_patterns = {
    "private-key marker": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "GitHub token": re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "generic bearer token": re.compile(r"Authorization:\s*Bearer\s+[A-Za-z0-9._~+/=-]{20,}", re.I),
}

# Literal IPv4 addresses are blocked except documentation-only example ranges and loopback.
ip_pattern = re.compile(r"(?<![0-9.])(?:\d{1,3}\.){3}\d{1,3}(?![0-9.])")
allowed_ips = {
    "127.0.0.1",
    "192.0.2.1", "192.0.2.10",
    "198.51.100.1", "198.51.100.10",
    "203.0.113.1", "203.0.113.10",
}

# Long hexadecimal strings can be legitimate hashes, so only flag UUID-like values in documentation.
uuid_pattern = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")

for relative in tracked_names:
    path = ROOT / relative
    if path.is_dir():
        continue
    if path.suffix.lower() not in text_suffixes and path.name != ".gitignore":
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    for label, pattern in secret_patterns.items():
        if pattern.search(text):
            errors.append(f"{relative}: {label} found")

    for address in ip_pattern.findall(text):
        octets = address.split(".")
        if all(part.isdigit() and 0 <= int(part) <= 255 for part in octets) and address not in allowed_ips:
            errors.append(f"{relative}: literal IPv4 address found: {address}")

    if path.suffix.lower() in {".md", ".txt"}:
        for value in uuid_pattern.findall(text):
            errors.append(f"{relative}: UUID-like identifier found: {value}")

for relative in tracked_names:
    name = Path(relative).name.lower()
    if name in {"id_rsa", "id_ed25519", "authorized_keys", ".env", "credentials", "secrets"}:
        errors.append(f"sensitive filename tracked: {relative}")
    if Path(relative).suffix.lower() in {".pem", ".key", ".p12", ".pfx", ".ppk"}:
        errors.append(f"sensitive key/certificate filename tracked: {relative}")

if errors:
    print("Privacy audit FAILED:")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"Privacy audit passed for {len(tracked_names)} tracked paths.")
