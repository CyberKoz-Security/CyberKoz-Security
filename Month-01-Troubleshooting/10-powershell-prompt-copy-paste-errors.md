# PowerShell Prompt Copy/Paste Errors

## Symptom

Commands failed with messages such as `Get-Process` receiving unexpected arguments, command names being treated as literal input, or table output being executed as commands.

## Root Cause

The PowerShell prompt text (for example `PS C:\Users\<WINDOWS_USER>>`) and/or previous command output was copied back into the shell along with the real command.

## Investigation

Check whether the entered line begins with the shell prompt or contains output columns such as `Name`, `Enabled`, or separator rows.

## Fix

Type only the command itself. Example:

```powershell
Get-LocalUser | Select-Object Name,Enabled,LastLogon
```

Do not include the visible prompt.

## Verification

The command returns structured PowerShell output rather than parser or positional-parameter errors.

## Lesson Learned

Terminal prompts and command output are not part of the command. When copying from documentation, copy only the command text inside the code block.
