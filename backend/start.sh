#!/bin/bash

echo "Setting up environment..."


python -c "
try:
    from scripts.doppler_env import main as create_env
    create_env()
    print('.env file created via Doppler')
except Exception as e:
    print(f'Doppler env creation failed: {e}')
    with open('.env', 'w') as f:
        f.write('DB_NAME=retail.db\n')
        f.write('DB_PASSWORD=admin_password\n')
        f.write('DB_PORT=8081\n')
        f.write('DB_USER=admin\n')
        f.write('DOPPLER_CONFIG=\n')
        f.write('DOPPLER_ENVIRONMENT=\n')
        f.write('DOPPLER_PROJECT=\n')
    print('Fallback .env file created')
"


echo "Starting backend API..."
PYTHONPATH=/app python -m backend.api &

echo "Starting main.py..."
PYTHONPATH=/app python -m backend.main &


echo "Applying TensorFlow CPU-only fix..."
python -c "
import os
import tensorflow as tf
os.environ['CUDA_VISIBLE_DEVICES'] = ''
tf.config.set_visible_devices([], 'GPU')
print('TensorFlow GPU disabled successfully')
" || echo "TensorFlow GPU fix failed"


echo "Training Rasa model..."
rasa train || echo "Rasa training failed (possibly already trained)"

# Run rasa
echo "Starting Rasa server..."
CUDA_VISIBLE_DEVICES="" rasa run -i 0.0.0.0 --enable-api --cors "*" --port 5005 &

echo "Starting custom actions server..."
rasa run actions --port 5055 &


wait