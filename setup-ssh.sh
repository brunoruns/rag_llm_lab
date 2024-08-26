#!/bin/bash

# Generate SSH key pair if it doesn't exist
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -C "bruno.herman@gmail.com" -f ~/.ssh/id_ed25519 -N ""
fi

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add the SSH private key to the SSH agent
ssh-add ~/.ssh/id_ed25519

# Display the public key
echo "Your SSH public key is:"
cat ~/.ssh/id_ed25519.pub
echo "Please add this key to your GitHub account."

# add safe account
git config --global --add safe.directory /workspaces/rag_llm_lab