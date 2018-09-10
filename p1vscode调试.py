import re
from urllib import request

#Beautiful soup, Scrapy 两个爬虫框架可以借鉴
#断点调试
#爬虫，反爬虫，反反爬虫
#爬回来的数据怎么用，怎么分析，才是重要意义
#频繁爬虫会被封，可以找代理ip库，封只会根据ip封
class Spider():
#    url = "https://www.panda.tv/cate/lol"
    url = "https://www.panda.tv/cate/kingglory"
    #url = "https://www.panda.tv/cate/hearthstone"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'
    def __fetch_content(self): #私有方法
        '''
        '''
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        #print(htmls)
        return htmls

    def __analysis(self,htmls):
        '''
        '''
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor : {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
            }
        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall("\d*",anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank' + str(rank + 1)
            + ' : ' + anchors[rank]['name'] 
            + '   ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)
spider = Spider()
spider.go()





