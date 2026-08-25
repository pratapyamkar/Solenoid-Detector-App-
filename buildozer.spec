[app]
title = Solenoid Detector
package.name = solenoiddetector
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_FINE_LOCATION
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
