# Git Initialized in the Wrong Directory

## Symptom

`git init` was accidentally run in the Kali home directory instead of inside the intended project folder. Running `git add .` from the home directory risked tracking unrelated personal and system files.

## Root Cause

Git creates repository metadata in the current working directory. Because the command was executed from `~`, the repository root became `/home/shieldx` rather than the portfolio project directory.

## Investigation

The current location and repository state were checked with:

```bash
pwd
ls -la ~ | grep .git
git status
```

The intended project directory was:

```text
/home/shieldx/ShieldX-Portfolio/03-Passwordless-SSH
```

## Fix

The project directory was entered explicitly and Git was initialized there:

```bash
cd ~/ShieldX-Portfolio/03-Passwordless-SSH
git init
git branch -m main
git status
```

Files were then added and committed from the correct repository root.

## Verification

```bash
git log --oneline
git status
```

The repository showed the expected project commit and a clean working tree.

## Lesson Learned

Before running `git init`, always verify the working directory with `pwd`. Treat repository initialization as a scope decision: Git will consider everything beneath that directory part of the repository unless excluded.
