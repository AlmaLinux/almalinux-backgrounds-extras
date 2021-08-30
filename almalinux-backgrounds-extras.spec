%global codename sphericalcow
# Package is only arch specific due to missing deps on arm
# Debuginfo package is useless.
%global debug_package %{nil}

Name:       almalinux-backgrounds-extras
Version:    84.0
Release:    1%{?dist}
Summary:    AlmaLinux-related desktop backgrounds for KDE and XFCE
BuildArch:  noarch

#Group:      System Environment/Base
URL:        http://www.almalinux.org
Source0:    alma-dark-metadata.desktop
Source1:    alma-light-metadata.desktop
Source2:    alma-abstract-dark-metadata.desktop
Source3:    alma-abstract-light-metadata.desktop
License:    MIT

Requires: almalinux-backgrounds
Requires: coreutils
Conflicts: desktop-backgrounds-compat
Provides: desktop-backgrounds-compat

%description
AlmaLinux-related desktop backgrounds for KDE and XFCE


%prep

%build

%install
# Declare an array for background types
declare -a bgtypes=("dark" "light" "abstract-dark" "abstract-light")
# Declare an array for background sizes
declare -a sizes=("1800x1440.jpg" "2048x1536.jpg" "2560x1080.jpg" "2560x1440.jpg" "2560x1600.jpg" "3440x1440.jpg")
# kde
## Loop through the above array(s) types and sizes to create links and metadata
for bg in "${bgtypes[@]}"
do
    # Remove any old folders and create new structure
    rm -rf /usr/share/wallpapers/Alma-$bg*
    mkdir -p %{buildroot}/usr/share/wallpapers/Alma-$bg/contents/images/
    # create sym link for all sizes
    for size in "${sizes[@]}"
    do
        ln -sf /usr/share/backgrounds/Alma-$bg-$size %{buildroot}/usr/share/wallpapers/Alma-$bg/contents/images/$size
    done
done
install -p -m 644 %{SOURCE0} %{buildroot}/usr/share/wallpapers/Alma-dark/metadata.desktop
install -p -m 644 %{SOURCE1} %{buildroot}/usr/share/wallpapers/Alma-light/metadata.desktop
install -p -m 644 %{SOURCE2} %{buildroot}/usr/share/wallpapers/Alma-abstract-dark/metadata.desktop
install -p -m 644 %{SOURCE3} %{buildroot}/usr/share/wallpapers/Alma-abstract-light/metadata.desktop

# xfce
mkdir -p %{buildroot}/usr/share/backgrounds/images
ln -s /usr/share/backgrounds/Alma-dark-2048x1536.jpg %{buildroot}/usr/share/backgrounds/images/default.png

%post


%postun

%posttrans


%files
/usr/share/wallpapers/Alma-abstract-dark
/usr/share/wallpapers/Alma-abstract-dark/contents
/usr/share/wallpapers/Alma-abstract-dark/contents/images
/usr/share/wallpapers/Alma-abstract-dark/contents/images/1800x1440.jpg
/usr/share/wallpapers/Alma-abstract-dark/contents/images/2048x1536.jpg
/usr/share/wallpapers/Alma-abstract-dark/contents/images/2560x1080.jpg
/usr/share/wallpapers/Alma-abstract-dark/contents/images/2560x1440.jpg
/usr/share/wallpapers/Alma-abstract-dark/contents/images/2560x1600.jpg
/usr/share/wallpapers/Alma-abstract-dark/contents/images/3440x1440.jpg
/usr/share/wallpapers/Alma-abstract-dark/metadata.desktop
/usr/share/wallpapers/Alma-abstract-light
/usr/share/wallpapers/Alma-abstract-light/contents
/usr/share/wallpapers/Alma-abstract-light/contents/images
/usr/share/wallpapers/Alma-abstract-light/contents/images/1800x1440.jpg
/usr/share/wallpapers/Alma-abstract-light/contents/images/2048x1536.jpg
/usr/share/wallpapers/Alma-abstract-light/contents/images/2560x1080.jpg
/usr/share/wallpapers/Alma-abstract-light/contents/images/2560x1440.jpg
/usr/share/wallpapers/Alma-abstract-light/contents/images/2560x1600.jpg
/usr/share/wallpapers/Alma-abstract-light/contents/images/3440x1440.jpg
/usr/share/wallpapers/Alma-abstract-light/metadata.desktop
/usr/share/wallpapers/Alma-dark
/usr/share/wallpapers/Alma-dark/contents
/usr/share/wallpapers/Alma-dark/contents/images
/usr/share/wallpapers/Alma-dark/contents/images/1800x1440.jpg
/usr/share/wallpapers/Alma-dark/contents/images/2048x1536.jpg
/usr/share/wallpapers/Alma-dark/contents/images/2560x1080.jpg
/usr/share/wallpapers/Alma-dark/contents/images/2560x1440.jpg
/usr/share/wallpapers/Alma-dark/contents/images/2560x1600.jpg
/usr/share/wallpapers/Alma-dark/contents/images/3440x1440.jpg
/usr/share/wallpapers/Alma-dark/metadata.desktop
/usr/share/wallpapers/Alma-light
/usr/share/wallpapers/Alma-light/contents
/usr/share/wallpapers/Alma-light/contents/images
/usr/share/wallpapers/Alma-light/contents/images/1800x1440.jpg
/usr/share/wallpapers/Alma-light/contents/images/2048x1536.jpg
/usr/share/wallpapers/Alma-light/contents/images/2560x1080.jpg
/usr/share/wallpapers/Alma-light/contents/images/2560x1440.jpg
/usr/share/wallpapers/Alma-light/contents/images/2560x1600.jpg
/usr/share/wallpapers/Alma-light/contents/images/3440x1440.jpg
/usr/share/wallpapers/Alma-light/metadata.desktop
/usr/share/backgrounds/images/default.png

#%license COPYING


%changelog
* Tue Aug 24 2021 Jonathan Wright <jonathan@effecthost.com> - 84.0-1
- package created
