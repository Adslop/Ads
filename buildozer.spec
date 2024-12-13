[app]
# (Mandatory) The title of your application.
title = ChessGod

# (Mandatory) The package name (unique identifier). It should be in reverse domain format (e.g., com.yourname.appname).
package.name = chessgod

# (Mandatory) The source directory. By default, this is the current directory (".").
source.dir = .

# (Mandatory) The version of your app.
version = 1.0

# (Optional) The version code (used for Android). Usually just the version number or increment this for updates.
version.code = 1

# (Optional) The requirements for your app, the modules that will be included.
requirements = python3, pillow, stockfish, android

# (Optional) Set the permissions needed by your app here.
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Optional) Set the Android API level (default is 30).
android.api = 30

# (Optional) Specify the minimum Android API level (default is 21).
android.minapi = 21

# (Optional) The target Android API level.
android.target = 30

# (Optional) The orientation of the app, e.g., landscape or portrait.
orientation = portrait

# (Optional) The architecture of the app (e.g., armeabi-v7a, arm64-v8a, x86).
android.arch = armeabi-v7a, arm64-v8a

# (Optional) Customize the launcher icon.
# android.icon = icon.png