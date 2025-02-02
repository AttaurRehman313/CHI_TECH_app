from flask import Blueprint, request,jsonify
from mainapp.utils.file_loadin_and_chunking import extract_text_and_image_from_slide,transcribe_image,image_runs,image_count
from mainapp.model.file_embedding import create_vector_db
upload=Blueprint("upload_pdf",__name__)


@upload.route("/upload_pptx", methods=["POST"])
def upload_pdf():
    """
    This route handles the upload of PDF files via a POST request. 
    It ensures the file is saved and processed into a vector database.
    """
    if request.method=="POST":
        file = request.files['file']
        if file == '':
            return jsonify({"message": "No file selected."}), 400
        
        elif isinstance(file, str) and not file.lower().endswith('.pptx'):
            return jsonify({"message":"only upload .pptx file"}), 400
        
        
        extract_text_and_image_from_slide(file)
        print("\ntext are extract AND image are restricted")
        data=transcribe_image(image_runs)
        image_lenght=image_count
        print("tesxt are transcribe")
        
        create_vector_db(data)
        return jsonify({"message": "Your vector is stored successfully."}), 200
 