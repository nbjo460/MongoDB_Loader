oc login --token=sha256~ZFZCpXMz9Pyo18VJupWDarUgOLayJszvt3Ps33uWkJ4 --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
@REM  oc delete project <project_name>
@REM  oc new-project <data-loader> \ --description="<Test of load data.>" --display-name="<Data-Loader>"
oc new-app mongodb/mongodb-community-server -e MONGO_INITDB_ROOT_PASSWORD=12345 -e MONGO_INITDB_ROOT_USERNAME=root
oc apply -f pvc.yaml
oc set volume deployment/mongodb-community-server --add --mount-path=/var/lib/mongo --claim-name=mongodb-pvc --name mongodb-pvc
@REM docker build -t mongo_fast:1 .
@REM docker tag fastapi nbjo460/mongo_fast:1
@REM docker push nbjo460/mongo_fast:1
docker buildx build --platform linux/amd64,linux/arm64 -t nbjo460/mongo_fastapi:latest . --push
oc create is fastapi
oc import-image fastapi:latest --from=docker.io/nbjo460/mongo_fastapi:latest --confirm
oc new-app fastapi:latest --name=fastapi -e HOST=mongodb-community-server -e USER=root -e PASSWORD=12345
@REM oc new-app --image=docker.io/nbjo460/mongo_fastapi:latest --name=fastapi -e HOST=mongodb-community-server -e USER=root -e PASSWORD=12345
oc rollout restart deployment/fastapi
oc get service
oc expose service/fastapi

