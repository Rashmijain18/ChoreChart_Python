# Docker Setup Guide for ChoreChart (Python Backend)

This guide will walk you through setting up the ChoreChart application using Docker and Docker Compose with a Python FastAPI backend.

## Prerequisites

1. **Docker Desktop** installed on your machine

   - Download from: https://www.docker.com/products/docker-desktop/
   - Ensure Docker is running

2. **Git** (if not already installed)
   - Download from: https://git-scm.com/

## Project Structure

The application consists of 4 main services:

- **PostgreSQL Database** (port 5432)
- **pgAdmin** - Database management tool (port 5050)
- **FastAPI Backend** (port 4000) - Python-based
- **React Frontend** (port 3000)

## Step-by-Step Setup

### Step 1: Navigate to Project

```bash
cd /Users/apple/Desktop/Rashmi_Code_repo/ChoreChart_python/ChoreChart
```

### Step 2: Create Environment File

Copy the environment template and customize if needed:

```bash
cp env.example .env
```

### Step 3: Start Docker Desktop

Make sure Docker Desktop is running on your machine.

### Step 4: Build and Start Services

```bash
# Build all Docker images
docker-compose build

# Start all services in detached mode
docker-compose up -d

# Or start and see logs in real-time
docker-compose up
```

### Step 5: Verify Services are Running

```bash
# Check running containers
docker-compose ps

# Check service logs
docker-compose logs

# Check specific service logs
docker-compose logs server
docker-compose logs ui
```

### Step 6: Access the Application

Once all services are running, you can access:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:4000
- **API Health Check**: http://localhost:4000/health
- **pgAdmin**: http://localhost:5050
  - Email: admin@admin.com
  - Password: admin

## Docker Commands Reference

### Development Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# Rebuild and start
docker-compose up --build

# View logs
docker-compose logs -f

# Execute commands in containers
docker-compose exec server bash
docker-compose exec ui bash
docker-compose exec postgres psql -U admin -d chorechart
```

### Production Commands

```bash
# Build production images
docker-compose build --target production

# Start production services
docker-compose up -d
```

### Troubleshooting Commands

```bash
# Remove all containers and volumes
docker-compose down -v

# Remove all images
docker-compose down --rmi all

# Clean up Docker system
docker system prune -a

# Check container health
docker-compose ps
```

## Service Details

### 1. PostgreSQL Database

- **Container**: chorechart-db
- **Port**: 5432
- **Database**: chorechart
- **User**: admin
- **Password**: adminpass
- **Volume**: postgres_data (persistent data)

### 2. pgAdmin

- **Container**: chorechart-pgadmin
- **Port**: 5050
- **Email**: admin@admin.com
- **Password**: admin
- **Purpose**: Database management interface

### 3. FastAPI Backend (Python)

- **Container**: chorechart-api
- **Port**: 4000
- **Framework**: FastAPI with Python 3.11
- **Features**: Auto-reload in development
- **Health Check**: /health endpoint
- **Dependencies**: See server/requirements.txt

### 4. React Frontend

- **Container**: chorechart-ui
- **Port**: 3000
- **Framework**: React with Vite
- **Features**: Hot reload in development
- **Build Tool**: Vite

## Python Backend Details

### Dependencies (server/requirements.txt)

- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **SQLAlchemy**: ORM for database
- **Alembic**: Database migrations
- **psycopg2-binary**: PostgreSQL adapter
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation
- **python-multipart**: File upload support

### API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

### Development Features

- Auto-reload on code changes
- Hot reload for development
- Health checks
- Volume mounting for live code editing

## Environment Variables

Key environment variables (defined in `.env`):

```bash
# Database
POSTGRES_USER=admin
POSTGRES_PASSWORD=adminpass
POSTGRES_DB=chorechart

# API
API_PORT=4000
CORS_ORIGIN=http://localhost:3000

# Frontend
VITE_API_URL=http://localhost:4000
```

## Health Checks

All services include health checks:

- **Database**: PostgreSQL readiness check
- **Backend**: HTTP health endpoint at /health
- **Frontend**: HTTP availability check

## Volumes

Persistent data is stored in Docker volumes:

- `postgres_data`: Database files
- `pgadmin_data`: pgAdmin configuration

## Development Workflow

1. **Start services**: `docker-compose up -d`
2. **Make code changes**: Edit Python files in your IDE
3. **Auto-reload**: FastAPI will automatically reload on changes
4. **View logs**: `docker-compose logs -f server`
5. **Stop services**: `docker-compose down`

## Common Issues and Solutions

### Port Already in Use

```bash
# Check what's using the port
lsof -i :3000
lsof -i :4000
lsof -i :5432

# Stop conflicting services or change ports in docker-compose.yml
```

### Permission Issues

```bash
# Fix file permissions
sudo chown -R $USER:$USER .

# Or run Docker with proper permissions
sudo docker-compose up
```

### Database Connection Issues

```bash
# Check database logs
docker-compose logs postgres

# Restart database
docker-compose restart postgres

# Reset database (WARNING: loses data)
docker-compose down -v
docker-compose up -d
```

### Python Dependencies Issues

```bash
# Rebuild server container
docker-compose build server

# Install new dependencies
docker-compose exec server pip install new-package

# Update requirements.txt and rebuild
docker-compose build server
```

### Build Issues

```bash
# Clean build
docker-compose down
docker system prune -a
docker-compose build --no-cache
docker-compose up -d
```

## Next Steps

After successful setup:

1. Access the frontend at http://localhost:3000
2. Test the API at http://localhost:4000
3. Check the health endpoint at http://localhost:4000/health
4. Set up database schema using Alembic
5. Start developing your FastAPI endpoints!

## Support

If you encounter issues:

1. Check the logs: `docker-compose logs`
2. Verify Docker is running
3. Check port availability
4. Review this guide for common solutions
