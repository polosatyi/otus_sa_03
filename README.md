# OTUS SA-2020-09 homework #03

## Installation instructions
* `kubectl create namespace otusapp`;
* `kubectl config set-context --current --namespace=otusapp`;
* `helm repo add bitnami https://charts.bitnami.com/bitnami` (https://github.com/bitnami/charts/tree/master/bitnami/postgresql);
* `helm install otusapp-db bitnami/postgresql`;
* `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
* `helm install prom prometheus-community/kube-prometheus-stack -f prometheus.yaml --atomic`
* `helm install postgres-exporter prometheus-community/prometheus-postgres-exporter -f postgres-exporter.yaml`
* `helm dependency update ./otusapp-chart`
* `minikube addons disable ingress`
* `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx` -->
* `helm install nginx ingress-nginx/ingress-nginx -f nginx-ingress.yaml --atomic` -->
* DRY RUN: `helm install otusapp ./otusapp-chart --dry-run`
* INSTALL: `helm install otusapp ./otusapp-chart --atomic`
* UNINSTALL: `helm uninstall otusapp` & `kubectl delete all --all` & it's needed to remove old pvc instances (`kubectl get pvc` & `kubectl delete pvc {pvc_name}`).

The job (initdb.yaml) starts with a 10 second delay.

Checking:
* `curl -H'Host: arch.homework' http://192.168.64.3/otusapp/ksalov`

## Available endpoints

* `GET` http://arch.homework/otusapp/ksalov/
* `GET` http://arch.homework/otusapp/ksalov/health/
* `GET` http://arch.homework/otusapp/ksalov/version/
* `POST` http://arch.homework/otusapp/ksalov/user
* `GET` http://arch.homework/otusapp/ksalov/user/{user_id}
* `PUT` http://arch.homework/otusapp/ksalov/user/{user_id}
* `DELETE` http://arch.homework/otusapp/ksalov/user/{user_id}

## Monitoring & alerting
Graphana: `kubectl port-forward service/prom-grafana 9000:80` (endpoint: http://127.0.0.1:9000/, login: `admin`, password: `prom-operator`)
Prometheus: `kubectl port-forward service/prom-kube-prometheus-stack-prometheus 9090` (endpoint: http://127.0.0.1:9090/)

## Postman tests
`newman run user_api.json`
