from django.db import models

# Create your models here.
#logo管理
class Logo(models.Model): #会在根目录(company)创建upload文件夹，用于存储要上传logo图片
	img=models.FileField(upload_to='./upload')
#网站名称管理
class Webname(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
#首页轮播图
class Ppt(models.Model):
	title=models.CharField(max_length=100)
	img=models.FileField(upload_to='./upload')
	link=models.CharField(max_length=100)
	def __str__(self):
		return self.title
#联系我们
class Contact(models.Model):
	qq=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	addr=models.CharField(max_length=100)
	def __str__(self):
		return self.qq
#文章管理
class News(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField('内容')
	link=models.CharField(max_length=100)
	
	def __str__(self):
		return self.content