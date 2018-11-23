# producesort

A tool for determining if produce is rotten based on image recognition. Uses Gaussian smoothing and Canny edge detection to create the masks, and the difference of Gaussian method to isolate blobs, with scikit-image's modules.
![screenshot](https://i.imgur.com/gQ01WgY.png)
![screenshot](https://i.imgur.com/85epnld.png)
![screenshot](https://i.imgur.com/Cc0BA6H.png)
![screenshot](https://i.imgur.com/npTPwk1.png)
![screenshot](https://i.imgur.com/NFF2wIb.png)

## Dependencies

Use `python3 -m pip install --user -r req.txt` to install the necessary dependencies.

## Getting started

Download the repo with `git clone https://github.com/idoneam/producesort/`. Navigate into the directory and load your images into the `img` directory. Run `python3 Main.py` and select the fruit image for analysis. For demonstration purposes, the application will display the input image, the edge mask, the input image with its background subtracted, and blemishes on the input image found by the blob detection algorithm.

Developed by Marie Payne and Johanan Idicula.
