#!/bin/sh
# keepMine.sh
# Keeps the local version of the file during a merge

# Arguments provided by Git:
# $1 = Base version of the file (from common ancestor)
# $2 = Current version of the file (local branch)
# $3 = Incoming version of the file (other branch)

# We simply copy our version over, ignoring all changes from the other branch
cp -f $2 $3
