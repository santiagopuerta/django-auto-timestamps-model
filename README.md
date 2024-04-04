# Django Auto Timestamps Model

Django model for automatic timestamps.

## Features

- Automatically adds `created_at` and `updated_at` timestamps to your Django models.
- Simplifies tracking of creation and modification times of objects.

## Installation

You can install `django-auto-timestamps-model` via pip:

```sh
pip install django-auto-timestamps-model
```

## Usage

1. Install django-auto-timestamps-model using pip.
2. Import the AutoTimestampsModel class from this module.
3. Inherit the AutoTimestampsModel class in your Django model class.
4. The 'created_at' and 'updated_at' fields will be automatically added to your model.
5. The 'created_at' field will be set to the current timestamp when a new instance is created.
7. The 'updated_at' field will be updated with the current timestamp whenever the model is saved.

Example:
```python
from django.db import models
from django_auto_timestamps_model import AutoTimestampsModel

class YourModel(AutoTimestampsModel, models.Model):
    # Your model fields here
```

## Compatibility
```
Django >= 1.4 and Django <= 4.2
```

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.