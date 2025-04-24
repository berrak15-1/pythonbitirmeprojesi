from flask import Flask, render_template
import random

app = Flask(__name__)

cumleler = [
    "Dünya nüfusunun sadece yarısı hergün 250 ml su tasarrufu yapsaydı yılda 350 milyar litreden fazla su tasarrufu yapılmış olurdu",
    "Deniz seviyelerinin yükselmesi, kıyı bölgelerinde yaşayan milyonlarca insanı yerinden edebilir",
    "Küresel sıcaklık artışı, su kaynaklarının azalmasına ve kuraklıkların daha sık yaşanmasına yol açmaktadır.",
    "Küresel iklim değişikliği nedeniyle her yıl binden fazla türün yok olduğu tahmin ediliyor",
    "Kuzey Kutbu, dünya ortalamasından iki kat daha hızlı ısınıyor",
    "Eğer dünya nüfusunun 1/3'ü ayda 2 kagıt bosa kullanmasaydı yılda 64 milyar kagıt kurtulmuş olurdu",
    "Küresel sıcaklık artışı, su kaynaklarının azalmasına ve kuraklıkların daha sık yaşanmasına yol açmaktadır",
    "İklim değişikliği kuraklıkları, selleri ve don olaylarını artırıyor. Bu da tarımsal üretimi doğrudan etkiliyor",
    "Buzulların erimesi ve yağış rejimlerinin değişmesi, tatlı su kaynaklarını etkiliyor",
    "Artan sıcaklıklar ve kuraklık, orman yangınlarını hem daha sık hem de daha uzun süreli hale getiriyor",
    "Deniz seviyesindeki yükselme, milyonlarca insanın yaşadığı kıyı alanlarını tehdit ediyor",
    "Hayvanlar ve bitkiler, değişen iklim koşullarına uyum sağlamak için yaşam alanlarını terk ediyor",
    "İklim değişikliği, sağlık üzerinde doğrudan ve dolaylı etkiler yaratıyor",
    "Artan sıcaklıklar, tarımsal üretimde verim kayıplarına neden oluyor",
    "Bazı tarım ürünleri, artık alışıldık bölgelerde yetiştirilemiyor",
    "Okyanuslar daha fazla ısı emdikçe, fırtınalar daha güçlü hale geliyor",
    "İklim değişikliği, doğal afetlerin hem sıklığını hem de etkisini artırıyor",
    "Toprak, karbonu tutma kapasitesi sayesinde iklim değişikliğini yavaşlatabilir",
    "Enerji verimliliği, hem karbon salımını azaltır hem de ekonomik tasarruf sağlar",
    "2000'li yıllardan sonra dünya genelindeki doğal afetlerin sayısı %40 oranında arttı",
    "Elektrikli araçların kullanımı, fosil yakıt tüketimini ve dolayısıyla sera gazı emisyonlarını azaltabilir",
    "Ormansızlaşma, atmosferdeki karbon miktarını artırarak küresel ısınmayı hızlandırmaktadır"
]


@app.route("/")
def index():
    rastgele_cumle = random.choice(cumleler)
    return render_template("index.html",card_title=rastgele_cumle)  

@app.route("/ny",methods=['GET'])
def neler_yapabiliriz():
    return render_template('yapılacaklar.html')




if __name__ == "__main__":
    app.run(debug=True)