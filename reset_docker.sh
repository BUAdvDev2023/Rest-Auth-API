# THIS CODE WILL DELETE ALL YOUR CONTAINERS IMAGES AND VOLUMES FOR YOUR PROJECT ONLY!!

# Set the Docker project name
DOCKER_PROJECT_NAME="rest-auth-api"

# Stop and remove containers for the specified project
docker-compose -p $DOCKER_PROJECT_NAME down

# Remove all Docker images for the specified project
docker -p $DOCKER_PROJECT_NAME rmi -f $(docker -p $DOCKER_PROJECT_NAME images -a -q)

# Remove all Docker volumes for the specified project
# docker -p $DOCKER_PROJECT_NAME volume rm $(docker -p $DOCKER_PROJECT_NAME volume ls -q)

# Bring up Docker Compose services for the specified project
docker-compose -p $DOCKER_PROJECT_NAME up -d

#--------------------------------------------------------------------------------------------

# THIS CODE WILL DELETE ALL YOUR CONTAINERS IMAGES AND VOLUMES FOR DOCKER OVERALL!!

# # Stop and remove containers
# docker-compose down

# # Remove all Docker images
# docker rmi -f $(docker images -a -q)

# # Remove all Docker volumes
# docker volume rm $(docker volume ls -q)

# # Remove Docker cache
# docker builder prune -a --force

# # Bring up Docker Compose services
# docker-compose up -d
