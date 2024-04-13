# Getting Started with Git
## What is Git?
  Git is a version control system created by Linus Torvalds (the same guy behind Linux). Git provides programmers with a way to save code and look back on previous versions.
## Installing and Setting Up Git
  For the purposes of this guide, I'll limit the instructions for setting up Git to MacOS through the Terminal app, but it can be installed on any system.
  Ensure that Homebrew is installed and use the command below to install Git.
  ```
  brew install git
  ```
  Now, check that git is installed using the below command.
  ```
  git --version
  ```
  Next, set up the global variables necessary.
  ```
  git config --global user.name "<your git username>"
  git config --global user.email "<your email address>"
  ```
  To confirm these changes have been made, execute the below command.
  ```
  git config --list
  ```
## Cloning Our Repository
  Now, you have Git setup, but we want to clone[^1] our repository[^2]. We can do this by finding the URL for our repository (repo for short). The URL is available under the green "Code" button n the home screen of the repository. Copy this URL, we'll need it later!
  Next, open your terminal and run the following command.
  ```
  git clone <the URL you just copied>
  ```
  This will likely ask for some form of authentication, so make sure you know your password!
  Now that you have a local copy, you can edit the code as normal!
## Pushing
  The last main feature we want to use is the ability to modify code on our machine and have those changes visible to everyone else using the repo. We can achieve this using the `git push` command.
  Once you have made all the changes you want to, open your terminal and use the cd command to navigate into the directory that contains your local copy of the repository.
  ```
  cd <the path of the directory containing your git repo>
  ```
  Next, we have to add our changes.
  ```
  git add .
  ```
  We can confirm that git has recognized our changes by running the below.
  ```
  git status
  ```
  Now, we commit our changes. It's important that with every commit you provide a meaningful message explaining what was changed from the last version.
  ```
  git commit -m "<your commit message>"
  ```
  Finally, we make these changes available to everyone on the repo.
  ```
  git push origin main
  ```
## Pulling
  Sometimes, the repository will change and your local copy will be a version or two behind. We can fix this problem by using the `git pull` command. Keep in mind that this copy the repository as is, possibly overwriting your uncommitted changes.
  ```
  git pull origin main
  ```
## Final Notes
- I recommend pulling the repo every time you start working, and pushing your changes whenever you're done working.
- Git is a very complex system and has a number of features we won't use. Don't be discouraged if you sometimes see information that you don't understand or if an error message shows up!
- Because Git is so complex, if you run into any issues, let me know. Oftentimes resources like ChatGPT or other online resources may tell you to fix the error by running some command. **DO NOT** blindly copy and paste this, reach out to me and I will handle the issue.
  [^1]: Cloning refers to creating a local copy of a repository on your machine.
  [^2]: A repository is basically a folder - for example this repository is called `destin_programming`.
