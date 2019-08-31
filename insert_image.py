from PIL import Image

img = Image.open("./image/KakaoTalk_20190806_133853463_04.jpg")
sung_jin = Image.open("./image/simpson_sungjin.jpg")
hyun_jae = Image.open("./image/simpson_hyunjae.jpg")

sung_jin = sung_jin.resize((1954 - 1687, 1865 - 1597))
hyun_jae = hyun_jae.resize((1150 - 965, 2863 - 2677))

img.paste(sung_jin,(1597, 1687))
img.paste(hyun_jae,(2677, 965))

img.save("./image/paste_image.jpg")

