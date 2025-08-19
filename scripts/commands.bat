oc login --token=sha256~ZFZCpXMz9Pyo18VJupWDarUgOLayJszvt3Ps33uWkJ4 --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
@REM  oc delete project <project_name>
@REM  oc new-project <data-loader> \ --description="<Test of load data.>" --display-name="<Data-Loader>"
oc new-app mongodb/mongodb-community-server -e MONGO_INITDB_ROOT_PASSWORD=12345 -e MONGO_INITDB_ROOT_USERNAME=root
oc apply -f pvc.yaml
oc set volume deployment/mongodb-community-server --add --mount-path=/var/lib/mongo --claim-name=mongodb-pvc --name mongodb-pvc
docker build -t mongo_fast:1 .
docker tag fastapi nbjo460/mongo_fast:1
docker push nbjo460/mongo_fast:1
oc new-app --image=docker.io/nbjo460/mongo_fast:1 --name=fastapi -e HOST=mongodb-community-server -e USER=root -e PASSWORD=12345
oc get service
oc expose service/fastapi
