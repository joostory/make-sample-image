# Make Sample Images

sample용 이미지를 만듭니다.

## 사용하기 전에

이미지를 만들기 위해서 [Pillow](https://github.com/python-pillow/Pillow)가 필요합니다.

```
$ pip install Pillow
```

## usage

```
Usage: make-sample-image.py [options] count

Options:
  -h, --help       show this help message and exit
  --prefix=PREFIX  filename prefix
  --ext=EXT        file ext ('png', 'jpg', 'gif')
  --output=OUTPUT  output dir
  --width=WIDTH    image width
  --height=HEIGHT  image height
```