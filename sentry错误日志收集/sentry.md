

### sentry是什么

> We’re so much more than **error monitoring software**. We’re also **performance monitoring software**. Our platform helps every developer diagnose, fix, and optimize the performance of their code. With Sentry, developers around the world save time, energy, and probably a few therapy sessions.

sentry是一个基于Django构建的现代化的实时事件日志监控、记录和聚合平台,主要用于如何快速的发现故障。





### sentry私有化部署

项目：[GitHub](https://github.com/getsentry/self-hosted)

文档：[doc](https://develop.sentry.dev/self-hosted/)

步骤简介：

```bash
git clone https://github.com/getsentry/self-hosted.git
mv self-hosted sentry
cd sentry
sudo ./install.sh
sudo docker-compose up -d 
```







