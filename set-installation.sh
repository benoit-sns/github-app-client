jwt="$(cat ./jwt.txt)"

curl -sX POST \
-H "Authorization: Bearer $jwt" \
-H "Accept: application/vnd.github.machine-man-preview+json" \
"https://api.github.com/app/installations/$1/access_jwts" | jq -r .token > token.txt