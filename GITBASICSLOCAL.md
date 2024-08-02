# Local and remote repos communication
### Setting up user id and email as authenticator in local repo
```
git config --global user.name "DimpleB51"
git config --global user.email dimple.bhuta@tihiitb.org
```

To check if you have correctly configured github credentials RUN,
```
git config user.name && git config user.email
```

### Git init
`git init`

### Track changes to github repo
`git status`

### Add and commit the changes
```
git add .
git commit -m "first version of the website"
```
### Set origin
`git remote add origin https://github.com/<UserName>/<RepoName>.git`

### Rename local branch
`git branch -M main`

### And push your updates online
`git push origin main`

### And pull your updates online
`git pull origin main`
