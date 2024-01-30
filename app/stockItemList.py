# app/stockItemList.py

from bs4 import BeautifulSoup
import requests

def stock_item_list(action_type="default"):
    r = requests.get('https://isin.twse.com.tw/isin/C_public.jsp?strMode=2')
    job_date = ""

    if(r.status_code == requests.codes.ok):
        soup = BeautifulSoup(r.text, 'html.parser')
        headers = soup.findAll('font',  {"class": "h1"})
        stock_record_list = []
        
        for header in headers:
            heat_str = header.getText()
            if(":" in heat_str):
                job_date = heat_str.split(":")[1].strip()
        
        stock_table = soup.findAll('table',  {"class": "h4"})
        stock_table_records  = stock_table[0].findAll('tr')
        
        stock_type = ""
        for stock_record in stock_table_records:
            stock_record_attr = stock_record.findAll("td")
            stock_obj_json={}
            
            if(len(stock_record_attr) == 1):
                stock_type =stock_record_attr[0].getText()
            elif (stock_record_attr[0].has_attr('bgcolor') and stock_record_attr[0]['bgcolor'] == '#FAFAD2'):
                stock_obj_json["stock_no"] = stock_record_attr[0].getText().split("　")[0].strip()
                stock_obj_json["name"] =  stock_record_attr[0].getText().split("　")[1].strip()
                stock_obj_json["isin_code"] = stock_record_attr[1].getText()
                stock_obj_json["puhlished_date"] = stock_record_attr[2].getText()
                stock_obj_json["market_type"] = stock_record_attr[3].getText()
                stock_obj_json["industry＿type"] = stock_record_attr[4].getText()
                stock_obj_json["cfi_code"] = stock_record_attr[5].getText()
                stock_obj_json["note"] = stock_record_attr[6].getText()
                stock_obj_json["stock_type"] = stock_type.strip()
                if(action_type=="init"):
                    stock_record_list.append(stock_obj_json)
                elif(action_type=="default" and job_date == stock_obj_json["puhlished_date"]):
                    stock_record_list.append(stock_obj_json)
        
        
    
    return job_date , stock_record_list

