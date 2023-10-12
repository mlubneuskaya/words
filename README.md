open cmd  
git clone https://github.com/mlubneuskaya/words  
cd words  
docker copose build  
docker compose up   
open in browser:  
    http://localhost:5000  
    http://localhost:5000/swagger/  


az login  
az account set --subscription "679661f7-3345-4372-a38d-3f58da522662"

az containerapp env create --resource-group ms-test --name containerappenv --location westeurope
az containerapp compose create -g ms-test --environment containerappenv

az containerapp ingress enable -n app -g ms-test --type external --target-port 5000 --transport auto
az containerapp ingress enable -n database -g ms-test --type external --target-port 5432 --transport auto
https://app--rn38nqk.gentlemeadow-c1b1a0a0.westeurope.azurecontainerapps.io:5000/
az containerapp show -n app -g ms-test    