import cv2
import numpy as np

image_path = ("path/to/image")

def process_image(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=30)

    return circles

def detect_spine_pins(image_path):
    circles = process_image(image_path)

    if circles is not None:
        pins_coordinates = []
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            x, y, _ = i
            pins_coordinates.append((x, y))
            # Uncomment the following lines if you want to draw circles on the detected pins and display the image
            # cv2.circle(img, (x, y), 2, (0, 0, 255), 3)
            # cv2.circle(img, (x, y), 2, (255, 0, 0), -1)
        
        return pins_coordinates
    else:
        print("No pins were detected.")
        return None

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    pins_coordinates = detect_spine_pins(image_path)
    print("Detected SPINE pin coordinates:", pins_coordinates)

    # Uncomment the following lines if you want to display the image with detected pins
    # cv2.imshow("Detected pins", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
