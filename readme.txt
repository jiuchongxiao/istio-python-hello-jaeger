1.cd hello

2.生成镜像
docker build -t dinfo.cn/jiabao/python-hello:latest .
3.cd ..
4.启动(注意方便测试 指定了pod运行的node    kubectl label nodes nlp04 node=python-hello    kubectl get node -a -l "node=python-hello"）
kubectl create -f <(istioctl kube-inject -f pytho-helloworl.yaml)
5.kubectl get pods 确定启动成功
6.访问服务
http://192.168.181.99:30022/python-sa/info
7.查看jaeger ui
http://192.168.181.99:30668/search

8.新增日志功能，发送到fluent
有两种发送方式
1）app.py中记录的直接sendfluent interface
2)app-logging.py中记录的定义log格式并发送日志

9：注意
部署到istio中需要修改地址
1）服务之间的调用地址
2）fluent远程地址
