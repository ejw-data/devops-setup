# Custom Git Command Setup

### Setup Directory
1.  I prefer to put all folders like this in my root directory so first open `Git Bash` and do the following:
1.  Type `cd ~`
1.  Type `mkdir custom-git-commands`
1.  Type `touch git-autopush`
1.  Add code to file
1.  You may need to make the file executable by typing  `chmod +x git-autopush`.
1.  Next navigate to `.bash_profile` or .`.bashrc` for windows or `.zshrc` for mac.  These files are typically in the home/root directory (`cd ~`)
1.  Add this line of code to the file: `export PATH=$PATH:"/C/Users/<username>/git-custom-commands"` for windows or `export PATH=$PATH:/<userdirectory>/my-git-custom-commands` for mac
1.  Lastly, run the file by typing: `source ~/.bash_profile` or the other file listed above that you added your code.  If everything works, then there should be no message.
1.  The code should work now.  If you have problems running any of the other git commands then there is a problem with how the Path was set above.
1.  Close out terminal and go to an existing repo.


### Sample Script

```bash
#!/bin/sh

message=$1 # First parameter will be the commit message
currentBranch=$(git symbolic-ref --short -q HEAD) # Getting the current branch

while : ; do
    read -p "Do you want to apply pre-commit checks?  [y/n]" RESPONSE < /dev/tty
    case "${RESPONSE}" in
        [Yy]* )
            if [ ! -z "$1" ] # checking if the commit message is present. If not then aborting.
            then
                git add .
                git commit -m "$message"
                git push origin $currentBranch
            else
                echo "Commit message is not provided"
            fi
            exit 0;
            break;;
        [Nn]* )
            if [ ! -z "$1" ] # checking if the commit message is present. If not then aborting.
            then
                git add .
                git commit -m "$message" --no-verify
                git push origin $currentBranch
            else
                echo "Commit message is not provided"
            fi
            exit 1
            ;;
    esac
done



```
