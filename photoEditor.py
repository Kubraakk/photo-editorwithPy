
import numpy as np
from PIL import Image


print("Fotoğraf Editörüne Hoşgeldiniz...")


while True:
    print("Yapmak İstediğiniz İşlemi Seçiniz: \n1.Resim Yükleme\n2.Resmi Siyah-Beyaz Yapma\n3.Resmi yatay eksende döndürme")
    islem = int(input("Yapmak istediğiniz işlem numarasını giriniz:"))
    if islem == 1:
        resim=input("Yüklemek istediğiniz resim dosyasının adını giriniz:")
        image = Image.open(resim)
        print("Resim yükleniyor...")
        image.show()
        npImage = np.array(image)
        print("Devam etmek istediğiniz işlemi giriniz:\n2.Resimi siyah-beyaz yapma\n3.Resmi yatay eksende döndürme")
        islem2 =int(input("Yapmak istediğiniz işlem numarasını giriniz:"))
        if islem2==2:
            npImage= np.array(image)
            grayImage = np.zeros(npImage.shape)
            R = np.array(npImage[:,:,0])
            G = np.array(npImage[:,:,1])
            B = np.array(npImage[:,:,2])

            R= (R*.299)
            G= (G*.587)
            B= (B*.114)

            image2 = (R+G+B)
            grayImage = npImage

            for i in range(3):
                grayImage[:,:,i] = image2
            image2 = Image.fromarray(npImage)
            print("Filtre uygulanıyor.Lütfen bekleyiniz.")
            image2.show()
        elif islem2==3:
            image3 = np.array(npImage)
            image4 = image.size[1]-1
            for i in range(0,(image.size)[1]):
                image3[image4]= npImage[i]
                image4-=1

            image5=Image.fromarray(image3)
            print("Resim 180 derece çevriliyor...")
            image5.show()

    else:
        print("Lütfen ilk önce işlem 1 ile başlayınız!")
