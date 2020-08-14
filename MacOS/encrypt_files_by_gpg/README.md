#HOW TO USE GPG TO ENCRYPT/DECRYPT FILES

##INSTALL GNUPG (or GPG) BY HOMEBREW
```
brew install gnupg
```
After install GPG, copy all files: 'gpg-agent.conf' & 'gpg.conf' to your folder '.gnupg' (create this folder if you did not 
have one). In file 'gpg.conf': use ```no-symkey-cache``` to remove password cached!

##TO ENCRYPT
```
gpg -c test.txt
```

##TO DECRYPT
```
gpg test.txt.asc
```

##Reference 
https://dev.to/efe/how-to-use-gnupg-for-encrypting-files-on-macos-2kke
