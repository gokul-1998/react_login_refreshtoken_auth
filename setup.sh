#!/bin/bash

# Define the script name and the Git pre-commit hook path
UPDATE_SCRIPT="update_sample_env.sh"
PRE_COMMIT_HOOK=".git/hooks/pre-commit"

# Create the update_sample_env.sh script
cat << 'EOF' > $UPDATE_SCRIPT
#!/bin/bash

# Find all .env files in the repository
find . -type f -name '.env' | while read ENV_FILE; do
  # Define the path for the corresponding sample.env file
  SAMPLE_ENV_FILE="\$(dirname "\$ENV_FILE")/sample.env"

  # Create or update the sample.env file
  awk -F '=' '/=/ { print $1 "=" }' "\$ENV_FILE" > "\$SAMPLE_ENV_FILE"

  echo "\$SAMPLE_ENV_FILE has been updated."
done
EOF

# Make the update_sample_env.sh script executable
chmod +x $UPDATE_SCRIPT

# Check if the .git/hooks directory exists
if [ ! -d ".git/hooks" ]; then
  echo "No .git/hooks directory found. Make sure you're in a Git repository."
  exit 1
fi

# Create the pre-commit hook
cat << EOF > $PRE_COMMIT_HOOK
#!/bin/bash

# Run the update_sample_env.sh script before commit
./$UPDATE_SCRIPT
EOF

# Make the pre-commit hook executable
chmod +x $PRE_COMMIT_HOOK

echo "Setup complete. The update_sample_env.sh script will run before each commit."
