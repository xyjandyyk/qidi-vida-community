# 更新协议（v6 已实现）

`update.json` 提供 schemaVersion、channel、packageName、versionCode、versionName、minSdk、downloadUrl、sha256、sizeBytes、signerCertificateSha256、releaseNotesUrl。

客户端行为：

1. 启动后限频检查，保留手动检查入口；检查失败不阻塞蓝牙、运动或相册。
2. 比较 versionCode，而不是按版本字符串大小判断。仅提示更高版本。
3. 展示发布说明与文件大小，由用户发起下载；下载可取消、重试。
4. 对完整下载文件验证 SHA-256、包名、versionCode 和 APK 签名证书。客户端内固定信任现有签名证书，不能单凭远程清单提供的证书值建立信任。
5. 使用系统安装流程，按系统要求由用户确认。签名不符、哈希错误或下载未完成时不得调用安装。
6. 不在 APK 中嵌入 GitHub PAT、仓库写权限或签名私钥。

v6 提供首页前台检查及手动检查，同一次 App 运行自动检查间隔至少 15 分钟，不承诺 App 未运行时实时通知。v5 没有此能力，需要手动安装一次 v6。

清单最大 64 KiB，APK 最大 512 MiB；仅接受指定仓库的 HTTPS 下载地址及 GitHub 官方附件域名跳转。连接超时 15 秒、读取超时 20 秒。文件放在应用缓存，检查大小、哈希、包名、版本名称、递增版本号和固定签名证书通过后打开系统安装页。取消、返回或离开下载页会取消当前下载，重试从头开始。

现有签名证书 SHA-256：`79533c8ad5e18c34a8958513b14aba52fa7783af1641a9cff1c8be8b0e8e7bd6`。它是公开证书摘要，不是私钥。
