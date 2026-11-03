#!/bin/zsh
cd "$(dirname "$0")" || exit 1
reader_port="${READER_PORT:-4186}"
reader_url="http://127.0.0.1:${reader_port}"
if curl --silent --fail --max-time 2 "${reader_url}/health" | /usr/bin/grep -q 'ai-engineering-learning-reader'; then
  open "$reader_url"
  exit 0
fi
if ! command -v node >/dev/null 2>&1; then
  print "Node.js is required to run the learning reader."
  read -r "reply?Press Return to close. "
  exit 1
fi
READER_PORT="$reader_port" node browser-reader/scripts/server.mjs &
reader_pid=$!
trap 'kill "$reader_pid" 2>/dev/null' EXIT INT TERM
for attempt in {1..30}; do
  if curl --silent --fail --max-time 1 "${reader_url}/health" | /usr/bin/grep -q 'ai-engineering-learning-reader'; then
    open "$reader_url"
    print "Keep this window running while reading. Ctrl+C stops the reader."
    wait "$reader_pid"
    exit $?
  fi
  if ! kill -0 "$reader_pid" 2>/dev/null; then
    print "The reader could not start. Check whether port ${reader_port} is in use."
    read -r "reply?Press Return to close. "
    exit 1
  fi
  sleep 1
done
print "The reader did not become ready. Check the messages above."
read -r "reply?Press Return to close. "
exit 1
