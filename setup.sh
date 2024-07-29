#!/bin/bash

# Create the update script
cat << 'EOF' > update_sample_env.sh
#!/bin/bash

# Function to create or update sample.env
create_sample_env() {
    local env_file="$1"
    local sample_file="${env_file%.env}.sample.env"

    if [ -f "$env_file" ]; then
        # Create sample.env by stripping values
        awk -F'=' '{print $1"="}' "$env_file" > "$sample_file"
    fi
}

# Find all .env files and create/update sample.env files
find . -name ".env" | while read -r env_file; do
    create_sample_env "$env_file"
done
EOF

# Make the update script executable
chmod +x update_sample_env.sh

# Add a pre-commit hook to run the update script
HOOKS_DIR=$(git rev-parse --show-toplevel)/.git/hooks
echo -e "#!/bin/bash\n./update_sample_env.sh" > "$HOOKS_DIR/pre-commit"
chmod +x "$HOOKS_DIR/pre-commit"

echo "Setup complete. The update_sample_env.sh script has been created and added as a pre-commit hook."
