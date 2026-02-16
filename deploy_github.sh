#!/bin/bash
# Deploy to GitHub - Run this on your local machine

cd /home/node/.openclaw/workspace

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git..."
    git init
    git remote add origin https://github.com/ReneTeacher/Coding-Projects.git
fi

echo "Enter your GitHub credentials when prompted:"
git push -u origin master
