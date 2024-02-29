E='photoAI.py';B=exit;A=print;from os import system as F,listdir as G
if not E in G():
	try:from requests import get
	except:
		F('pip install requests')
		try:from requests import get
		except:A('Error! Please Install Requests Library');B()
	try:
		C=get('https://mr-r0ot.github.io/photoAI_python_library/photoAI.py')
		if C.status_code!=200:A('GiHub Error!');B()
	except:A('NetWork Error!');B()
	D=open(E,'w+');D.write(C.text);D.close()
import photoAI
import sys


try:
	input_photo=sys.argv[1]
	output_photo=sys.argv[2]
except:
	print('Enter Path Photo --> file.py photo.png output.png')
argv=''
for a in sys.argv:
	argv=(f'{argv} {a}')
argv=argv.lower()
try:
	image = photoAI.open_photo(input_photo)
except:
	print('Photo Not Find!')
	sys.exit()


if '--size(' in argv:
	size=(argv.split('--size(')[1])
	size1=(size.split('x')[0])
	size2=(size.split('x')[1])
	size2=(size2.split(')')[0])
	image = photoAI.photo.Setting_size(image,size1,size2)

if '--quality' in argv or 'quality' in argv:
    image = photoAI.photo.Setting_quality(image,quality=1000)
if '--Adjust_brightness_and_contrast(contrast=10,brightness=2)' in argv or 'contrast' in argv or 'brightness' in argv:
	con=argv.split('contrast=')[1]
	con=con.split(',')[0]
	bri=argv.split('brightness=')[1]
	bri=bri.split(')')[0]
	image = photoAI.photo.Adjust_brightness_and_contrast(image,contrast=int(con),brightness=int(bri))
if '--enhance' in argv or 'enhance' in argv or 'quality' in argv:
    image = photoAI.photo.Enhance_image(image)

if '--old' in argv or 'old' in argv:
	image = photoAI.filters.Old_filter(image)

if '--dark' in argv or 'dark' in argv:
	image = photoAI.filters.Dark_filter(image)

if '--blurred' in argv or 'blurr' in argv:
	image = photoAI.filters.Blurred_filter(image)

if '--modern_quality' in argv or 'modern' in argv:
	image = photoAI.filters.Modern_quality(image)

if '--reconstruct_image' in argv or 'reconstruct' in argv:
	image = photoAI.photo.Reconstruct_image(image)

if '--remove_noise' in argv or 'noise' in argv:
	image = photoAI.photo.Remove_noise(image)

if '--adjust_grain' in argv or 'grain' in argv:
	image = photoAI.photo.Adjust_grain(image)

if '--show' in argv or 'show' in argv:
    photoAI.show_photo('photo',image)
photoAI.save_photo(output_photo,image)
