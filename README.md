# Downloader

This is a very simple GUI app for learning how to packaging things with flatpak.

This app:

- uses PyQt5
- includes a custom python module
- has pip dependencies
- has static resources

To build the flatpak package:

```
flatpak-builder build-dir com.micahflee.Downloader.json --force-clean
```

To test the build:

```
flatpak-builder --run build-dir com.micahflee.Downloader.json downloader
```

To get a shell in the sandbox:

```
flatpak-builder --run build-dir com.micahflee.Downloader.json /bin/bash
```
