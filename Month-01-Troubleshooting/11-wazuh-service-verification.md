# Wazuh Service Verification Workflow

## Purpose

After installation, upgrade, reboot, or troubleshooting, verify that the Wazuh stack is actually running before investigating higher-level alerts.

## Checks

On the Wazuh server, verify the main services individually:

```bash
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status filebeat --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

## Healthy Result

Each required service should report an active/running state appropriate to the deployment.

## If a Service Is Not Healthy

Review recent logs before restarting blindly:

```bash
sudo journalctl -u <SERVICE_NAME> -n 100 --no-pager
```

Then fix the actual configuration, dependency, certificate, storage, or permission issue revealed by the logs.

## Verification

Re-run `systemctl status` and confirm the dashboard and agent communications work as expected.

## Lesson Learned

Always verify the platform layer before assuming an alerting or dashboard problem is caused by the agent or rule logic.
