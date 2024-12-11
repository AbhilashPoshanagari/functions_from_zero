[![Python CI](https://github.com/AbhilashPoshanagari/functions_from_zero/actions/workflows/main.yml/badge.svg)](https://github.com/AbhilashPoshanagari/functions_from_zero/actions/workflows/main.yml)

# functions_from_zero
curl -X 'POST' \
  '0.0.0.0:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "facebook"
}'
## Docker Image
`docker build .`
`docker image ls`

## run docker image
`docker run localhost:8080:8080 image_Id`