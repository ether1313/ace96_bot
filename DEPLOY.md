# Fly.io 部署指南

## 前置要求

1. 安装 [Fly CLI](https://fly.io/docs/getting-started/installing-flyctl/)
2. 注册 [Fly.io 账号](https://fly.io/)
3. 登录 Fly.io: `fly auth login`

## 部署步骤

### 1. 初始化 Fly.io 应用（如果还没有）

```bash
cd /Users/choward/Desktop/TELEGRAM\ BOT/ace96_bot
fly launch
```

如果提示是否使用现有的 `fly.toml`，选择 `Yes`。

### 2. 创建数据持久化 Volume

为了保存用户数据和管理员信息，需要创建一个 volume：

```bash
# 创建 volume（只需要执行一次）
fly volumes create ace96_bot_data --size 1 --region sin
```

**注意：** 
- `--size 1` 表示 1GB 存储空间（足够存储大量用户数据）
- `--region sin` 必须与 `fly.toml` 中的 `primary_region` 一致
- 如果 volume 已存在，会提示错误，可以忽略

### 3. 设置环境变量

设置 Telegram Bot Token 和其他配置：

```bash
# 设置 Bot Token（必需）
fly secrets set BOT_TOKEN="你的bot_token"

# 设置 Telegram Channel（可选）
fly secrets set TELEGRAM_CHANNEL="https://t.me/your_channel"

# 设置 URLs（可选）
fly secrets set FREE_SPIN_URL="https://ace96au.com/RFACE96AUBOT9"
fly secrets set FREE_CREDIT_URL="https://ace96au.com/RFACE96AUBOT9"
```

### 4. 部署应用

```bash
fly deploy
```

### 5. 查看日志

```bash
# 实时查看日志
fly logs

# 查看最近的日志
fly logs --tail 100
```

### 6. 检查应用状态

```bash
# 查看应用信息
fly status

# 查看应用详情
fly info
```

## 常用命令

```bash
# 重启应用
fly apps restart ace96-bot

# 查看应用配置
fly config show

# SSH 连接到容器（调试用）
fly ssh console

# 查看应用监控
fly dashboard
```

## 注意事项

1. **数据持久化**: `user_stats.json` 和 `admins.json` 文件现在保存在 Fly.io volume (`/data`) 中，数据会持久化保存，不会因为容器重启而丢失。

2. **环境变量**: 所有敏感信息（如 BOT_TOKEN）应该通过 `fly secrets set` 设置，不要提交到代码仓库。

3. **区域选择**: 在 `fly.toml` 中的 `primary_region` 可以改为你需要的区域（如 `sin` 新加坡、`hkg` 香港、`nrt` 东京等）。

4. **监控**: 使用 `fly logs` 监控 bot 运行状态，确保 bot 正常运行。

## 故障排查

如果 bot 无法启动：

1. 检查日志: `fly logs`
2. 检查环境变量: `fly secrets list`
3. 检查应用状态: `fly status`
4. SSH 进入容器检查: `fly ssh console`

## 更新部署

修改代码后，重新部署：

```bash
fly deploy
```
