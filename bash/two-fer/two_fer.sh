#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.
main () {
    # -n True if length of string is non-zero
    if [[ -n $1 ]]; then
        echo "One for $1, one for me."
    else
        echo "One for you, one for me."
    fi
}
main "$@"