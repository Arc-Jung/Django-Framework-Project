{"filter":false,"title":"models.py","tooltip":"/testserver/testapp1/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":67,"column":29},"action":"insert","lines":["#-*- coding: utf-8 -*- ","# 한글을 사용하면 위에 꼭 써야함","from django.db import models","from django.contrib.auth.models import User","from django.utils import timezone # DB 시간설정 ","from datetime import date # DB 시간 설정","","class UserModel(models.Model):","    UserId = models.CharField(primary_key=True, max_length=20) # AutoField","    Password = models.CharField(max_length=20)","    UserNameSet = models.CharField(max_length=20)","    Phone = models.CharField(max_length=20)","    KakaoId = models.CharField(max_length=20)","    Email = models.CharField(max_length=50)","    ","    def __str__(self):","        return self.UserId","        ","class ProductModel(models.Model):","    ProductId = models.CharField(primary_key=True,max_length=20)","    ProductName = models.CharField(max_length=50)","    ProductCategory = models.CharField(max_length=20)","    ProductPrice = models.CharField(max_length=20)","    ProductDate = models.DateTimeField(default=date.today, null=True, blank=True)","    ProductText = models.CharField(max_length=3000) # Long Text","    ProductType = models.CharField(max_length=20)","    UserId = models.CharField(max_length=20) # 외래키","    ","    def __str__(self):","        return self.ProductName","","class LikeModel(models.Model):","    Like = models.AutoField(primary_key=True)","    UserId = models.CharField(max_length=20) # 외래키","    ProductId = models.CharField(max_length=20) # 외래키","","class SaleModel(models.Model):","    SaleId = models.CharField(primary_key=True, max_length=20)","    SaleDate = models.DateTimeField(default=date.today, null=True, blank=True)","    #ProductId = models.CharField(max_length=20) # 외래키","    ","    def __str__(self):","        return self.SaleId    ","    ","class UserImageModel(models.Model):","    #NullFiled = models.CharField(max_length=20)","    UserId = models.CharField(primary_key=True, max_length=20) # 외래키","    ImageId = models.CharField(max_length=20) # 외래키","    ","    def __str__(self):","        return self.NullFiled    ","    ","class ProImageModel(models.Model):","    #NullFiled = models.CharField(max_length=20)","    ProductId = models.CharField(primary_key=True, max_length=20) # 외래키","    ImageId = models.CharField(max_length=20) # 외래키","    ","    def __str__(self):","        return self.NullFiled","    ","class ImageModel(models.Model):","    ImageId = models.CharField(primary_key=True, max_length=20)","    ImageName = models.CharField(max_length=3000) # Long Text","    ImageSize = models.CharField(max_length=3000) # Long Text","    ImageLink = models.CharField(max_length=3000) # Long Text","","    def __str__(self):","        return self.ImageName"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":58,"column":29},"end":{"row":58,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1571666706361,"hash":"19503e7e016f370aed8c19e232acacf14a7536e4"}