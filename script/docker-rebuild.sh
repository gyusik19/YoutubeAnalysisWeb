docker-compose down
docker volume rm youtube-meta_static youtube-meta_media
docker-compose up -d --build
