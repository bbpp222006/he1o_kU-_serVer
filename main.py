# main.py
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import pixiv_class
from saucenao_api import SauceNao
import base64
from io import BytesIO
import requests


app = FastAPI()
pixiv=pixiv_class.Pixiv()


class Pic_item(BaseModel):
    pic_data: str= None


@app.get("/pixiv")
def hello(type: Optional[str] = Query("rank", regex="^(illust)|(rank)|(search)$"),
    action: Optional[str] = Query(None, regex="^update$"),
    id:Optional[int] = None,
    rank_mode: Optional[str] = Query("week", regex="^(day)|(week)|(month)|(day_male)|(day_female)|(week_original)|(week_rookie)|(day_manga','day_r18)|(day_male_r18)|(day_female_r18)|(week_r18)|(week_r18g)$"),
    rank_page: Optional[int] = 1,
    rank_date: Optional[str] = Query(None, regex="^\d{4}-\d{2}-\d{2}$"),
    search_word: Optional[str] = None,
    search_mode: Optional[str] = Query("partial_match_for_tags", regex="^(partial_match_for_tags)|(exact_match_for_tags)|(title_and_caption)$"),
    search_order: Optional[str] = Query("date_desc", regex="^(date_desc)|(date_asc)$"),
    search_page: Optional[int] = 1):
    if action=="update":
        return_message =pixiv.api_init()
    elif type=="illust":
        return_message=pixiv.get_with_id(id)
    elif type=="search":
        return_message = pixiv.search_with_word(search_word,search_mode,search_order,search_page)
    elif type=="rank":
        return_message = pixiv.get_rank(rank_mode,rank_page,rank_date)
    return {"message":return_message}

@app.post("/saucenao")
def get_saucenao(request_data:Pic_item):
    return_data=[]
    sauce = SauceNao()
    new = base64.b64decode(request_data.pic_data.encode())
    results = sauce.from_file(BytesIO(new))  # or from_file()
    for result in results[:min(3,len(results))]:
        r = requests.get(result.thumbnail)
        preview = str(base64.b64encode(r.content), "utf-8")
        if result.urls:
            url=result.urls[0]
        else:
            url = result.thumbnail
        return_data.append({"preview":preview,"title":result.title,"url":url,"similarity":result.similarity})
    return return_data


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app=app,host="0.0.0.0",port=25621,workers=1)