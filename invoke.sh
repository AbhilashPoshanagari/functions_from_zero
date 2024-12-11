curl -X 'POST' \
  '0.0.0.0:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "facebook"
}'