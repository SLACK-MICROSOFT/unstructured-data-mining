cat results.txt | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | sort -u
