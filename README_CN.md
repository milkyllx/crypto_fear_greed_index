# Fear and Greed Index 项目安装和运行文档

以下文档将指导您如何安装和运行该项目。该项目旨在从外部API获取恐惧与贪婪指数数据，并将其存储到本地数据库中，同时支持定时任务定期更新数据。

---

## 环境要求

1. **操作系统**：支持 Windows、Linux 或 macOS。
2. **Python版本**：建议使用 Python 3.8 或更高版本。
3. **数据库**：MySQL 5.7 或更高版本。
4. **网络访问**：需要能够访问 `https://api.alternative.me/fng/`。

---

## 安装步骤

### 1. 克隆项目
使用以下命令将项目代码克隆到本地：
```bash
git clone <项目仓库地址>
cd <项目目录>
```

### 2. 创建虚拟环境
建议使用虚拟环境管理依赖项：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. 安装依赖项
使用 `pip` 安装项目所需的依赖项：
```bash
pip install -r requirements.txt
```

**注意**：如果项目中没有 `requirements.txt` 文件，请手动安装以下依赖项：
```bash
pip install pymysql requests apscheduler
```

### 4. 配置数据库
#### 4.1 创建数据库
使用以下命令在 MySQL 中创建数据库：
```sql
CREATE DATABASE crypto_follow CHARACTER SET utf8 COLLATE utf8_general_ci;
```

#### 4.2 创建数据表
运行以下 SQL 脚本以创建数据表：
```sql
CREATE TABLE `index_fear_greed` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(10) NOT NULL,
  `value_classification` varchar(50) NOT NULL,
  `timestamp` bigint(20) NOT NULL,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `timestamp` (`timestamp`)
);
```

#### 4.3 配置数据库连接
编辑项目中的 `db_utils.py` 文件，确保 `DB_CONFIG` 配置正确：
```python
DB_CONFIG = {
    'host': 'localhost',          # 数据库地址
    'user': 'root',               # 数据库用户名
    'password': 'juxue654321A!',  # 数据库密码
    'database': 'crypto_follow',  # 数据库名称
    'charset': 'utf8'             # 字符集
}
```

---

## 运行项目

### 1. 手动运行一次数据抓取
运行以下命令手动抓取数据并存储到数据库：
```bash
python main.py
```

### 2. 启动定时任务
项目默认每小时抓取一次数据并存储到数据库。运行以下命令启动定时任务：
```bash
python main.py
```

定时任务启动后，您将看到以下日志信息：
```
Scheduler has started. The task will run every hour.
```

---

## 项目结构说明

- **db.txt**：包含数据库表结构定义。
- **db_utils.py**：数据库操作工具，用于连接数据库和保存数据。
- **fetch_utils.py**：数据抓取工具，用于从外部API获取恐惧与贪婪指数数据。
- **main.py**：项目主入口，包含定时任务逻辑和手动运行逻辑。

---

## 常见问题

### 1. 数据库连接失败
**解决方法**：
- 确保 MySQL 服务已启动。
- 检查 `db_utils.py` 中的 `DB_CONFIG` 配置是否正确。
- 确保用户具有对 `crypto_follow` 数据库的访问权限。

### 2. 数据抓取失败
**解决方法**：
- 检查网络连接是否正常。
- 检查 `https://api.alternative.me/fng/` 是否可访问。

### 3. 定时任务未运行
**解决方法**：
- 检查日志输出是否有错误信息。
- 确保您没有关闭运行脚本的终端。

---

## 结束语

通过以上步骤，您应该能够成功安装和运行该项目。如果您遇到问题，请随时联系开发者或提交问题到项目的 GitHub 仓库。
