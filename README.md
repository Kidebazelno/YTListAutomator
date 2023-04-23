## Description
- In one of my course, my professor give us a PDF file containing all the recorded video on Youtube, and ask us to watch the video every week. 
- However, I find it annoying to open the PDF every time, also, I have to copy the PDF among different devices in order to watch Youtube video on all devices.
- Therefore, I decide to write a program with selenium that stores all the URLs in the PDF to a Youtube playlist, so I can simply use Youtube app on all devices.
## Environment
```shell
pip install -r requirements.txt
```

```shell
python3 crawl.py -a 'user@gmail.com' -p 'YourPassword' -f 'path/to/pdfFile/containing/YT/links'
```