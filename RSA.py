import cv2
import numpy as np

demo = cv2.imread("C:\Users\lenovo\Documents\Semester 3\Praktik Sistem Keamanan Data\P10\Gambar.jpeg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("C:\Users\lenovo\Documents\Semester 3\Praktik Sistem Keamanan Data\P10\KEY-Gambar.jpeg", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("C:\Users\lenovo\Documents\Semester 3\Praktik Sistem Keamanan Data\P10\ENC-Gambar.jpeg", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("C:\Users\lenovo\Documents\Semester 3\Praktik Sistem Keamanan Data\P10\DES-Gambar.jpeg", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()