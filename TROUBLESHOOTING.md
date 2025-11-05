# GitHub Pages 404 Troubleshooting

## Quick Fixes

### 1. Verify GitHub Pages is Enabled

Go to: https://github.com/hyperalz/AI_Governance/settings/pages

**Check:**
- ✅ Source is set to **Branch: `main`**
- ✅ Folder is set to **`/ (root)`**
- ✅ Click **Save** if you made changes

### 2. Check Repository Name Case Sensitivity

GitHub Pages URLs are case-sensitive. Your repository is `AI_Governance` (with underscore and capital letters).

**Correct URL:**
```
https://hyperalz.github.io/AI_Governance/
```

**If that doesn't work, try:**
- Wait 5-10 minutes after enabling Pages
- Check the Actions tab for build status
- Try accessing without trailing slash: `https://hyperalz.github.io/AI_Governance`

### 3. Verify Files Are in Root

Your `index.html` should be in the root directory (✅ it is).

### 4. Check Actions Tab

1. Go to: https://github.com/hyperalz/AI_Governance/actions
2. Look for "pages build and deployment" workflow
3. Check if it's running or completed
4. If there are errors, check the logs

### 5. Common Issues

**Issue: Pages not enabled**
- Solution: Enable in Settings → Pages

**Issue: Wrong branch selected**
- Solution: Make sure `main` branch is selected

**Issue: Build failed**
- Solution: Check Actions tab for errors

**Issue: Case sensitivity**
- Solution: Use exact repository name: `AI_Governance`

**Issue: Deployment in progress**
- Solution: Wait 5-10 minutes, then refresh

### 6. Alternative: Use GitHub Actions

If standard Pages doesn't work, we can set up a GitHub Actions workflow for deployment.

## Still Not Working?

1. **Check repository visibility:**
   - Repository must be public (or you need GitHub Pro for private repos)

2. **Verify the URL:**
   - Make sure you're using: `https://hyperalz.github.io/AI_Governance/`
   - Note the underscore and capital letters

3. **Wait longer:**
   - Sometimes takes 10-15 minutes for first deployment

4. **Check browser cache:**
   - Try incognito/private window
   - Hard refresh (Cmd+Shift+R or Ctrl+Shift+R)

