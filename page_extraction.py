from selenium import webdriver
from PIL import Image

driver = webdriver.Chrome()

images = []

for i in range(1, 2):
    driver.get(f"https://testprep.cloudthat.com/mod/securepdf/view.php?id=28154&page=1={i}")
    driver.save_screenshot(f"page{i}.png")
    images.append(Image.open(f"page{i}.png").convert("RGB"))

images[0].save("output.pdf", save_all=True, append_images=images[1:])
driver.quit()