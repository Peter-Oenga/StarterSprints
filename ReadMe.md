# 📱 Android Image Slider Home-Screen Widget

## Project Overview

This project is a modern Android **home-screen widget** that displays a rotating image slider.  
The widget dynamically fetches images from a remote website so that the content can be updated remotely without modifying or reinstalling the Android app.

The project was rebuilt from scratch to replace a deprecated legacy Android widget originally built for very old Android versions.

---

## Key Features

✅ Home-screen widget (not just an in-app component)  
✅ Automatic image slideshow  
✅ Left and right navigation buttons  
✅ Loads images dynamically from a live website  
✅ Remote content management via website API  
✅ Supports modern Android versions  
✅ Built in Java using Android Studio

---

## Architecture Summary

The system is composed of **two main parts**:

### 1. Android Widget

- Displays the image slider on the home screen
- Fetches image URLs from a JSON API
- Caches images locally on the device
- Uses WorkManager for background downloads
- Uses AlarmManager to auto-rotate images

### 2. Web-Based Admin System

- Runs on a website server
- Stores uploaded images
- Provides a JSON API that returns image URLs
- Allows client to change content without app updates

---

## Project Folder Structure


---
```text
WidgetImageSlider/
 └── app/
     └── src/
         └── main/
             ├── java/com/example/widgetimageslider/
             │   ├── ImageSliderWidget.java
             │   └── ImageDownloadWorker.java
             ├── res/layout/
             │   └── image_slider_widget.xml
             ├── res/xml/
             │   └── image_slider_widget_info.xml
             └── AndroidManifest.xml
```
## Requirements to Run

### System Requirements

- Windows OS
- Android Studio installed
- Physical Android phone or emulator

### Android Requirements

- Minimum Supported: Android 5.0+
- Target SDK: Modern Android versions

---

## How the Image System Works

1. Client uploads images through the website dashboard
2. Images are stored on the server
3. API returns JSON with image URLs
4. The Android widget reads the API
5. The widget downloads images
6. The widget displays them on the home screen

Example API response:

```json
[
  {
    "id": "1",
    "file_name": "https://euafroawards.com/assets/user_data/test.jpg",
    "uploaded_at": "2025-11-23 00:45:30"
  }
]
