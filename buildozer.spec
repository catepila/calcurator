[app]
title = Calculator
package.name = calculator
package.domain = com.calculator
source.dir = .
version = 1.0.0

[buildozer]
log_level = 2
warn_on_root = 1
android.skip_update = True
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.ndk = 23b
android.permissions = INTERNET
android.features =

[app:android]
requirements = python3,kivy
android.orientation = portrait
p4a.bootstrap = sdl2
p4a.source_dir = 
android.gradle_dependencies =
