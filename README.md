## Description
- In one of my course, my professor give us a PDF file containing all the recorded video on Youtube, and ask us to watch the video every week. 
- However, I find it annoying to open the PDF every time, also, I have to copy the PDF among different devices in order to watch Youtube video on all devices.
- Therefore, I decide to write a program with selenium that stores all the URLs in the PDF to a Youtube playlist, so I can simply use Youtube app on all devices.
## Environment
```shell
pip install -r requirements.txt
```
## Execute
Heres one example of running the code:
```shell
python3 crawl.py -a 'user@gmail.com' -p 'YourPassword' -f 'path/to/pdfFile/containing/YT/links' -n 0
```
## Usage
- a,account argument is the Youtube account you want to login
- p,password argument is the password of your YT account
- f,file argument is the path to the URLs PDF
- n,newlist is the option that decide whether to create a new playlist or use the existing one. Any number other than 0 will create a new list.
- l,listname is the name of your playlist.