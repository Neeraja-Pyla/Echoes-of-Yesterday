
import uuid
from pathlib import Path
from io import BytesIO
from PIL import Image

UPLOAD_FOLDER = Path("uploads")
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB


def save_uploaded_image(image_bytes):

    UPLOAD_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    if len(image_bytes) > MAX_IMAGE_SIZE:
        raise ValueError("Image must be smaller than 10 MB.")

    try:
        image = Image.open(BytesIO(image_bytes))

        if image.format not in ["JPEG", "PNG"]:
            raise ValueError("Only JPG and PNG images are supported.")

        image.load()

        image = image.convert("RGB")

    except Exception:
        raise ValueError("Invalid or unsupported photograph.")

    filename = f"{uuid.uuid4().hex}.jpg"

    file_path = UPLOAD_FOLDER / filename

    image.save(
        file_path,
        format="JPEG",
        quality=90
    )

    return str(file_path)


def delete_uploaded_image(image_path):

    if not image_path:
        return

    path = Path(image_path)

    try:
        if path.parent.resolve() == UPLOAD_FOLDER.resolve():
            if path.is_file():
                path.unlink()

    except OSError as error:
        print(f"Image deletion error: {error}")
