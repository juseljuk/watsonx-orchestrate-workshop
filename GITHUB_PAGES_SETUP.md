# GitHub Pages Setup Instructions

Your workshop repository is now configured for GitHub Pages with MkDocs Material! Follow these steps to enable and deploy your documentation site.

## What Has Been Set Up

✅ **MkDocs Configuration** ([`mkdocs.yml`](mkdocs.yml))
- Beautiful Material theme with dark/light mode
- Navigation structure matching your workshop parts
- Search functionality
- Code syntax highlighting
- Responsive design

✅ **GitHub Actions Workflow** ([`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml))
- Automatic deployment on push to main branch
- Builds and deploys to GitHub Pages
- No manual intervention needed

✅ **Documentation Structure** ([`docs/`](docs/))
- All workshop content copied to docs directory
- Custom landing page with overview
- All existing README files and resources preserved

✅ **Git Configuration** ([`.gitignore`](.gitignore))
- MkDocs build artifacts excluded from version control

## Your Existing Files Are Safe

**Important:** All your original files remain untouched in their original locations:
- ✅ `part1-setup/`, `part2-first-agent/`, etc. - All still there
- ✅ All `README.md` files - Unchanged
- ✅ All images and resources - Preserved
- ✅ Repository structure - Intact

The `docs/` directory contains **copies** of your content for the website. Your original files continue to work exactly as before.

## Enable GitHub Pages

### Step 1: Push Changes to GitHub

```bash
git add .
git commit -m "Add GitHub Pages with MkDocs Material"
git push origin main
```

### Step 2: Enable GitHub Pages in Repository Settings

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **Source**, select:
   - Source: **GitHub Actions**
5. Click **Save**

### Step 3: Wait for Deployment

1. Go to the **Actions** tab in your repository
2. You should see a workflow run called "Deploy MkDocs to GitHub Pages"
3. Wait for it to complete (usually 1-2 minutes)
4. Once complete, your site will be live!

## Access Your Documentation Site

Your documentation will be available at:

```
https://[your-username].github.io/bobchestrate-workshop/
```

Replace `[your-username]` with your GitHub username.

## Update the Site URL

After deployment, update the `site_url` in [`mkdocs.yml`](mkdocs.yml):

```yaml
site_url: https://[your-username].github.io/bobchestrate-workshop/
```

Also update the repository information:

```yaml
repo_name: bobchestrate-workshop
repo_url: https://github.com/[your-username]/bobchestrate-workshop
```

## Local Development

### Preview Locally

To preview your documentation site locally:

```bash
mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

### Build Locally

To build the site without serving:

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## Automatic Updates

Every time you push changes to the `main` branch:
1. GitHub Actions automatically rebuilds the site
2. Changes are deployed to GitHub Pages
3. Your documentation site updates within 1-2 minutes

## Customization

### Update Site Information

Edit [`mkdocs.yml`](mkdocs.yml) to customize:
- Site name and description
- Theme colors
- Navigation structure
- Features and plugins

### Add New Pages

1. Add markdown files to the `docs/` directory
2. Update the `nav` section in [`mkdocs.yml`](mkdocs.yml)
3. Commit and push changes

### Change Theme Colors

In [`mkdocs.yml`](mkdocs.yml), modify the `theme.palette` section:

```yaml
theme:
  palette:
    - scheme: default
      primary: indigo  # Change to: blue, red, green, etc.
      accent: indigo
```

## Troubleshooting

### Site Not Deploying

1. Check the **Actions** tab for error messages
2. Ensure GitHub Pages is enabled in Settings → Pages
3. Verify the workflow file is in `.github/workflows/deploy-docs.yml`

### Broken Links

- All links in the documentation should be relative
- Images should be in the `docs/` directory
- Check the build output for warnings about missing files

### Local Preview Not Working

Ensure MkDocs is installed:

```bash
python3 -m pip install mkdocs-material mkdocs-glightbox
```

## Benefits of This Setup

✅ **Professional Documentation** - Beautiful, searchable, mobile-friendly site
✅ **Zero Maintenance** - Automatic deployment on every push
✅ **Original Files Intact** - All your existing structure preserved
✅ **Easy Navigation** - Sidebar menu with all workshop parts
✅ **Search Functionality** - Find content quickly
✅ **Dark/Light Mode** - User preference support
✅ **Code Highlighting** - Syntax highlighting for all code examples

## Next Steps

1. Push the changes to GitHub
2. Enable GitHub Pages in repository settings
3. Wait for the first deployment
4. Share your documentation URL with workshop participants!

Your workshop content is now ready to be consumed as a beautiful, professional documentation site while maintaining all your original files and structure! 🎉