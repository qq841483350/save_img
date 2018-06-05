#coding:utf8
#抓取网页图片下载到本地
import urllib2,re,os,time,sys,urllib
reload(sys)
sys.setdefaultencoding('utf8')
url="http://www.xhj.com/xiaoqu/xiangce/2773.html"   #网站URL地址
html=urllib2.urlopen(url).read()#获取网页源代码
name=re.findall('【(.*?)户型图_长沙.*?房型图_小区照片_相册',html)[0]  #获取小区名称，为了下面建立一个文件夹做准备
list_url=re.findall('data-index="\d+" src="(.*?)" />',html)  #获取所有需要图片URL

cur_path=os.path.abspath(os.curdir)  #获取当前目录
glal_path=cur_path+'\\'+name.encode('gbk')  #当前目录 name名称连接 生成一个 新的路径 比如 ：E:\\python\test\某某小区
os.mkdir(glal_path)   #创建一个文件夹
i=1  #定义一个i=1
for img_url in list_url:
    urllib.urlretrieve(img_url,glal_path+'\\'+'%s.jpg'%str(i))  #保存图片，img_url是图片地址  后面参数是路径与重新命名的图片名称
    i=i+1
