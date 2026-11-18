import base64,glob,os
s=open('src-template.html').read()
s=s.replace('__PHOTO__','data:image/jpeg;base64,'+base64.b64encode(open('assets/photo.jpg','rb').read()).decode())
for f in glob.glob('assets/*.jpg'):
    k=os.path.basename(f)[:-4]
    s=s.replace(f'__IMG_{k}__','data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode())
assert '__IMG_' not in s
open('index.html','w').write(s); print(len(s)//1024,'KB')
