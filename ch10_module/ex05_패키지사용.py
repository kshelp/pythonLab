# 패키지 사용하기
import image.io_file.imgread

image.io_file.imgread.pngread()
image.io_file.imgread.jpgread()
'''
pngread in imgread module
jpgread in imgread module
'''


from image.io_file import imgread
imgread.pngread()
imgread.jpgread()
'''
pngread in imgread module
jpgread in imgread module
'''


from image.io_file.imgread import  pngread
pngread()
# pngread in imgread module

from image.io_file.imgread import *
pngread()
jpgread()
# pngread in imgread module
# jpgread in imgread module


from image.io_file import imgread as img
img.pngread()
img.jpgread()
# pngread in imgread module
# jpgread in imgread module


from image.io_file.imgread import pngread as pread
from image.io_file.imgread import jpgread as jread

pread()
jread()
# pngread in imgread module
# jpgread in imgread module

