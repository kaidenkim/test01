# Create a subnet

gcloud compute networks subnets create vpc-connector-subnet \
    --network default \
    --region asia-northeast3 \
    --range 10.8.0.0/28 \
    --enable-private-ip-google-access

# Create a VPC Serverless Access Connector

gcloud compute networks vpc-access connectors create vpc-connector-001 \
    --region asia-northeast3 \
    --subnet vpc-connector-subnet

