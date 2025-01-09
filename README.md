# Python Image Steganography Project
This project implements a simple image steganography technique using Python. It allows you to hide a text message within the least significant bits (LSB) of an image and extract it later. The project utilizes popular libraries such as Pillow (PIL), NumPy, Matplotlib, and tqdm.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Hide a text message within an image.
- Extract the hidden message from the modified image.
- Visualize the original and modified images.
- Progress tracking during the hiding process using a progress bar.

## Requirements

Make sure you have Python 3.x installed on your machine. You will also need the following libraries :

- Pillow (PIL) :  For image processing and manipulation.
- NumPy : For numerical operations and handling image data as arrays.
- Matplotlib : For displaying images and visualizing results.
- tqdm : For creating progress bars in loops.

## Installation

You can install the required libraries using pip. Run the following command in your terminal :
``` pip install pillow numpy matplotlib tqdm ```

## Usage

1. **Clone the Repository** (if applicable)
   
2. **Run the script** :
   Open a terminal and navigate to the directory containing `main.py`. Use the following command to execute the script :
   ```python main.py```

3. **Input Image Path** :
When prompted, enter the path to a grayscale image where you want to hide your message.

4. **Enter Message** :
After selecting an image, you will be prompted to enter the text you want to hide in the image.

5. **View Results** :
The modified image will be displayed, and the hidden message will be extracted and printed to the terminal.

## Example

Here’s an example of how to use the program:

1. Enter the path of an image (e.g., `demo_image.jpg`).
2. Enter a message (e.g., "Hello, this is a secret message!").

The program will modify the image by hiding your message and then display both the original and modified images.

## Notes

- Ensure that your input image is in grayscale format for best results.
- The hidden message is terminated with a marker `[Yum]`, which is used to identify where the message ends during extraction.
- If there are not enough pixels in the image to store the entire message, an error message will be displayed.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


