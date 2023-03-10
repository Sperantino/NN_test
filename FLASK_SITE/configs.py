import os


base_dir = os.path.dirname(os.path.dirname(__file__))

dir_models = os.path.join(base_dir, 'models') # dir with models

if not os.path.exists(dir_models):
    os.mkdir(dir_models)

dir_images = os.path.join(base_dir, 'images') # dir with save images

if not os.path.exists(dir_images):
    os.mkdir(dir_images)

# Описание наших моделей для классов изображений
type_images = {
    'TIRADS': {
        'name_desease': 'TIRADS',
        'model_path': os.path.join(dir_models, 'TIRADS/activities_81.26.h5'),
        'input_shape': (260, 200, 3),
        'save_images': os.path.join(dir_images, 'TIRADS/activities_81.26.h5')
    }
}

# Доступные фформаты изображений
allowed_types = ['jpg', 'png', 'bmp', 'jpeg']