from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tqdm

# function for hiding data by changing the least significant bit of each pixels intensity.
def encryption(img, message) :
    # adding a marker to the end of message
    message += "[Yum]"

    # converting the message to a byte object
    message = message.encode("ascii")

    # converting each character of message in its 8-bit binary format 
    message_bits = ''.join(([format(i, '08b') for i in message]))

    # converting to one-dimensional array
    img = img.flatten()

    # checking if the image has enough pixels to store the message
    if len(message_bits) > len(img) :
        print("Not enough pixels in image to hide the message.")
        return
    print()
        
    # modifying last bits of image to store hidden message
    for index in tqdm.tqdm(range(len(message_bits)), desc = "Hiding data...") :
        # storing intensity value of each pixel in binary format
        val = img[index]
        val = bin(val)

        # slicing least significant bit and binary format('0b') from pixel value
        val = val[2:9]
        new_val = val + message_bits[index]


        # Ensure new_val is within bounds
        if int(new_val,2) < 0 or int(new_val,2) > 255:
            print(f"Warning: Value out of bounds for pixel at index {index}: {new_val}")
            break

        img[index] = int(new_val, 2)

    # reshaping the flatten array into its original dimensions 
    img = img.reshape((A,B))
    modified_image = img

    # displaying the modified image
    plt.imshow(modified_image, cmap="gray")
    plt.axis('off')
    plt.title('Modified image')
    plt.show()

    return modified_image

# function to extract hidden message from modified image
def message_extraction(img) :
    # variable to store extracted message
    msg = ""
    index = 0
    img = img.flatten()

    # looping over until end marker is hit
    while msg[-5:] != "[Yum]" :
        # checking for bounds before extraction
        if index > img.shape[0]-8 :
            print("No hidden message.")
            break

        # extracting the least significant bit(last bit) for each next 8 pixel values
        extracted_bits = [bin(i)[-1] for i in img[index:index+8]]

        bits_str = "".join(extracted_bits)

        msg += chr(int(bits_str, 2))

        # incrementing index by 8 for next set of bits
        index +=8

    # returning the extracted message(without end marker)
    return msg[:-5]

# input image path from user
image_path = input("Enter the path of image to hide data in : ")

# opens the image in grayscale and creates an array of each pixels intensity as a single value(0 for black and 255 for white).
try:
    original_img = np.array(Image.open(image_path).convert("L"))
except Exception as e:
    print(f"Error opening image : {e}")
    exit()


# to show the image
plt.imshow(original_img, cmap="gray")
plt.axis("off")
plt.title('Original image')
plt.show()

# to get dimensions of image
A, B = original_img.shape

# taking input from user
message = input("Enter the text to hide :\n")

modified_img = encryption(original_img, message)
extracted_msg = message_extraction(modified_img)

# display extracted message
print("\nExtracted hidden message -\n", extracted_msg)