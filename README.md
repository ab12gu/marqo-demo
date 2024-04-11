# marqo-demo
Demo of marqo (multimodel vector search repository)




# Run simple query

```bash
$ docker rm -f marqo  
$ docker run --name marqo -it -p 8882:8882 marqoai/marqo:latest  
$ docker run --name marqo -it -p 8882:8882 -d marqoai/marqo:latest  
$ python3 ./test/marqo-test.py  
$ python3 ./test/marqo-results.py 
```


# Alternate vector engines
$ https://github.com/currentslab/awesome-vector-search


# Extract text from images: 
```bash
# [Optical Character Recognition (OCR)]
$ pytesseract  
$ EasyOCR  
$ Keras-OCR  
$ TrOCR  
$ docTR  
```

Discussions:
- https://cloudinary.com/guides/web-performance/extract-text-from-images-in-python-with-pillow-and-pytesseract
- https://basilchackomathew.medium.com/best-ocr-tools-in-python-4f16a9b6b116
- https://towardsdatascience.com/top-5-python-libraries-for-extracting-text-from-images-c29863b2f3d
- https://www.youtube.com/watch?v=oyqNdcbKhew


