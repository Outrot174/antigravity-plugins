---
name: ffmpeg-media-craft
description: Process, transcode, compress, slice, and extract audio/video/GIFs using native FFmpeg and FFprobe. Use when editing video files, converting media formats, extracting audio, generating thumbnails, or creating optimized animations.
tools: Read, Glob, Grep, Bash
---

# FFmpeg Media Craft (AGY v2)

Native media processing engine powered by `$PREFIX/bin/ffmpeg` and `$PREFIX/bin/ffprobe`.

## Storage Isolation Standard
All output video files must strictly be written to:
`/storage/emulated/0/Antigravity/видео/`
All extracted frames, GIFs, and images must strictly be written to:
`/storage/emulated/0/Antigravity/изображения/`

---

## Common Media Operations

### 1. Media Inspection (FFprobe)
```bash
# Get resolution, codec, duration, and bitrate as clean JSON
ffprobe -v quiet -print_format json -show_format -show_streams "input.mp4"
```

### 2. Video Compression & Optimization
Balanced H.264 compression for high quality and small file size:
```bash
ffmpeg -i "input.mp4" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart "/storage/emulated/0/Antigravity/видео/compressed.mp4"
```

### 3. High-Quality Palette-Optimized GIF
Generate high-fidelity GIFs without color banding:
```bash
ffmpeg -i "input.mp4" -vf "fps=15,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 "/storage/emulated/0/Antigravity/изображения/animation.gif"
```

### 4. Fast Slicing / Trimming (Zero Re-encoding)
Instant cut using keyframe-accurate stream copying:
```bash
# Cut from 00:00:10 for 30 seconds
ffmpeg -ss 00:00:10 -i "input.mp4" -t 30 -c copy "/storage/emulated/0/Antigravity/видео/clip.mp4"
```

### 5. Audio Extraction
```bash
# Extract audio stream directly
ffmpeg -i "input.mp4" -vn -c:a copy "/storage/emulated/0/Antigravity/видео/audio.aac"

# Convert to MP3
ffmpeg -i "input.mp4" -vn -c:a libmp3lame -q:a 2 "/storage/emulated/0/Antigravity/видео/audio.mp3"
```

### 6. Keyframe & Thumbnail Extraction
```bash
# Extract single frame at 5 seconds
ffmpeg -ss 00:00:05 -i "input.mp4" -vframes 1 -q:v 2 "/storage/emulated/0/Antigravity/изображения/thumbnail.jpg"

# Extract 1 frame every 10 seconds
ffmpeg -i "input.mp4" -vf "fps=1/10" "/storage/emulated/0/Antigravity/изображения/frame_%04d.jpg"
```
