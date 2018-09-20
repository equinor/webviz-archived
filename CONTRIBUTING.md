#Contributing to Webviz
The following is a set of guidelines for contributing to Webviz. Use your best
judgement at feel free to propose changes to this document in a pull request.

##Issues
Issues are created [here](https://github.com/Statoil/webviz/issues/new).

When creating a new issue, please use this format when explaining your problem:
* Expected behavior
* Actual behavior
* How to reproduce

##Pull Requests


### Step 1: Fork
Fork the project [on Github](https://github.com/Statoil/webviz) and clone your fork locally
```sh
$ git clone git@github.com:username/webviz.git
$ cd electron
$ git remote add upstream https://github.com/Statoil/webviz.git
$ git fetch upstream
```

### Step 2: Build
Follow the [build steps](https://github.com/Statoil/webviz/blob/master/README.md) to build
the project locally. Verify that it works as it should. You are now ready to start making changes!

### Step 3: Branching
Create a new branch off of the `master` branch.
```sh
$ git checkout -b my-branch 
```

### Step 4: Code
##### Code style
We enforce the use of [pycodestyle](https://github.com/PyCQA/pycodestyle) to help us 
write cleaner and more cohesive code. You can read the list of 
[error codes](http://pycodestyle.pycqa.org/en/latest/intro.html#error-codes).

##### Testing
The testing is done with [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/), and 
the specified test rate for each component is 100%. If you for some reason want to reduce the 
test rate, this has to be argued for, and the reviewer will have to decide if it makes sense 
to lower the treshold. 

### Step 5: Commit
Add the changed files to a commit. _Note: package.lock files should not be included, as they
are updated in a dedicated pull request._

```sh
$ git add my/changed/files
$ git commit -m "Describing message about what you have done"
```
Please be specific when writing the pull request message. You can also tagg your message
with the issue you are solving by putting the issue number in a hashtag at the end
of the commit message. _Note: this __has__ to be at the end of the message, as everything 
else after the hashag gets escaped_

### Step 6: Ready pull request
##### Rebase
To prevent merge conflicts, it is a good idea to use ``git rebase`` to synchronize your work 
with main repository. 
```sh
$ git fetch upstream
$ git rebase upstream/master
```

##### Test and lint
Make sure that all tests are working. The linter will also cause the build to fail and 
make it unable to merge. 

From the main directorym run these:
```sh
$ make test
$ make lint
```

##### Push
When the commits are ready to go, and all the tests and linting has passed, you can
push your commits to your working branch at your fork. 
```sh
$ git push -u origin my-branch
```

### Step 7: Opening the pull request
When you have pushed your branch, this will be detected in the main repository. 
You can now go to the [Pull requests](https://github.com/Statoil/webviz/pulls) tab 
and open a new pull request. 

### Step 8: Review
Before your work can be included in the project it needs to be reviewed. You will probably get 
some feedback or change requests at this point. Don't be discouraged, this is an important 
part of the submission process! To make sure the project keeps its high standard, some key 
people from Equinor will have to sign of that the code is good to go. 

If you have made some new changes, simply repeat step 5 and 6 to update the pull request. 

When the pull request gets the green light, you are ready to merge your code. 
Please use the 'Squash and merge' alternative. 

__As a reviewer__ you can also suggest changes to a pull request. The pull requests
are open for everyone, but it takes a key role to make them available for merging. 
To check out a pull request locally, use this command:
```sh
$ git fetch upstream refs/pull/*PR_NUMBER*/head:*new branch name*
```
