# Chatzy Docker Images 

This README provides all the commands to check that the Chatzy frontend and backend Docker images are working correctly from Docker Hub.

---

## **Prerequisites**

- Docker must be installed and running on your machine.  
- Ensure the following host ports are free:
  - Backend: `8000`
  - Frontend: `3000`

---

## **Commands to Test Docker Images**

```bash
# Step 1: Pull Docker images from Docker Hub
docker pull medhavini330/chatbot-backend:latest
docker pull medhavini330/chatbot-frontend:latest

# Step 2: Check running containers (optional)
docker ps

# If any container is using ports 8000 or 3000, stop and remove it:
docker stop <container_id>
docker rm <container_id>

# Step 3: Run backend container
docker run -d -p 8000:8000 --name chatzy-backend medhavini330/chatbot-backend:latest
# Backend URL: http://localhost:8000

# Step 4: Run frontend container
docker run -d -p 3000:80 --name chatzy-frontend medhavini330/chatbot-frontend:latest
# Frontend URL: http://localhost:3000

# Optional: If port 3000 is in use, map frontend to a different host port
docker run -d -p 3001:80 --name chatzy-frontend medhavini330/chatbot-frontend:latest
# Frontend URL: http://localhost:3001

# Step 5: Verify logs (optional)
docker logs chatzy-backend
docker logs chatzy-frontend

# Step 6: Cleanup (optional)
docker stop chatzy-backend chatzy-frontend
docker rm chatzy-backend chatzy-frontend
