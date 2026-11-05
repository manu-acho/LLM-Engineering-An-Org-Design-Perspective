#!/bin/zsh
cd "$(dirname "$0")" || exit 1
reader_port="${READER_PORT:-4191}"
reader_url="http://127.0.0.1:${reader_port}"
if curl --noproxy '*' --silent --fail --max-time 2 "${reader_url}/health" | /usr/bin/grep -q 'ai-standalone-learning-reader'; then
  open "$reader_url"
  exit 0
fi
if ! command -v node >/dev/null 2>&1; then
  print "Node.js is required to run the learning reader."
  read -r "reply?Press Return to close. "
  exit 1
fi
print "Keep this terminal open while reading. Ctrl+C stops the reader."
READER_PORT="$reader_port" node browser-reader/scripts/server.mjs
