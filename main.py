# main.py
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import pixiv_class


app = FastAPI()
pixiv=pixiv_class.Pixiv()

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

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app=app,host="0.0.0.0",port=25621,workers=1)