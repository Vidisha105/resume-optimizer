# Pushing to GitHub - Step by Step

## Option 1: Using GitHub CLI (Easiest)

1. **Install GitHub CLI** (if not already installed)
   - macOS: `brew install gh`
   - Windows: Download from https://cli.github.com
   - Linux: See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

2. **Authenticate**
   ```bash
   gh auth login
   ```

3. **Create and Push Repository**
   ```bash
   cd resume-optimizer
   git init
   git add .
   git commit -m "Initial commit: Resume optimizer agent"
   gh repo create resume-optimizer --public --source=. --push
   ```

## Option 2: Using Git + GitHub Website

1. **Create Repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `resume-optimizer`
   - Description: "AI-powered resume optimization tool"
   - Choose Public or Private
   - **Don't** initialize with README (we already have one)
   - Click "Create repository"

2. **Push Your Code**
   ```bash
   cd resume-optimizer
   git init
   git add .
   git commit -m "Initial commit: Resume optimizer agent"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/resume-optimizer.git
   git push -u origin main
   ```

   Replace `YOUR_USERNAME` with your actual GitHub username.

## Option 3: Using SSH (For Regular Git Users)

1. **Set up SSH key** (if not already done)
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   cat ~/.ssh/id_ed25519.pub
   # Add this key to GitHub: Settings > SSH and GPG keys
   ```

2. **Create repo on GitHub** (see Option 2, step 1)

3. **Push with SSH**
   ```bash
   cd resume-optimizer
   git init
   git add .
   git commit -m "Initial commit: Resume optimizer agent"
   git branch -M main
   git remote add origin git@github.com:YOUR_USERNAME/resume-optimizer.git
   git push -u origin main
   ```

## Verify Your Repository

After pushing, visit:
```
https://github.com/YOUR_USERNAME/resume-optimizer
```

You should see:
- ✅ README.md displayed on the main page
- ✅ All your files listed
- ✅ Green "Code" button for cloning

## Customizing Your Repository

### Add Topics (Tags)
On GitHub, click the gear icon next to "About" and add topics:
- `resume`
- `ai`
- `python`
- `claude`
- `job-search`
- `career`

### Add a Description
Click the gear icon next to "About" and add:
"AI-powered tool for optimizing resumes based on job descriptions using Claude AI"

### Create a Release
After testing your code:
```bash
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

## Security Reminder ⚠️

**Never commit your API key!**

The `.gitignore` file already excludes:
- `.env` files
- `.txt` files (your resumes)
- Personal documents

Always double-check before committing:
```bash
git status  # Check what will be committed
```

## Updating Your Repository

After making changes:
```bash
git add .
git commit -m "Description of your changes"
git push
```

## Making it Private Later

If you want to make it private:
1. Go to repository Settings
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Make private"

---

Need help? Check the [GitHub Docs](https://docs.github.com) or open an issue!
