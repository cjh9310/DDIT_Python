from PIL import Image

Image.open('imgs/01.jpg')

latent_real = torch.load('inversion_codes/01.pt')['latent']
latent_real = style2list(latent_real)

source_im, _ = generator1(latent_real)

display_image(source_im)


result2 = toonify(latent_real, latent2)

display_image(result2)






import cv2

rect_img = tensor2image(source_im).copy()

x, y, w, h = 65, 80, 120, 120

cv2.rectangle(rect_img, pt1=(x, y), pt2=(x+w, y+h), thickness=2, color=(255, 255, 255))

plt.imshow(rect_img)


reference_im, _ = generator1(latent2)

display_image(reference_im)


with torch.no_grad():
    blend = generator1.blend_bbox(latent_real, latent2, [(x, y, w, h)], model_type='face', num_blend=10)

display_image(blend)