# Order Tracking Bot 🤖

A conversational AI bot built with Rasa and React for managing retail orders. This system provides customers with natural language interaction capabilities to track, modify, and manage their orders.

## 🌟 Features

### Core Functionality
- **Order Tracking**: Real-time order status updates and tracking information
- **Order Management**: Place new orders, modify existing orders, and cancel orders
- **Shipping Management**: Update shipping addresses and delivery preferences
- **Invoice Generation**: Automated PDF invoice generation and retrieval
- **Product Catalog**: Browse and search product listings
- **Cancellation Fees**: Calculate and display order cancellation fees

### Technical Features
- **Natural Language Processing**: Rasa for intent recognition and dialogue management
- **RESTful API**: Flask-based backend with comprehensive API endpoints
- **Modern Frontend**: React with TypeScript for a responsive user interface
- **Database Integration**: SQLite
- **Docker Support**: Containerized deployment with Docker Compose
- **Environment Management**: Secure configuration with Doppler integration

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Docker (optional)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/order-tracking-bot.git
cd order-tracking-bot
```

### 2. Backend Setup

#### Option A: Local Development
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database and generate Rasa files
python main.py

# Start the services
chmod +x start.sh
./start.sh
```

#### Option B: Docker Deployment
```bash
# Build and start all services
docker-compose up --build

# Or use the Makefile
make up
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Rasa API: http://localhost:5005
- Custom Actions: http://localhost:5055
- Flask API: http://localhost:5000

```