from PIL import Image

def load_img(filename):
    img = Image.open(filename)
    return img

def show_img(img_object):
    img_object.show()
    # save_name is basically a placeholder) so like anywhere that says sn irt would be replaces by something .jpg
def save_img(img_object, save_name):
    img_object.save(save_name)

img_object = load_img("obama.jpg")
show_img(img_object)
save_img(img_object, "yay.jpg")

# should return a new image object with filter applied
def obamicon(img_object):
    #create mew empty list wihc you will put all new pixels values into (hint: use append)  
    original_pixel = img_object.getdata()
  
    #use for loop to iterate through every single pixel 
    #at every pixel sum up the red dreen blue values
    #use conditionals and boolean checks to determine which new colors to change to <>=
    #idk what im doing

