# QIDI VIDA 社区修复版

用于发布 QIDI VIDA 手机 App 社区修复包、记录已知问题和收集反馈。此项目不是官方服务，不能恢复已经停用的官方云后台。

## 下载与更新

[下载最新版安装包](https://github.com/xyjandyyk/qidi-vida-community/releases/latest) · [查看全部版本](https://github.com/xyjandyyk/qidi-vida-community/releases)

安装包通过本仓库 **Releases** 发布，不放进代码目录。每次发布提供 APK、`SHA256SUMS.txt`、更新说明和 `update.json`。

v6 新增 App 内更新检查：进入首页会检查新版，也可在 **我的 → 关于 → 版本更新** 手动检查、下载并安装。请以 Releases 中实际存在的附件为准。v5 用户需手动升级一次到 v6。

手机需要能够访问 GitHub；连接超时时可换网络后重试。App 关闭时暂不提供实时推送。

同签名的社区版本可覆盖安装。不要为解决不同签名冲突而直接卸载、丢失原有数据。

## 反馈问题

[提交故障反馈](https://github.com/xyjandyyk/qidi-vida-community/issues/new?template=bug-report.md) · [查看已有问题](https://github.com/xyjandyyk/qidi-vida-community/issues)

在 **Issues → New issue → 故障反馈** 填写版本、机型、固件、发生时间、步骤和实际结果。先搜索已有问题，避免重复提交。

这是公开仓库：**不要在 Issue 上传完整日志、轨迹、激活码、账号信息或通知正文**。只提交经过检查的错误摘要。App 导出的日志只有基础脱敏，完整日志的私密上传入口目前尚未启用。

## 本地功能与云服务

v5 修复连接、相册、GPX/健康数据处理及诊断路径。官方云组队、云账户同步等会明确提示不可用；它们需要替代后台，不能靠伪造成功恢复。

验证范围与已知边界见 [v5 发布说明](releases/v5.md)，更新功能见 [v6 发布说明](releases/v6.md)。后续版本会持续记录修复与回归结果。

## 维护者

- [发布流程](docs/PUBLISHING.md)
- [客户端更新协议](docs/UPDATE_PROTOCOL.md)
- [日志收集方案](docs/DIAGNOSTICS.md)

本仓库初始化内容不包含签名私钥、凭据、设备备份、原始日志或完整反编译树。
