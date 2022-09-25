> 参考项目：[GitHub](https://github.com/PagerTree/prometheus-grafana-alertmanager-example)
>
> 另一个可参考视频：[链接1](https://www.bilibili.com/video/BV1HN4y157Zk)
>
> 



# 简介

基于 Prometheus+Grafana+Alertmanager+飞书通知 的监控告警平台

## Prometheus

官方文档：[官方文档](https://prometheus.io/docs/introduction/overview/)

Prometheus 是一款基于时序数据库的开源监控告警系统，基本原理是通过HTTP协议周期性抓取被监控组件的状态，任意组件只要提供对应的HTTP接口就可以接入监控。输出被监控组件信息的HTTP接口被叫做**exporter** 。目前互联网公司常用的组件大部分都有exporter可以直接使用，比如Varnish、Haproxy、Nginx、MySQL、Linux系统信息(包括磁盘、内存、CPU、网络等等)。



## Alertmanager

Prometheus监控系统中，采集与警报是分离的，警报规则在 **Prometheus** 定义，警报规则触发以后，才会将信息转发到给独立的组件 **Alertmanager** ，经过 **Alertmanager** r对警报的信息处理后，最终通过接收器发送给指定用户。

文档：[官方文档](https://prometheus.io/docs/alerting/latest/alertmanager/)



## Grafana

官方文档：[GitHub](https://github.com/grafana/grafana)

Grafana是一款用Go开发的开源数据可视化工具，可以做数据监控和数据统计。

结合Prometheus使用 [文档](https://grafana.com/docs/grafana/v9.0/datasources/prometheus/)



## 架构图

![Prometheus architecture](https://prometheus.io/assets/architecture.png)







# Demo

环境准备：

准备2台虚拟机，Ubuntu20.04，例如

```bash
master: 192.168.31.121  
node1: 192.168.31.83   
```



### 安装node-exporter

node-exporter用于采集服务器层面的运行指标，包括机器的loadavg、filesystem、meminfo等基础监控，类似于传统主机监控维度的zabbix-agent。

官方文档：[node_exporter](https://github.com/prometheus/node_exporter)

可以采用二进制安装、docker安装、k8s安装。具体见官方文档

docker安装

```bash
docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter:latest \
  --path.rootfs=/host
```



### 启动app转发alert

app.py ：主要接收来自Alertmanager的告警，以一定规则格式转发到群聊，方便及时查看。

在master上启动





## 启动使用



### 1.启动 Prom+Grafana+Alert

master:

```bash
sudo docker-compose up -d
# 查看启动的容器
sudo docker-compose ps
# 停止和删除容器、网络、卷、镜像。
sudo docker-compose down --volumes
```



### 2.访问

prom：http://192.168.31.121:9090

grafana: http://192.168.31.121:3000   账号：密码(admin: admin)

alert: http://192.168.31.121:9093



:::tip

基本告警监控已经可以运作，其他就是：

1.完善grafana的dashbords（可以去官网找找现有的）

2.添加其他exporter，比如nginx-vts-exporter，或者数据库exporter，接入到prometheus（prometheus/prometheus.yml）。

3.增加或修改告警规则（prometheus/alert.rules）

:::



