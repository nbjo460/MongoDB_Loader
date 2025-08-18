oc login --token=sha256~ZFZCpXMz9Pyo18VJupWDarUgOLayJszvt3Ps33uWkJ4 --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
@REM  oc delete project <project_name>
@REM  oc new-project <data-loader> \ --description="<Test of load data.>" --display-name="<Data-Loader>"
oc new-app mysql --name mysql -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_DATABASE=load_db -e MYSQL_USER=menachem -e MYSQL_PASSWORD=yarhi
oc create -f C:\Users\Menachem\Desktop\Galil\data-loader\infrastructure\k8s\pvc.yaml
oc set volume deployment/mysql --add --mount-path=/var/lib/mysql --claim-name=mysql-pvc --name mysql-pvc
oc cp .\create_data.sql mysql-68dcc6f4c7-75dds:/var/lib/mysql
oc cp ./insert_data.sql mysql-68dcc6f4c7-75dds:/var/lib/mysql
oc exec -it mysql-68dcc6f4c7-bwl78 -- bash
mysql -u menachem -p
use load_db;
source /var/lib/mysql/create_data.sql
source /var/lib/mysql/insert_data.sql
docker build -t backend_load_data .
docker run -d --name api -p 8000:8000  -e username=root -e password= -e database=malshinon -e table=alerts backend_load_data
docker tag backend_load_data nbjo460/backend_load_data:1.1
oc new-app --docker-image=docker.io/nbjo460/backend_load_data:1.2  --name=fastapi -e username=root -e password=12345 -e database=load_db -e table=data -e host=mysql
