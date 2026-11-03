# Run the learning reader locally

This is a setup guide for contributors and local readers. It is excluded from the reader's lesson library.

Run these commands in Terminal:

```sh
cd "/Users/manu/Documents/ChatGPT/LLM Engineering"
node browser-reader/scripts/server.mjs
```

The reader stays in the foreground. Keep that Terminal window open while reading; press Ctrl+C to stop it. Closing the chat does not stop a server you started yourself in Terminal.

On this Mac, open `http://127.0.0.1:4186`. Other devices on the same network can use the **Network reader** address printed at startup. You can also double-click **Open Learning Guide.command** to run the same foreground server in a terminal window.

Node.js must be installed. There are no packages to install. To use another port, prefix the server command with `READER_PORT=4187`.

## Read and refresh

The reader provides module navigation, full-text search, page outlines, bookmarks, progress, private browser notes and printing. Use Menu and Search on narrow screens, or press `/` to focus search on a wider screen. Read and Save controls are manual; opening a lesson does not mark it complete.

Edit lesson Markdown and refresh the browser to see changes. The server rebuilds the content index when requested. Code examples are displayed for reading and are never executed by the reader.

The library contains only the files listed in the builder. Authoring notes, local inventories and maintenance instructions are excluded. Course notebook and literature links open on GitHub, using recorded revisions. The reader does not require either source repository to be cloned locally.

## Notes and privacy

Progress, bookmarks and notes stay in this browser's local storage. They are not written to the Markdown or sent to the source repositories. Changing browser, hostname or port gives a separate storage location; clearing browser storage removes the saved state. Existing saved state from the earlier reader name remains readable.

The server accepts IPv4 connections on this Mac, including from other devices on the same network. It serves only the reader's fixed asset list and generated learning collection. Private instructor files and the wider project folders are not served. The generated `browser-reader/dist/` folder is ignored by Git. Build the static reading collection with `node browser-reader/scripts/build.mjs`.

## Open on another device

Connect the other device to the same local network, then open the **Network reader** address printed when the server starts. Keep this Mac awake and the server running. The address may change when this Mac reconnects to the network.

The launcher and normal start command both enable network reading. To restrict a later session to this Mac only, start with:

```sh
READER_HOST=127.0.0.1 node browser-reader/scripts/server.mjs
```

Notes, bookmarks and progress remain separate in each browser; they do not sync between devices.

## Why Node rather than Python?

The Node server rebuilds the reading collection when the browser refreshes. Python's simple HTTP server only serves files that have already been generated. Both can serve a static site, but the Node reader keeps the preview current as lessons are edited.

No background service or automatic launch at login is installed. Start and stop the server in Terminal, as with a Python HTTP server.
