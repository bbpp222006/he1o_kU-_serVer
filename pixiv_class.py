from pixivpy3 import *
import os

class Pixiv():
    def __init__(self):
        self.api_init()

    def api_init(self):
        self.pixiv_api = ByPassSniApi()  # Same as AppPixivAPI, but bypass the GFW
        self.pixiv_api.require_appapi_hosts()
        self.pixiv_api.set_accept_language('en-us')
        # self.pixiv_api = AppPixivAPI()  # Same as AppPixivAPI, but bypass the GFW
        self.pixiv_api.auth(refresh_token="ZaomxM51QJOJc447jq8liIBmxl5UtusP1pdFZio3AzI")  #os.environ.get('PIXUSER'), os.environ.get('PIXPASS')
        self.refresh_pixiv_list()
        print('登录成功')
        return "成功更新当日日榜"

    def refresh_pixiv_list(self,date=None,offset = None):
        modes = ['day', 'week', 'month', 'day_male', 'day_female', 'week_original', 'week_rookie', 'day_manga',
                 'day_r18', 'day_male_r18', 'day_female_r18', 'week_r18', 'week_r18g']
        self.pixiv_dic_list = {}
        for mode in modes:
            self.pixiv_dic_list[mode] = self.pixiv_api.illust_ranking(mode=mode, date=date, offset=offset)
        return "成功更新为"+str(date)+"  "+str(offset)+"页"

    def get_with_id(self,illust_id):
        return self.pixiv_api.illust_detail(illust_id)

    def search_with_word(self,word, search_target='partial_match_for_tags', sort='date_desc',offset=None):
        return self.pixiv_api.search_illust(word=word, search_target=search_target, sort=sort, duration=None,offset=offset)

    def get_rank(self,mode="day_male",page=1,date=None):
        if page!=1 and date!=None:
            self.refresh_pixiv_list(page,date)
        return self.pixiv_dic_list[mode]

a=Pixiv()
