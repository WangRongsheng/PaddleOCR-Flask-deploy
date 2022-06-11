> 服务已开启，请根据具体需求进行使用

## PaddleOCR服务请求示例

请求方法：`POST`、`GET`

请求URL： `http://IP:8090/ocr`

请求参数说明：

| 参数 | 值                                                   |
| ---- | ---------------------------------------------------- |
| file | 图像数据，`base64`编码，支持`JPG`、`PNG`、`JPEG`格式 |

返回参数说明：

| 参数     | 值                                       |
| -------- | ---------------------------------------- |
| 服务状态 | `success`：成功识别；`faild`：无法识别； |
| 识别结果 | 列表格式，包含从图片中识别的所有文字信息 |
| 识别时间 | 模型识别文字消耗时间                     |

代码请求示例：

```python
import requests
import json

url = 'http://IP:8090/ocr'
files = {'file': open('./demo.jpg', 'rb')}
r = requests.post(url, files=files)
print(r.text)
```



