from PIL import Image

def image_to_ascii(image_path, save_path, scale):
    scale = int(scale)

    # Open the image
    with Image.open(image_path) as img:
        # Resize the image
        w, h = img.size
        resized_img = img.resize((w // scale, h // scale))
        
        # Define the character set based on pixel intensity
        intensity_to_char = {
            range(0): '#',
            range(1, 50): '@',
            range(50, 100): 'X',
            range(100, 150): 'H',
            range(150, 200): '%',
            range(200, 250): '&',
            range(250, 300): '8',
            range(300, 350): 'W',
            range(350, 400): '*',
            range(400, 450): 'o',
            range(450, 500): ':',
            range(500, 550): ';',
            range(550, 600): ',',
            range(600, 650): '"',
            range(650, 700): '`',
            range(700, 725): '.',
            range(725, 750): "'",
            range(750, 256 * 3): ' ' # in RGB model each color has range from 0 to 255, so the sum of colors can go from 0 to 765
        }

        # Convert the image to ASCII art
        ascii_art = []
        
        # we resize the image because if we used the original image, the ascii text would be way too long and we couldn't even visualize it
        pixels = resized_img.load()
        for y in range(resized_img.height):
            row = []
            for x in range(resized_img.width):
                intensity = sum(pixels[x, y])
                char = ' '  # Default character (space)

                # dictionary lookups are faster than if else checks lol
                for intensity_range, char_value in intensity_to_char.items():
                    if intensity in intensity_range:
                        char = char_value
                        break

                row.append(char)
            ascii_art.append(''.join(row))

    # Save the ASCII art to file
    with open(save_path, 'w') as f:
        f.write('\n'.join(ascii_art))

if __name__ == "__main__":
    image_to_ascii("photo.jpg", "photo_ascii.txt", "5")
