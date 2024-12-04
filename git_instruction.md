# Instructions for Setting Up and Using Git with PyCharm

Welcome! Follow these steps to set up Git in PyCharm, register on GitHub, and manage updates to this repository.

---

## Prerequisites

- **PyCharm**: Installed on your computer.
- **Git**: Installed and configured. Download it from [git-scm.com](https://git-scm.com/) if not installed.
- **GitHub Account**: Sign up for a free account at [GitHub](https://github.com/).

---

## Step 1: Register and Connect GitHub to PyCharm

1. **Create a GitHub Account**:
   - Visit [GitHub](https://github.com/) and sign up if you haven’t already.

2. **Link GitHub to PyCharm**:
   - Go to `File > Settings > Version Control > GitHub`.
   - Click the "+" to add an account.
   - Log in using your GitHub credentials.

---

## Step 2: Set Up Git in PyCharm

1. **Configure Git Executable**:
   - Open PyCharm.
   - Go to `File > Settings` (on macOS: `PyCharm > Preferences`).
   - Navigate to `Version Control > Git`.
   - Set the "Path to Git executable" (e.g., `/usr/bin/git` or `C:\Program Files\Git\bin\git.exe`).
   - Click "Test" to ensure Git is properly configured.

2. **Clone the Repository**:
   - Go to `File > New > Project from Version Control`.
   - Paste the repository URL (e.g., https://github.com/PDDMain/SergeyPractices.git).
   - Choose a directory to clone the project and click "Clone".

---

## Step 3: Workflow for Updating Repository and Adding Solutions

### 1. Pull the Latest Changes
   - In PyCharm, go to `VCS > Git > Pull`.
   - Ensure your local repository is up-to-date.

### 2. Create a New Branch
   - Go to `VCS > Git > Branches`.
   - Click `New Branch`.
   - Name the branch (e.g., `solution-lesson1`) and ensure "Checkout branch" is selected.

### 3. Add Your Solution
   - Write your solution code in the appropriate files or folders.
   - Save your work in PyCharm.

### 4. Commit Your Changes
   - Go to `VCS > Commit`.
   - Review the changes you made.
   - Add a meaningful commit message (e.g., "Added solution for Lesson 1").
   - Click `Commit` (or `Commit and Push`).

### 5. Push the Branch to GitHub
   - If you didn’t push during the commit step, go to `VCS > Git > Push`.
   - Ensure the correct branch is selected.
   - Click "Push".

### 6. Create a Pull Request
   - Go to your GitHub repository in a browser.
   - Switch to your branch (e.g., `solution-lesson1`).
   - Click "Pull Request" > "New Pull Request".
   - Add a title and description for your pull request.
   - Assign the pull request to me so I can review it.

---

## Step 4: Review and Feedback

- I will review your pull request.
- If changes are needed, you’ll receive comments in the pull request.
- After approval, I will merge the changes into the main branch.

---

Feel free to reach out if you face any issues! Happy coding!
