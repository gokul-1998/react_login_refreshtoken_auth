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
