#!/bin/sh

ffmpeg -i %05d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p ready4gif.mp4
ffmpeg -i ready4gif.mp4 -vf fps=10,scale=320:-1:flags=lanczos,palettegen palette.png
ffmpeg -i ready4gif.mp4 -i palette.png -filter_complex "fps=10,scale=500:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
