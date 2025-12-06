[app]
title = Calculator
package.name = calculator
package.domain = org.calculator
source.dir = .
version = 1.0
requirements = python3,kivy
permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
