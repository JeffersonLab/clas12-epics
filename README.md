# clas12-slowctrls
Top-level for CLAS12 release tree

## Adding subtrees
```
git subtree add --prefix clon https://github.com/jeffersonlab/clas12-clon master
git subtree add --prefix coda https://github.com/jeffersonlab/clas12-coda master
git subtree add --prefix epics https://github.com/jeffersonlab/clas12-epics master
git subtree add --prefix parms https://github.com/jeffersonlab/clas12-parms master
```

## Commiting Changes
```
cd epics/
vim README.md
git add README.md
git commit -m "Added blah blah blah"

# push to clas12-slowctrls
git push origin master
# push to clas12-epics (must be in the top level)
cd ..
git subtree push --prefix epics https://github.com/jeffersonlab/clas12-epics master
```
