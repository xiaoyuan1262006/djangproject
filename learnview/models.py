from django.db import models
#管理器是模型类的属性  其作用是用来操作模型类和数据库的持久化
class BookInfoManager(models.Manager):
    def get_query_set(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete = False)
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread  = 0
        b.bcommet =0
        b.isDelete = False
        return b


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date =models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet =models.IntegerField(null=False,default=0)
    isDelete =models.BooleanField(default=False)
    #元数据元选项
    class Meta:
        db_table='bookinfo'
    bookInfo = BookInfoManager()

    # objects 自定义管理器
    # 管理器是模型类的属性，用于将模型类和数据表进行映射
    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread  = 0
        b.bcommet =0
        b.isDelete = False
        return b


#F 对象内的一个列和另一个列进行比较的时候要用F对象
#Q 对象内的多个列进行逻辑或计算时要用Q对象
    def __str__(self):
        return self.btitle



class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    hbooke = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

class  AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    aparent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

