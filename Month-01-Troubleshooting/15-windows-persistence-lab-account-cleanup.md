# Windows Persistence Lab Account Cleanup

## Scenario

A temporary local account was created and added to the local Administrators group to generate Windows security events for a Wazuh detection lab.

## Cleanup Goal

Return the endpoint to its pre-lab state after evidence collection.

## Safe Cleanup

Run PowerShell with appropriate administrative privileges:

```powershell
Remove-LocalGroupMember -Group "Administrators" -Member "<LAB_ACCOUNT>"
Remove-LocalUser -Name "<LAB_ACCOUNT>"
```

## Verification

```powershell
Get-LocalUser | Select-Object Name,Enabled
Get-LocalGroupMember -Group "Administrators"
```

Confirm the temporary account no longer exists and is no longer a privileged group member.

## SOC Relevance

The corresponding create/add/remove/delete events can be correlated in Windows Event Logs and Wazuh to build a complete timeline.

## Lesson Learned

Every simulation should include rollback. Creating persistence for a detection exercise without removing it afterward leaves the lab in an unknown state and can contaminate future investigations.
