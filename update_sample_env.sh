#!/bin/bash

# Find all .env files in the repository
find . -type f -name '.env' | while read ENV_FILE; do
  # Define the path for the corresponding sample.env file
  SAMPLE_ENV_FILE="\$(dirname "\$ENV_FILE")/sample.env"

  # Create or update the sample.env file
  awk -F '=' '/=/ { print $1 "=" }' "\$ENV_FILE" > "\$SAMPLE_ENV_FILE"

  echo "\$SAMPLE_ENV_FILE has been updated."
done
