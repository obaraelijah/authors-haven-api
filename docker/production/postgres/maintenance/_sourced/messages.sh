#!/usr/bin/env bash

# This script defines functions for displaying messages with different colors and styles.
# Each function is designed to print a specific type of message.
# Usage example:
# message_success "Operation completed successfully!"
# message_warning "This is a warning!"
# message_error "An error occurred!"
# message_info "Here's some information."
#ANSI escape codes

# A function to print an empty line (newline).
message_newline(){
  echo
}

# A function to print a debug message in blue.
message_debug(){
  echo -e "DEBUG: ${@}"
}

# A function to print a welcome message in bold.
message_welcome(){
  echo -e "\e[1m${@}\e[0m"
}

# A function to print a warning message in yellow.
message_warning(){
  echo -e "\e[33mWARNING\e[0m: ${@}" 
}

# A function to print an error message in red.
message_error(){
  echo -e "\e[31mERROR\e[0m: ${@}"
}

# A function to print an information message in white.
message_info(){
  echo -e "\e[37mINFO\e[0m: ${@}"
}

# A function to print a suggestion message in yellow.
message_suggestion(){
  echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

# A function to print a success message in green.
message_success(){
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}
