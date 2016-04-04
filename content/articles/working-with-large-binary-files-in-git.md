Title: Working with large binary files in git
Date: 2013-07-02 11:33
status: draft
Tags: git, version-control 
Slug: working-with-large-binary-files-in-git
Summary: A note on how I'm managing large media files in public git respositories.

### Headlines and horizontal rules

[stackoverflow](http://stackoverflow.com/questions/540535/managing-large-binary-files-with-git)


+ [git-annex](http://git-annex.branchable.com)
+ [git-fat](https://github.com/jedbrown/git-fat)
+ [git-media](https://github.com/schacon/git-media)

[what git-annex is not](http://git-annex.branchable.com/not/)

`.gitattributes` at the top-level of the directory:

```bash
*.wav filter=fat -crlf
*.mp4 filter=fat -crlf
*.tgz filter=fat -crlf
*.gz filter=fat -crlf
```




`.gitfat`  


```bash
[rsync]
remote = user@server.host.com:/home/user/ldc-kiy 
```

I kept this from being uploaded to github by including the following
in `.gitignore':

```bash
.gitfat
```


