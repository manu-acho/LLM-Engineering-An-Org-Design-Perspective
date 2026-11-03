# Run the learning reader locally

This is a setup guide for contributors and local readers. It is excluded from the reader's lesson library.

Double-click **Open Learning Guide.command** in the project folder. The launcher starts the reader and opens a browser at `http://127.0.0.1:4186`. Keep the terminal window running; Ctrl+C stops it. If this reader is already running on that port, the launcher opens the existing instance.

Alternatively, run the following from the project folder:

```sh
node browser-reader/scripts/server.mjs
```

Node.js must be installed. There are no packages to install. To use another port, prefix the command with `READER_PORT=4187`.

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
