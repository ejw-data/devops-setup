# Commit Standards

Historically, I have just added short commit messages that only utilized a subject line.  In the future I would like to to develop the habit of having a subject line and body to each commit with a standard format of what each commit can contain.

## Setting VSCode as Default git editor
Type:  `git config --global core.editor "code --wait"`

## Searching git history
Sometimes you might need to know the change history of a specific file.  This command returns the commit info including the commit message and the diff.
* Type:  `git log --follow <file>`
* Alternate method type:  `git log --all --full-history -- **/<file>.*`

To just view the git history then use this command to display the most recent commits.
*  Type:  `git log`

To view a specific commit and its changes use:
*  Type:  `git show <SHA> -- <path-to-file>`

To access to the file and continue development then use:
*  Type:  `git checkout <commit>`


## Git remote checkout
**NOTE**: Checkout has multiple uses.  Using `git checkout` resets the current branch's code back to the most recent commit.  Other uses of checkout have been replaced with more specific commands to avoid confusion.  Using `git swtich <branch>` changes to a different branch but will not overwrite the existing branch.  Using `git restore <file>` converts a specific file to its most recent commit.  It should also be noted that `git switch <remote branch>` will automatically fetch the remote branch when switching and `git checkout <remote branch>` will not not do this check.  Also if you use `git checkout <remote branch>`, git will think you want to make your own local branch called `<remote branch>` but will recognize that there is already branch(s) named this in the repo and will respond with an error due to the ambiguity.  Another way to get around this is by doing this:
```bash
$ git fetch origin
$ git checkout origin/<remote branch name>
```
OR
```bash
$ git stitch remote/<remote branch name>
```

## Other helpful git commands
*  To view all branches use `git branch -a`.
*  To see the current status of your repo and all files within directories and not just the parent directory use `git status -u`.
*  In VSCode settings.json, this can be added at the end of the file to include vertical guidelines at 72 and 80 characters:
    ```bash
    "[git-commit]": {
    "editor.rulers": [72, 80],
    "editor.wordWrap": "off"
    }
    ```

## Standard Format
*  Currently, each branch that is tested with pre-commit has a prefix of `Cleaned` added to the beginning of the messaged.  If the branch does not run pre-commit then it is given the prefix of `Raw`.
*  Subject line less than or equal to 72 characters in length
*  Body line length limited to 80 characters
*  Use sentence case for commit subject line with no period
*  Use present tense imperative for the subject line and present tense for body text
*  Use the footer to reference related issues

**Examples**:
```feat(home): add signup link to home page```
```fix(signup): allow signup button to be clicked```

**Automated Package**:
* `Commitlint` - enforces rules for commits
