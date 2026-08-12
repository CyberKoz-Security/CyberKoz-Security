# Git Initialized in the Wrong Directory

## Symptom

`git init` was accidentally run in the Linux home directory instead of inside the intended project folder. Running `git add .` from the home directory risked tracking unrelated personal and system files.

## Root Cause

Git creates repository metadata in the current working directory. Because the command was executed from `~`, the repository root became the user's home directory rather than the intended portfolio project directory.

## Investigation

```bash
pwd
ls -la ~ | grep .git
git status
```

## Fix

Move into the intended project directory first:

```bash
cd <PROJECT_DIRECTORY>
pwd
git init
git branch -m main
git status
```

Only then stage and commit the files that belong to that project.

## Verification

```bash
git log --oneline
git status
```

The repository should show the intended project history and a clean working tree after the commit.

## Lesson Learned

Before running `git init`, always verify the working directory with `pwd`. Repository initialization is a scope decision: Git treats everything beneath that directory as potentially trackable unless excluded.
