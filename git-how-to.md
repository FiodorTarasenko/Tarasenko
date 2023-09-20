# Creating an SSH key:
## In Git on local server:
ssh-keygen -t ed25519 -C "email"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub

# Adding to GitHub:
Create new SSH key -> enter value of id_ed25519.pub

# Clone repository:
git clone <repository-link>
