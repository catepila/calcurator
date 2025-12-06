[app]
title = Calculator
package.name = calculator
package.domain = com.calculator
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

[buildozer]
log_level = 2
warn_on_root = 1
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.skip_update = False

[app:android]
requirements = python3,kivy
android.orientation = portrait
android.allow_backup = True
