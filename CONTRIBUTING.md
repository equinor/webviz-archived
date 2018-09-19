#Contributing to Webviz
The following is a set of guidelines for contributing to Webviz. Use your best
judgement at feel free to propose changes to this document in a pull request.

#Issues
Issues are created [here](https://github.com/Statoil/webviz/issues/new).

When creating a new issue, please use this format when explaining your problem:
* Expected behavior
* Actual behavior
* How to reproduce

#Pull Requests


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
$ git checkout -b branch-name 
```

### Step 4: Code
[Code style]()

[Testing requirements]()

### 5: Commit
Add the changed files to a commit. _Note: package.lock files should not be included, as they
are updated in pull requests dedicated to this._

```sh
$ git add my/changed/files
$ git commit -m "Describing message about what you have done"
```

## Style Guide