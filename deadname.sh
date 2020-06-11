#!/bin/sh

git filter-branch --env-filter '
OLD_EMAIL="ashrlmthsn@Gmail.com"
CORRECT_NAME="Emlyn Matheson"
CORRECT_EMAIL="emlynmatheson@Gmail.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

git push --force --tags origin HEAD:master
git update-ref -d refs/original/refs/heads/master
