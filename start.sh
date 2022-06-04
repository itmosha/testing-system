sudo docker stop vimdows
sudo docker rmi $(sudo docker images -f dangling=true -q)
sudo docker run -t vimdows -d -p 3000:5000 --rm -it $(sudo docker build -q code_runner/)
python3 app.py