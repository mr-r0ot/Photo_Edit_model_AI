# Photo_Edit_model_AI
An AI-based model that can be used to edit and increase photo quality, restore and..

# Need To ?
Python3
PiP

# How I do running?
download ModelAI.py and run it with your comand
```
git clone https://github.com/mr-r0ot/Photo_Edit_model_AI
cd Photo_Edit_model_AI
python3 ModelAI.py
```

# Commands:
```
python3 ModelAI.py + INPUT_PHOTO_PATH + OUTPUT_PHOTO_PATH + COMMANDS

commands:
  --size(400x500)  -->  setting size for photo
  --show -->  View photo before saving
  --quality  -->  Increase photo quality
  --Adjust_brightness_and_contrast(contrast=10,brightness=2)  -->  Adjust contrast and brightness
  --enhance  -->  Increase photo quality
  --old  -->  Make the photo look like old photos
  --dark  -->  Make the photo look like dark photos
  --blurred  -->  Make the photo look like blurred photos
  --Modern_quality  -->  Make the photo look like Modern photos
  --Reconstruct_image -->  Recover the rest of the photo
  --Remove_noise -->  Remove noise photo
  --Adjust_grain -->  Sharpen the photo
```

# Example: make the photo old
```
python3 ModelAI.py INPUT_PHOTO_PATH OUTPUT_PHOTO_PATH --show --old
```


# Example: photo aging (blur)
```
python3 ModelAI.py INPUT_PHOTO_PATH OUTPUT_PHOTO_PATH --show --old --Remove_noise
```

# Example: Increase photo quality
```
python3 ModelAI.py INPUT_PHOTO_PATH OUTPUT_PHOTO_PATH --show --Modern_quality --quality
```


# and moree..
Coded By Nicola (Telegram: @black_nicola)
