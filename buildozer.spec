[app]

# 应用基础信息
title = Comic Reader
package.name = comicreader
package.domain = org.kivy
version = 1.0.0
source.dir = .

# 入口文件
source.main = main.py

# 包含的文件类型
source.include_exts = py,png,jpg,jpeg,webp,gif,kv,json,ttf

# 需求配置
requirements =
    python3==3.10,
    kivy==2.3.0,
    pillow==10.1.0,
    pyjnius==1.5.0,
    android

# 图标和启动画面
icon.filename = assets/icon.png
presplash.filename = assets/splash.png

# 安卓专用配置
android.permissions = 
    READ_EXTERNAL_STORAGE,
    WRITE_EXTERNAL_STORAGE,
    INTERNET

android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.arch = arm64-v8a

# 屏幕方向
orientation = portrait
fullscreen = 0

# 调试配置
log_level = 2
warn_on_root = 1
android.accept_sdk_license = true

# 构建优化
p4a.branch = develop
android.allow_backup = true
android.adaptive_icon_foreground = assets/icon_foreground.png
android.adaptive_icon_background = #FFFFFF

# 额外添加的文件
include_extras =
    assets/

# 排除不必要的文件
android.exclude_exts = .git,.md,.bat,.sh

# 签名配置（发布时需要）
# (注意：真实密钥不应放在版本控制中)
# android.release_keystore = /path/to/keystore
# android.release_storepassword = password
# android.release_keypassword = password
# android.release_keyalias = myalias

[buildozer]
log_level = 2