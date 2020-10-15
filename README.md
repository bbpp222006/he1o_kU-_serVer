# heroku_server
将pixivpy通过fastapi框架部署到heroku上，得到一个免费的pixivapi。

heroku部署时需添加环境变量：pixiv账号和密码，具体请参考源文件里请求的环境变量名称进行设置。

使用方式：克隆本仓库，登录heroku，创建新容器，选择github链接，选择克隆的仓库，进行部署。
部署完成后访问heroku给的地址+/pixiv即可看到效果（默认返回的是当日week日榜）
访问地址+/docs能看到具体的请求参数设置（fastapi自带的一个说明页面）。
