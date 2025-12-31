# GIT ANGLE BY KAILA

### 1. `git clone`
This command:  
+ Downloads a remote repo
+ Creates a local folder
+ Sets up `origin` automatically
When to use:  
+ A repo exists on github but we want it loaclly
```bash
git clone https://github.com/Polymath-Kaila/python-backend-developer-roadmap

```
---------------------------------

### 2. `git status`
This command:  
+ Shows what git sees
+ Tells us whats staged,unstaged,untracked
When to use:  
+ Constantly (seriusly).  
If confused `git status`.  
```bash
git status
```
---------------------------------

### 3. `git add`
This command.    
+ Moves changes from working directory to staging area
```bash
git add file.py # stage one file
git add .       # stage everything 
```
----------------------------------

### 4. `git commit -m`
This command:  
+ creates a snapshot in history
```bash
git commit -m "Meaningful message"
```
-----------------------------------

### 5. `git push`
This command:  
+ Sends our local commits to the remote(Github)
```bash
git push -u origin main,dev, etc # depending on your branch
```
----------------------------------

### 6. `git pull`
This command:  
+ Fetches remote commits
+ Merges or rebases them ito your our branch
If on main branch do.  
```bash
git pull origin main 
# this is saying update my local main with remote main
```
If on a feature branch(feature-x).  
```bash
git pull origin feature-x
# this is saying update my loacl feature-x with remote feature-x
```
When to pull from `main` while on another branch.  
```bash
git pull --rebase origin main
# we rebase the feature onto the main branch
# meaning replay my feature commits on top of the latest main
```
#### common scenarios for pull & rebase
1. solo project
   This is mainly on `main` branch.  
   So we do:  
 ```bash
   git pull --rebase
   git push
 ```
2. Team project
   Here `main` is protected
   We do:  
 ```bash
 git checkout feature-x
 git pull --rebase origin main
 # work
 git push origin feature-x
 ```
 Then open a PR.  
`pull from the branch we want our current branch to be based on`

---------------------------------

### 7. `.gitignore`
This is a file not command:  
+ prevents new files from being tracked
Used for:  
+ `venv/`
+ `node_modules`
+ `.env`

---------------------------------

### 8. `git rm --cached`
This command:  
+ Stops tracking a file
+ Keeps it on disk
```bash
git rm --cached file.txt
git rm --cached venv
# git forget this file!
```
--------------------------------

### 9. `git reset --hard`
This command is Dengerous but powerful:  
+ It makes the local branch `EXACTLY` match another commit/branch
+ Deletes local uncommited changes
```bash
git reset --hard origin/main
```
When to use:  
+ Local repo is broken
+ We want a clean slate

--------------------------------

### 10. `git rebase --abort`
This command:  
+ Cancels a rebase in progress
Used when:  
+ Rebase goes sideways
+ We want to bail out safely

-------------------------------

### 11. `git branch`
```bash
git branch
git branch feature-x
```
This is branching.  then...
### 12. `git checkout`
```bash
git checkout feature-x
git checkout -b new-feature
```
-----------------------------

### 13. `git merge`
```bash
git merge feature-x
```
This combines histories.  
Used mostly in feature branches.  
In long lived branches.  

------------------------------

## Oh Sh*t Scenarios
#### 1. Accidentally pushed secrets(API keys etc)
`Step 1`: Rotate the Secret Immediately.  
`Step 2`: Remove it from code.  
```bash
# delete from file
git commit -am "Remove secret"
git push
```
`step 3`: Purge it from Git history.  
`git filter-repo`.  
```bash
git filter-repo --path .env --invert-paths
# then: 
git push --force
```
#### 2. I committed a file i didn't mean to(but havent't pushed)
```bash
git reset HEAD~1
```
+ Commit undone
+ Changes still on disk

#### 3. I want to undo a pushed commit
```bash
git revert <commit-hash>
```
This creates a new commit that undoes the old one.  
Preferred on shared branches.  

#### 4. I messed up locally & just want to start over
```bash
git fetch origin
git reset --hard origin/main
```
---------------------------------

## stashing
### 1. `git stash`
This temporarily hides uncommitted changes.  

```bash
git stash
```
### 2. `git stash pop`
Restores the hidden commits.  

```bash
git stash pop
```
--------------------------

## Ispecting History(Debugging Superpowers)

### 1. `git log`
```bash
git log --online --graph --all
```
### 2. `git diff`
```bash
git diff   # ustaged
git diff --staged # staged
```
--------------------------

## Proffessional Git Rules
1. Pull before push
2. Never commit secrets
3. Never commit generated files
4. Use --rebase on shared branches
5. If confused → git status
6. If scared → don’t force push
7. If solo → force push is fine
8. History matters, but clarity matters more

