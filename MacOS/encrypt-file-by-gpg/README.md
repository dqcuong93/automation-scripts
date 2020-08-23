#HOW TO USE GPG TO ENCRYPT/DECRYPT FILES

##INSTALL GNUPG (or GPG) BY HOMEBREW
```zsh
brew install gnupg
```
After install GPG, copy all files: 'gpg-agent.conf' & 'gpg.conf' to your folder '.gnupg' (create this folder if you did not 
have one). In file 'gpg.conf': use ```no-symkey-cache``` to remove password cached!

##TO ENCRYPT
```zsh
gpg -c test.txt
```

##TO DECRYPT
```zsh
gpg test.txt.asc
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

##Reference 
https://dev.to/efe/how-to-use-gnupg-for-encrypting-files-on-macos-2kke
