import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
import cv2


tree = et.parse('img/WhatsApp Image 2022-07-05 at 2.46.28 PM.xml')

with open('img/WhatsApp Image 2022-07-05 at 2.46.28 PM.xml', 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data, "xml")
b_unique = bs_data.find_all('object')

root = tree.getroot()


filename = root[1].text
print('filename: ', filename)
path = root[2].text
print('path: ', path)
count = len(b_unique)

img = cv2.imread(path)

for i in range(count):
    class_name = root[i+6][0].text
    print('class_name: ', class_name)
    xmin = root[i+6][4][0].text
    print('xmin: ', xmin)
    ymin = root[i+6][4][1].text
    print('ymin: ', ymin)
    xmax = root[i+6][4][2].text
    print('xmax: ', xmax)
    ymax = root[i+6][4][3].text
    print('ymax: ', ymax)

    
    cv2.rectangle(
        img, (int(xmin), int(ymin)), (int(xmax), int(ymax)),
        (0, 255, 0), 2
    )
    cv2.putText(
        img, f'{class_name}',
        (int(xmin), int(ymin)),
        cv2.FONT_HERSHEY_PLAIN, 2,
        (0, 255, 255), 2
    )

img_resize  = cv2.resize(img, (640, 480))
cv2.imshow('image', img_resize)
if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()

