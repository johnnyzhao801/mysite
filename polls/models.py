# coding=utf-8

from django.db import models

# Create your models here.
#定义模型类

#图书类
#一类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20) #图书名,CharField说明是一个字符串类型，max_length指定字符串的最大长度为20
    bpub_date = models.DateField() #图书出版日期，DateField说明是一个日期类型

    def __str__(self):
        return self.btitle.encode('utf-8') #返回图书标题
#英雄人物类
#图书类和英雄人物类之间有一对多的关系
    #hname 英雄名
    #hgender 性别
    #hcomment 英雄备注
    #hbook 关系属性 代表英雄属于哪一本图书

#多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20) #英雄名,CharField说明是一个字符串类型，max_length指定字符串的最大长度为20
    hgender = models.BooleanField(default=False) #性别，BooleanField说明是一个bool类型，default指定默认值为False,代表男
    hcomment = models.CharField(max_length=200) #英雄备注
    hbook = models.ForeignKey('BookInfo') #建立BookInfo类和HeroInfo类之间一对多关系

    def __str__(self):
        return self.hname.encode('utf-8')
