token="$(cat ./token.txt)"

curl -sX GET \
-H "Authorization: Bearer $token" \
-H "Accept: application/vnd.github.machine-man-preview+json" \
"$1" | jq