# cookiecutter-flask-sugar

基于flask-sugar flask-seek的项目模板

- vscode 配置

```json
{
    "python.analysis.diagnosticMode": "workspace",
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": true,
    }
}
```

- 启动
```shell
pip install cookiecutter
cookiecutter https://github.com/ShangSky/cookiecutter-flask-sugar.git
pip install -r requirements.txt
export PYTHONPATH=$PWD
python main.py
curl http://127.0.0.1:5000/ping
```

- 创建表工具

```shell
python cmd/db_cli --help
```

- 格式化代码

```
sh cmd/code_format.sh
```