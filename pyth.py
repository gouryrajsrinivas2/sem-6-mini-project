import cv2
import sys
import pytesseract
import re
import sys
if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)
  
  # Read image path from command line
  imPath = sys.argv[1]
  reload(sys)
  sys.setdefaultencoding('utf8')
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' sets the OCR Engine Mode to LSTM only.
  #
  #  There are four OCR Engine Mode (oem) available
  #  0    Legacy engine only.
  #  1    Neural nets LSTM engine only.
  #  2    Legacy + LSTM engines.
  #  3    Default, based on what is available.
  #
  #  '--psm 3' sets the Page Segmentation Mode (psm) to auto.
  #  Other important psm modes will be discussed in a future post.  


  config = ('-l eng --oem 1 --psm 3')

  # Read image from disk
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(im, config=config)

  # Print recognized text
  f=open("output.txt","w")
  f.write(text)
  y=re.findall('Total.*',text)
  ''' x=y[0].split(" ")
  #print(x[1])
  if(x[1]>sys.argv[2]):
      print("result is grater than given value")
  else:
      print("result is less than given value")'''