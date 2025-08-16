from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import uuid
import shutil

app = Flask(__name__)

# Klasör tanımları
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# YOLOv8 modelini yükle
model = YOLO('best.pt')  # Buraya kendi model yolunu ver

# Gerekli klasörleri oluştur
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Türkçeye çevirme
CLASS_TRANSLATIONS = {
    "GUN": "Silah",
    "BLADE": "Kesici Alet",
    "KNIFE": "Bıçak",
    "SCREW": "Vida",
    "SHURIKEN": "Shuriken"
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    original_image_url = None
    result_image_url = None
    alert_message = None

    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="Görsel bulunamadı.")

        file = request.files['image']

        if file.filename == '':
            return render_template('index.html', error="Görsel seçilmedi.")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_id = uuid.uuid4().hex
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_id + "_" + filename)
            file.save(input_path)

            # Tahmin sonucu klasörü
            result_folder = os.path.join(app.config['OUTPUT_FOLDER'], unique_id)
            if os.path.exists(result_folder):
                shutil.rmtree(result_folder)
            os.makedirs(result_folder, exist_ok=True)

            # YOLO tahmini
            results = model.predict(
                source=input_path,
                save=True,
                project=app.config['OUTPUT_FOLDER'],
                name=unique_id,
                exist_ok=True
            )

            # Tespit edilen sınıfları al
            detected = set()
            for box in results[0].boxes:
                cls_id = int(box.cls[0].item())
                class_name = model.names[cls_id]
                translated = CLASS_TRANSLATIONS.get(class_name, class_name)
                detected.add(translated)

            # Görsel yolları
            result_img_name = os.path.basename(input_path)  # Aynı isimle kaydedildi
            original_image_url = url_for('static', filename=f'uploads/{unique_id}_{filename}')
            result_image_url = url_for('static', filename=f'outputs/{unique_id}/{unique_id}_{filename}')
            alert_message = ', '.join(detected) if detected else None

            return render_template('index.html',
                                   original_image_url=original_image_url,
                                   result_image_url=result_image_url,
                                   alert_message=alert_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


