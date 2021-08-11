#!/bin/bash -e
# description: Script to create sym links of background images to use with wallpapers
# license: MIT.

# Declare an array for background types
declare -a bgtypes=("dark" "light" "abstract-dark" "abstract-light")
# Declare an array for background sizes
declare -a sizes=("1800x1440.jpg" "2048x1536.jpg" "2560x1080.jpg" "2560x1440.jpg" "2560x1600.jpg" "3440x1440.jpg")
## Loop through the above array(s) types and sizes to create links and metadata
for bg in "${bgtypes[@]}"
do
    echo "Processing 'Alma-"$bg"' background"
    # Remove any old folders and create new structure
    rm -rf /usr/share/wallpapers/Alma-$bg*
    mkdir -p /usr/share/wallpapers/Alma-$bg/contents/images/
    # creae sym link for all sizes
    for size in "${sizes[@]}"
    do
    ln -s /usr/share/backgrounds/Alma-$bg-$size /usr/share/wallpapers/Alma-$bg/contents/images/$size
    done
    # Create metadata file to make Desktop Wallpaper application happy
    # Move this to pre-created files in repo to give support to other languages
    # This is quick hack for time being.
    cat > /usr/share/wallpapers/Alma-$bg/metadata.desktop <<FOE
[Desktop Entry]
Name=AlmaLinux $bg

X-KDE-PluginInfo-Name=Alma-$bg
X-KDE-PluginInfo-Author=Bala Raman
X-KDE-PluginInfo-Email=srbala@gmail.com
X-KDE-PluginInfo-License=MIT
FOE
done
