import uuid
import os


def recipe_image_file_path(instance, filename):
    """Generate file path for a new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipes/', filename)
