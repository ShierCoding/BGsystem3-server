# BGsystem3-server

BGsystem 是一个在电脑桌面显示课表、值日表等信息的工具。本仓库为该项目的前端代码。

## 技术栈

- [FastAPI](https://fastapi.tiangolo.com/)：服务器框架
- [Invoke](https://www.pyinvoke.org/)：命令行工具

## 开发

在正式使用前请确保在`../BGsystem3-frontend`下已克隆了`BGsystem3-frontend`。

### 安装依赖

```sh
pip install -r requirements.txt
```

### 打包前端代码

运行前请确保在`../BGsystem3-frontend`下依赖已全部安装。

```sh
inv build
```

### 根据配置文件启动服务器

```sh
inv start
```

### 启动开发服务器

```sh
inv dev
```

### 启动生产服务器

```sh
inv prod
```

## 使用

### 配置

`./config.toml`：

+ `default`：默认配置（默认值：`default.json`）
+ `host`：主机（默认值：`localhost`）
+ `port`：端口（默认值：`21233`）
+ `mode`：模式（默认值：`development`）

### 模式

在`development`模式下，当检测到`*.py`和`*.toml`文件变动时服务器会自动重载。

在`production`模式下，服务器不会检测任何文件变化或重载。

## TODO

+ 还没想好