# 发布流程

1. 使用原社区签名密钥构建、验证 APK。私钥保存在维护者本地，不提交仓库、不放进 APK，也不放进公开 Actions 日志。
2. 维护递增的 Android versionCode。不得用同一版本号向已安装用户推送不同二进制。
3. 在本机运行 `python scripts/prepare_release.py --repo OWNER/REPO --apk PATH --out out/v5`，生成 v5 校验文件及更新清单。脚本校验此次已验收 APK 的确切哈希，不复制原始工作目录或日志。
4. 仓库有初始提交后，在 Releases 创建草稿：tag `v5`，标题 `QIDI VIDA 1.2.0-offline-v5`，说明使用 `releases/v5.md`。
5. 给同一草稿附上 APK、`SHA256SUMS.txt`、`update.json`。检查附件名和大小，草稿准备好后再发布。
6. 发布后实际下载 APK，核对哈希；下载 `update.json`，检查其 URL 可以匿名访问且指向同一资产。通过以后才将该版本作为应用更新源。

APK 约 245 MB，必须放 Releases 附件。普通 Git 文件有 100 MiB 限制，不应把 APK 提交到 Git 历史。[GitHub 文档](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

第一版客户端可读取 `https://github.com/OWNER/REPO/releases/latest/download/update.json`。该 URL 只适用于正式 latest release；测试版发布与检查应使用独立、明确的渠道，不依赖 latest 自动包含预发布版。

当前目录只是仓库初始化文件。远程仓库、Release、客户端更新功能分别需要创建、发布和实施验证，文件准备完成不等于这些步骤已经完成。
