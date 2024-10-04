# 导入falsk框架、jsonify处理json格式
from flask import Flask, jsonify

# 跨域，解决浏览器同源策略，不同协议，不同域名，不同端口，不能通讯的问题
from flask_cors import CORS

