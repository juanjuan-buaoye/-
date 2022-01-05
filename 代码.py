import json
import time
import os
import requests
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map,Timeline,Grid,Bar,Line,Liquid,TreeMap
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.globals import ChartType,SymbolType,ThemeType
from bs4 import BeautifulSoup
def get_html(Url, header):
    try:
        r = requests.get(url=Url, headers=header)
        r.encoding = r.apparent_encoding
        status = r.status_code
        # 将原始数据类型转换为json类型，方便处理
        data_json = json.loads(r.text)
        print(status)
        return data_json
    except:
        print("爬取失败")


# 将提取34个省数据的方法封装为函数
def get_data(data, info_list):
    # 直接提取["id","name","lastUpdateTime"] 的数据
    info = pd.DataFrame(data)[info_list]

    # 获取today的数据
    today_data = pd.DataFrame([province["today"] for province in data])
    # 修改列名
    today_data.columns = ["today_" + i for i in today_data.columns]

    # 获取total的数据
    total_data = pd.DataFrame([province["total"] for province in data])
    # 修改列名
    total_data.columns = ["total_" + i for i in total_data.columns]

    return pd.concat([info, today_data, total_data], axis=1)


def save_data(data, name):
    """定义保存数据的函数"""
    # 保存的文件名名称
    file_name = "" +  name + "_" + time.strftime("%Y_%m_%d", time.localtime(time.time())) + ".csv"
    data.to_csv(file_name, index=None, encoding="utf_8_sig")
    # 检查是否保存成功，并打印提示文本
    if os.path.exists(file_name):
        print("“" + file_name + "”" + "\n保存成功")
    else:
        print('保存失败')


if __name__ == "__main__":
    # 访问网易实时疫情播报平台网址
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"

    # 设置请求头，伪装为浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    """爬取中国各省的疫情数据"""
    # 1.获取数据（此时的数据未经处理）
    datas = get_html(url, headers)

    # 2.找到储存中国34省的数据所在
    data_province = datas["data"]["areaTree"][2]["children"]

    # 3.提取34个省数据
    province = get_data(data_province, ["id", "name", "lastUpdateTime"])

    # 4.保存国内数据
    print("\n\n保存国内34个省份数据")
    save_data(province, "today_province")


def get_html(Url, header):
    try:
        r = requests.get(url=Url, headers=header)
        r.encoding = r.apparent_encoding
        status = r.status_code
        # 将原始数据类型转换为json类型，方便处理
        data_json = json.loads(r.text)
        print(status)
        return data_json
    except:
        print("爬取失败")


# 将提取34个省数据的方法封装为函数
def get_data(data, info_list):
    # 直接提取["id","name","lastUpdateTime"] 的数据
    info = pd.DataFrame(data)[info_list]

    # 获取today的数据
    today_data = pd.DataFrame([province["today"] for province in data])
    # 修改列名
    today_data.columns = ["today_" + i for i in today_data.columns]

    # 获取total的数据
    total_data = pd.DataFrame([province["total"] for province in data])
    # 修改列名
    total_data.columns = ["total_" + i for i in total_data.columns]

    return pd.concat([info, today_data, total_data], axis=1)


def save_data(data, name):
    """定义保存数据的函数"""
    # 保存的文件名名称
    file_name = "" +  name + "_" + time.strftime("%Y_%m_%d", time.localtime(time.time())) + ".csv"
    data.to_csv(file_name, index=None, encoding="utf_8_sig")
    # 检查是否保存成功，并打印提示文本
    if os.path.exists(file_name):
        print("“" + file_name + "”" + "\n保存成功")
    else:
        print('保存失败')


if __name__ == "__main__":
    # 访问网易实时疫情播报平台网址
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"

    # 设置请求头，伪装为浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    """爬取中国各省的疫情数据"""
    # 1.获取数据（此时的数据未经处理）
    datas = get_html(url, headers)

    # 5.找到储存国外的数据所在
    world_data = datas["data"]["areaTree"]
    
    # 6.提取国外的数据
    worlds = get_data(world_data, ["id", "name", "lastUpdateTime"])
    
    # 7.储存国外的数据
    print("\n\n保存国外数据")
    save_data(worlds, "today_worlds")

def get_html(Url, header):
    try:
        r = requests.get(url=Url, headers=header)
        r.encoding = r.apparent_encoding
        status = r.status_code
        # 将原始数据类型转换为json类型，方便处理
        data_json = json.loads(r.text)
        print(status)
        return data_json
    except:
        print("爬取失败")


# 将提取34个省数据的方法封装为函数
def get_data(data, info_list):
    # 直接提取["id","name","lastUpdateTime"] 的数据
    info = pd.DataFrame(data)[info_list]

    # 获取today的数据
    today_data = pd.DataFrame([province["today"] for province in data])
    # 修改列名
    today_data.columns = ["today_" + i for i in today_data.columns]

    # 获取total的数据
    total_data = pd.DataFrame([province["total"] for province in data])
    # 修改列名
    total_data.columns = ["total_" + i for i in total_data.columns]

    return pd.concat([info, today_data, total_data], axis=1)


def save_data(data, name):
    """定义保存数据的函数"""
    # 保存的文件名名称
    file_name = "" + "全国最近两月疫情数据总汇" + ".csv"
    data.to_csv(file_name, index=None, encoding="utf_8_sig")
    # 检查是否保存成功，并打印提示文本
    if os.path.exists(file_name):
        print("“" + file_name + "”" + "\n保存成功")
    else:
        print('保存失败')


if __name__ == "__main__":
    # 访问网易实时疫情播报平台网址
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total"

    # 设置请求头，伪装为浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    """爬取中国各省的疫情数据"""
    # 1.获取数据（此时的数据未经处理）
    datas = get_html(url, headers)

    # 2.找到储存中国34省的数据所在
    data_province = datas["data"]["chinaDayList"]

    # 3.提取34个省数据
    CHI_data = get_data(data_province, ["date"])

    # 4.保存国内数据
    print("\n\n保存国内最近两月疫情数据")
    save_data(CHI_data, "today_province")


translates = pd.read_excel("世界各国中英文国名对照表.xlsx")
name = list(worlds['name'])
English_name = []
null = []
for i in range(len(worlds['name'])):
    for j in range(len(translates['英文'])):
        if worlds['name'][i] == translates['中文'][j]:
            English_name.append(translates['英文'][j])

Extant_patient = list(zip(list(province['name']),list(province['total_confirm'] - province['total_heal'] - province['total_dead'])))
Extant_patients = list(zip(English_name,list(worlds['total_confirm'] - worlds['total_heal'] - worlds['total_dead'])))
LIST1 = [Extant_patient,Extant_patients]
LIST2 = ["国内","全球"]
LIST3 = ["china","world"]
LIST4 = [[{"min": 0, "max": 0, "label": "0"},
          {"min": 1, "max": 9, "label": "1~9"},
          {"min": 10, "max": 99, "label": "10~99"},
          {"min": 100, "max": 999, "label": "100~999"},
          {"min": 1000, "max": 9999, "label": "1000~9999"},
          {"min": 10000, "label": "> 10000"}],  #现存患者
         [{"min": 0, "max": 99, "label": "0~99"},
          {"min": 100, "max": 999, "label": "100~999"},
          {"min": 1000, "max": 9999, "label": "1000~9999"},
          {"min": 10000, "max": 99999, "label": "10000~99999"},
          {"min": 100000, "max": 999999, "label": "100000~999999"},
          {"min": 1000000, "label": "> 1000000"}]]

t = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="825px",height='515px'))
for i in range(2):
    province_map=(
        Map()
        .add('现存确诊',LIST1[i],LIST3[i],is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="{}新冠现存确诊数据可视化".format(LIST2[i])),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(
            range_text=["High","Low"],is_piecewise=True,
            pieces=LIST4[i]),
    )
            )
    t.add(province_map,'{}'.format(LIST2[i]))
t.render('map.html')
t.render_notebook()

l1 = (
    Liquid()
    .add("死亡率", [sum(list(province['total_dead']))/sum(list(province['total_confirm']))],
         color = ['red'],
         center=["70%", "70%"],
         label_opts=opts.LabelOpts(
             font_size=20,
             formatter=JsCode(
                 """function (param)
                 {return '死亡率:' + (Math.floor(param.value * 10000) / 100) + '%';
                }"""
             ),
             position="inside",
         ),
        )
     #.set_global_opts(title_opts=opts.TitleOpts(title="中国新冠肺炎治愈率与死亡率"))
)


l2 = (
    Liquid()
    .add("治愈率",[sum(list(province['total_heal']))/sum(list(province['total_confirm']))],
         color = ['green'],
         center=["30%", "30%"],
         label_opts=opts.LabelOpts(
             font_size=20,
             formatter=JsCode(
                 """function (param)
                 {return '治愈率:' + (Math.floor(param.value * 10000) / 100) + '%';
                }"""
             ),
             position="inside",
         ),
        )
)
grid1 = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="350px",height='350px'))
    .add(l1, grid_opts=opts.GridOpts())
    .add(l2, grid_opts=opts.GridOpts())
)
grid1.render('china_heal_and_dead.html')
grid1.render_notebook()


l1 = (
    Liquid()
    .add("死亡率", [sum(list(worlds['total_dead']))/sum(list(worlds['total_confirm']))],
         color = ['red'],
         center=["30%", "70%"],
         label_opts=opts.LabelOpts(
             font_size=20,
             formatter=JsCode(
                 """function (param)
                 {return '死亡率:' + (Math.floor(param.value * 10000) / 100) + '%';
                }"""
             ),
             position="inside",
         ),
        )
     #.set_global_opts(title_opts=opts.TitleOpts(title="全球新冠肺炎治愈率与死亡率"))
)


l2 = (
    Liquid()
    .add("治愈率",[sum(list(worlds['total_heal']))/sum(list(worlds['total_confirm']))],
         color = ['green'],
         center=["70%", "30%"],
         label_opts=opts.LabelOpts(
             font_size=10,
             formatter=JsCode(
                 """function (param)
                 {
                 return '治愈率:' + (Math.floor(param.value * 10000) / 100) + '%';
                }"""
             ),
             position="inside",
         ),
        )
)
grid1 = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="350px",height='350px'))
    .add(l1, grid_opts=opts.GridOpts())
    .add(l2, grid_opts=opts.GridOpts())
)
grid1.render('worlds_heal_and_dead.html')
grid1.render_notebook()

    
date_CHI = list(CHI_data['date'])
Extant_CHI = list(CHI_data['total_storeConfirm'])
Added_CHI = list(CHI_data['today_confirm'])
suspect_CHI = list(CHI_data['today_suspect'])
input_CHI = list(CHI_data['today_input'])
nums_CHI = [Extant_CHI,Added_CHI,suspect_CHI,input_CHI]
Classification = ['现存确诊','当日新增','新增疑似','新增输入']

line=(
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="375px",height='325px'))
    .add_xaxis(date_CHI)
    .add_yaxis('新增确诊',CHI_data['today_confirm'],is_smooth=True,linestyle_opts=opts.LineStyleOpts(width=2))
    .extend_axis(yaxis=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}"),
                                     is_show=True,name='新增输入'))
    .set_global_opts(
                    yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}"),
                                     is_show=True,name='新增确诊')
                    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    ))

line2=(
    Line()
    .add_xaxis(date_CHI)
    .add_yaxis('新增输入',CHI_data['today_input'],yaxis_index=1,is_smooth=True,
              linestyle_opts=opts.LineStyleOpts(width=2))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
    ))
line.overlap(line2)
line.render('china_ac.html')
line.render_notebook()

t4 = Timeline(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width="800px",height='300px'))
for i in range(4):
    bar=(
    Bar()
    .add_xaxis(date_CHI)
    .add_yaxis(" ",nums_CHI[i],itemstyle_opts=opts.ItemStyleOpts(color='#02ccfe'))
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter='{value}/人'),name="人数"),
        xaxis_opts=opts.AxisOpts(name="日期")
                    )
    .set_series_opts( 
        label_opts=opts.LabelOpts(is_show=False)
))
    line=(
        Line()
        .add_xaxis(date_CHI)
        .add_yaxis(" ",nums_CHI[i],is_smooth=True,
                   label_opts=opts.LabelOpts(is_show=False),
              linestyle_opts=opts.LineStyleOpts(width=4,color='#fa2a55'))
    )
    bar.overlap(line)
    t4.add(bar,'{}'.format(Classification[i]))
t4.render('china_10_12_mouth.html')
t4.render_notebook()

data = []
for i in range(len(worlds['total_confirm'])):
    a = {"value": worlds['total_confirm'][i], "name": "{}".format(worlds['name'][i])}
    data.append(a)
data
[{'value': 372221, 'name': '突尼斯'},
 {'value': 715147, 'name': '塞尔维亚'},
 {'value': 116834, 'name': '中国'},
 {'value': 779532, 'name': '日本本土'},
 {'value': 204595, 'name': '泰国'},
 {'value': 62315, 'name': '新加坡'},
 {'value': 149191, 'name': '韩国'},
 {'value': 30290, 'name': '澳大利亚'},
 {'value': 3725349, 'name': '德国'},
 {'value': 34352185, 'name': '美国'},
 {'value': 667876, 'name': '马来西亚'},
 {'value': 11304, 'name': '越南'},
 {'value': 6, 'name': '圣巴泰勒米'},
 {'value': 176137, 'name': '肯尼亚'},
 {'value': 3049648, 'name': '伊朗'},
 {'value': 839730, 'name': '以色列'},
 {'value': 16, 'name': '毛利亚尼亚'},
 {'value': 542649, 'name': '黎巴嫩'},
 {'value': 358677, 'name': '克罗地亚'},
 {'value': 648849, 'name': '奥地利'},
 {'value': 700978, 'name': '瑞士'},
 {'value': 416195, 'name': '希腊'},
 {'value': 1701, 'name': '毛里求斯'},
 {'value': 130658, 'name': '爱沙尼亚'},
 {'value': 155568, 'name': '北马其顿'},
 {'value': 406861, 'name': '白俄罗斯'},
 {'value': 278072, 'name': '立陶宛'},
 {'value': 335264, 'name': '阿塞拜疆'},
 {'value': 72, 'name': '美属维尔京群岛'},
 {'value': 197, 'name': '蒙古'},
 {'value': 2286767, 'name': '乌克兰'},
 {'value': 2878061, 'name': '波兰'},
 {'value': 204697, 'name': '波黑'},
 {'value': 11, 'name': '蒙特塞拉特'},
 {'value': 1761066, 'name': '南非'},
 {'value': 85, 'name': '布隆迪'},
 {'value': 1755, 'name': '南苏丹'},
 {'value': 30582, 'name': '马耳他'},
 {'value': 255878, 'name': '摩尔多瓦'},
 {'value': 420654, 'name': '保加利亚'},
 {'value': 833291, 'name': '孟加拉'},
 {'value': 1521, 'name': '阿尔巴尼亚'},
 {'value': 311948, 'name': '巴勒斯坦'},
 {'value': 176, 'name': '科摩罗'},
 {'value': 93272, 'name': '阿富汗'},
 {'value': 468175, 'name': '沙特阿拉伯'},
 {'value': 2711, 'name': '新西兰'},
 {'value': 13308, 'name': '塔吉克斯坦'},
 {'value': 313, 'name': '泽西岛'},
 {'value': 177, 'name': '叙利亚'},
 {'value': 389173, 'name': '巴拿马'},
 {'value': 160594, 'name': '古巴'},
 {'value': 167095, 'name': '尼日利亚'},
 {'value': 524475, 'name': '摩洛哥'},
 {'value': 42050, 'name': '塞内加尔'},
 {'value': 19, 'name': '老挝'},
 {'value': 12225, 'name': '巴哈马'},
 {'value': 2282, 'name': '马约特岛'},
 {'value': 256581, 'name': '斯洛文尼亚'},
 {'value': 70466, 'name': '卢森堡'},
 {'value': 267289, 'name': '爱尔兰'},
 {'value': 439374, 'name': '厄瓜多尔'},
 {'value': 1665526, 'name': '捷克'},
 {'value': 807209, 'name': '匈牙利'},
 {'value': 1255, 'name': '法属圭亚那'},
 {'value': 530, 'name': '多哥共和国'},
 {'value': 345312, 'name': '哥斯达黎加'},
 {'value': 250, 'name': '文莱'},
 {'value': 187, 'name': '法罗群岛'},
 {'value': 37, 'name': '马提尼克岛'},
 {'value': 1702174, 'name': '荷兰'},
 {'value': 17533221, 'name': '巴西'},
 {'value': 249118, 'name': '洪都拉斯'},
 {'value': 343615, 'name': '乌拉圭'},
 {'value': 2007477, 'name': '秘鲁'},
 {'value': 1487239, 'name': '智利'},
 {'value': 13, 'name': '格陵兰'},
 {'value': 6, 'name': '圣巴托洛谬岛'},
 {'value': 70897, 'name': '马尔代夫'},
 {'value': 254116, 'name': '委内瑞拉'},
 {'value': 20151, 'name': '毛里塔尼亚'},
 {'value': 31, 'name': '纳米比亚'},
 {'value': 487, 'name': '法属留尼汪岛'},
 {'value': 5536, 'name': '波多黎各'},
 {'value': 94699, 'name': '加纳'},
 {'value': 8662, 'name': '赤道几内亚'},
 {'value': 23398, 'name': '几内亚'},
 {'value': 28912, 'name': '卢旺达'},
 {'value': 23, 'name': '格林纳达'},
 {'value': 18754, 'name': '斯威士兰'},
 {'value': 509, 'name': '坦桑尼亚'},
 {'value': 8140, 'name': '贝宁'},
 {'value': 35918, 'name': '刚果（金）'},
 {'value': 7101, 'name': '中非共和国'},
 {'value': 2575, 'name': '利比里亚'},
 {'value': 14823, 'name': '索马里'},
 {'value': 4449, 'name': '塞拉利昂'},
 {'value': 4943, 'name': '乍得'},
 {'value': 115824, 'name': '赞比亚'},
 {'value': 96, 'name': '巴巴多斯'},
 {'value': 14356, 'name': '马里'},
 {'value': 4172742, 'name': '阿根廷'},
 {'value': 60, 'name': '法属波利尼西亚'},
 {'value': 260334, 'name': '巴林'},
 {'value': 71651, 'name': '莫桑比克'},
 {'value': 80090, 'name': '喀麦隆'},
 {'value': 64521, 'name': '乌干达'},
 {'value': 41, 'name': '厄立特里亚'},
 {'value': 12121, 'name': '刚果（布）'},
 {'value': 40318, 'name': '津巴布韦'},
 {'value': 291139, 'name': '丹麦'},
 {'value': 101, 'name': '阿鲁巴'},
 {'value': 1322, 'name': '斐济'},
 {'value': 12989, 'name': '伯利兹'},
 {'value': 146051, 'name': '缅甸'},
 {'value': 73311, 'name': '塞浦路斯'},
 {'value': 183, 'name': '关岛'},
 {'value': 1326, 'name': '科索沃'},
 {'value': 1, 'name': '圣皮埃尔岛和密克隆岛'},
 {'value': 111990, 'name': '吉尔吉斯斯坦'},
 {'value': 60, 'name': '博茨瓦纳'},
 {'value': 5452, 'name': '尼日尔'},
 {'value': 18825, 'name': '苏里南'},
 {'value': 31704, 'name': '佛得角'},
 {'value': 76297, 'name': '萨尔瓦多'},
 {'value': 159, 'name': '圭亚那'},
 {'value': 7696, 'name': '尼加拉瓜'},
 {'value': 28, 'name': '冈比亚'},
 {'value': 24, 'name': '东帝汶'},
 {'value': 944065, 'name': '巴基斯坦'},
 {'value': 274404, 'name': '埃及'},
 {'value': 331013, 'name': '科威特'},
 {'value': 391149, 'name': '斯洛伐克'},
 {'value': 176, 'name': '直布罗陀'},
 {'value': 99, 'name': '摩纳哥'},
 {'value': 396149, 'name': '巴拉圭'},
 {'value': 22, 'name': '荷属安的列斯'},
 {'value': 18, 'name': '多米尼克'},
 {'value': 104463, 'name': '乌兹别克斯坦'},
 {'value': 99988, 'name': '黑山'},
 {'value': 273730, 'name': '危地马拉'},
 {'value': 24755, 'name': '加蓬'},
 {'value': 36304, 'name': '苏丹'},
 {'value': 189555, 'name': '利比亚'},
 {'value': 77, 'name': '圣马丁岛'},
 {'value': 5342028, 'name': '土耳其'},
 {'value': 8, 'name': '巴布亚新几内亚'},
 {'value': 310391, 'name': '多米尼加'},
 {'value': 744377, 'name': '约旦'},
 {'value': 223904, 'name': '亚美尼亚'},
 {'value': 15, 'name': '圣基茨和尼维斯'},
 {'value': 171, 'name': '瓜德罗普'},
 {'value': 1263, 'name': '安提瓜和巴布达'},
 {'value': 411677, 'name': '玻利维亚'},
 {'value': 3802052, 'name': '哥伦比亚'},
 {'value': 27, 'name': '圣文森特和格林纳丁斯'},
 {'value': 19, 'name': '圣卢西亚'},
 {'value': 5806256, 'name': '法国'},
 {'value': 601950, 'name': '阿联酋'},
 {'value': 1411652, 'name': '加拿大'},
 {'value': 29633105, 'name': '印度'},
 {'value': 4596994, 'name': '英国'},
 {'value': 4247032, 'name': '意大利'},
 {'value': 5189260, 'name': '俄罗斯'},
 {'value': 1332832, 'name': '菲律宾'},
 {'value': 94026, 'name': '芬兰'},
 {'value': 612202, 'name': '尼泊尔'},
 {'value': 859045, 'name': '葡萄牙'},
 {'value': 6864, 'name': '也门'},
 {'value': 11, 'name': '塞舌尔'},
 {'value': 3745199, 'name': '西班牙'},
 {'value': 228256, 'name': '斯里兰卡'},
 {'value': 134115, 'name': '阿尔及利亚'},
 {'value': 40157, 'name': '柬埔寨'},
 {'value': 16662, 'name': '海地'},
 {'value': 1084636, 'name': '瑞典'},
 {'value': 123, 'name': '特里尼达和多巴哥'},
 {'value': 11575, 'name': '吉布提'},
 {'value': 659, 'name': '圣多美与普林西比'},
 {'value': 13459, 'name': '布基纳法索'},
 {'value': 1077087, 'name': '比利时'},
 {'value': 1264301, 'name': '伊拉克'},
 {'value': 34588, 'name': '马拉维'},
 {'value': 6555, 'name': '冰岛'},
 {'value': 3809, 'name': '几内亚比绍'},
 {'value': 136403, 'name': '拉脱维亚'},
 {'value': 66, 'name': '不丹'},
 {'value': 128499, 'name': '挪威'},
 {'value': 1937652, 'name': '印度尼西亚'},
 {'value': 36921, 'name': '安哥拉'},
 {'value': 187, 'name': '开曼群岛'},
 {'value': 274480, 'name': '埃塞俄比亚'},
 {'value': 12, 'name': '梵蒂冈'},
 {'value': 47909, 'name': '科特迪瓦'},
 {'value': 220033, 'name': '卡塔尔'},
 {'value': 4, 'name': '莱索托'},
 {'value': 356179, 'name': '格鲁吉亚'},
 {'value': 2459601, 'name': '墨西哥'},
 {'value': 5090, 'name': '圣马力诺'},
 {'value': 460340, 'name': '哈萨克斯坦'},
 {'value': 13828, 'name': '安道尔'},
 {'value': 49379, 'name': '牙买加'},
 {'value': 252, 'name': '格恩西岛'},
 {'value': 1079879, 'name': '罗马尼亚'},
 {'value': 238566, 'name': '阿曼'},
 {'value': 82, 'name': '列支敦士登'},
 {'value': 41966, 'name': '马达加斯加'}]



data = [
 {'value': 372221, 'name': '突尼斯'},
 {'value': 715147, 'name': '塞尔维亚'},
 {'value': 116665, 'name': '中国'},
 {'value': 777978, 'name': '日本本土'},
 {'value': 202264, 'name': '泰国'},
 {'value': 62315, 'name': '新加坡'},
 {'value': 148647, 'name': '韩国'},
 {'value': 30282, 'name': '澳大利亚'},
 {'value': 3725383, 'name': '德国'},
 {'value': 34348925, 'name': '美国'},
 {'value': 667876, 'name': '马来西亚'},
 {'value': 11002, 'name': '越南'},
 {'value': 6, 'name': '圣巴泰勒米'},
 {'value': 176137, 'name': '肯尼亚'},
 {'value': 3049648, 'name': '伊朗'},
 {'value': 839701, 'name': '以色列'},
 {'value': 16, 'name': '毛利亚尼亚'},
 {'value': 542649, 'name': '黎巴嫩'},
 {'value': 358677, 'name': '克罗地亚'},
 {'value': 648849, 'name': '奥地利'},
 {'value': 700978, 'name': '瑞士'},
 {'value': 416195, 'name': '希腊'},
 {'value': 1701, 'name': '毛里求斯'},
 {'value': 130599, 'name': '爱沙尼亚'},
 {'value': 155568, 'name': '北马其顿'},
 {'value': 406861, 'name': '白俄罗斯'},
 {'value': 277942, 'name': '立陶宛'},
 {'value': 335264, 'name': '阿塞拜疆'},
 {'value': 72, 'name': '美属维尔京群岛'},
 {'value': 197, 'name': '蒙古'},
 {'value': 2285534, 'name': '乌克兰'},
 {'value': 2877819, 'name': '波兰'},
 {'value': 204697, 'name': '波黑'},
 {'value': 11, 'name': '蒙特塞拉特'},
 {'value': 1761066, 'name': '南非'},
 {'value': 85, 'name': '布隆迪'},
 {'value': 1755, 'name': '南苏丹'},
 {'value': 30582, 'name': '马耳他'},
 {'value': 255878, 'name': '摩尔多瓦'},
 {'value': 420654, 'name': '保加利亚'},
 {'value': 833291, 'name': '孟加拉'},
 {'value': 1521, 'name': '阿尔巴尼亚'},
 {'value': 311690, 'name': '巴勒斯坦'},
 {'value': 176, 'name': '科摩罗'},
 {'value': 93272, 'name': '阿富汗'},
 {'value': 468175, 'name': '沙特阿拉伯'},
 {'value': 2709, 'name': '新西兰'},
 {'value': 13308, 'name': '塔吉克斯坦'},
 {'value': 313, 'name': '泽西岛'},
 {'value': 177, 'name': '叙利亚'},
 {'value': 388325, 'name': '巴拿马'},
 {'value': 160594, 'name': '古巴'},
 {'value': 167078, 'name': '尼日利亚'},
 {'value': 524475, 'name': '摩洛哥'},
 {'value': 42050, 'name': '塞内加尔'},
 {'value': 19, 'name': '老挝'},
 {'value': 12225, 'name': '巴哈马'},
 {'value': 2282, 'name': '马约特岛'},
 {'value': 256581, 'name': '斯洛文尼亚'},
 {'value': 70466, 'name': '卢森堡'},
 {'value': 267289, 'name': '爱尔兰'},
 {'value': 439374, 'name': '厄瓜多尔'},
 {'value': 1665327, 'name': '捷克'},
 {'value': 807102, 'name': '匈牙利'},
 {'value': 1255, 'name': '法属圭亚那'},
 {'value': 530, 'name': '多哥共和国'},
 {'value': 343604, 'name': '哥斯达黎加'},
 {'value': 248, 'name': '文莱'},
 {'value': 187, 'name': '法罗群岛'},
 {'value': 37, 'name': '马提尼克岛'},
 {'value': 1702156, 'name': '荷兰'},
 {'value': 17533221, 'name': '巴西'},
 {'value': 248115, 'name': '洪都拉斯'},
 {'value': 343615, 'name': '乌拉圭'},
 {'value': 2004252, 'name': '秘鲁'},
 {'value': 1487239, 'name': '智利'},
 {'value': 13, 'name': '格陵兰'},
 {'value': 6, 'name': '圣巴托洛谬岛'},
 {'value': 70897, 'name': '马尔代夫'},
 {'value': 252883, 'name': '委内瑞拉'},
 {'value': 20109, 'name': '毛里塔尼亚'},
 {'value': 31, 'name': '纳米比亚'},
 {'value': 487, 'name': '法属留尼汪岛'},
 {'value': 5536, 'name': '波多黎各'},
 {'value': 94493, 'name': '加纳'},
 {'value': 8662, 'name': '赤道几内亚'},
 {'value': 23398, 'name': '几内亚'},
 {'value': 28912, 'name': '卢旺达'},
 {'value': 23, 'name': '格林纳达'},
 {'value': 18754, 'name': '斯威士兰'},
 {'value': 509, 'name': '坦桑尼亚'},
 {'value': 8109, 'name': '贝宁'},
 {'value': 35918, 'name': '刚果（金）'},
 {'value': 7101, 'name': '中非共和国'},
 {'value': 2575, 'name': '利比里亚'},
 {'value': 14817, 'name': '索马里'},
 {'value': 4449, 'name': '塞拉利昂'},
 {'value': 4943, 'name': '乍得'},
 {'value': 115824, 'name': '赞比亚'},
 {'value': 96, 'name': '巴巴多斯'},
 {'value': 14356, 'name': '马里'},
 {'value': 4172742, 'name': '阿根廷'},
 {'value': 60, 'name': '法属波利尼西亚'},
 {'value': 260334, 'name': '巴林'},
 {'value': 71651, 'name': '莫桑比克'},
 {'value': 80090, 'name': '喀麦隆'},
 {'value': 64521, 'name': '乌干达'},
 {'value': 41, 'name': '厄立特里亚'},
 {'value': 12121, 'name': '刚果（布）'},
 {'value': 40318, 'name': '津巴布韦'},
 {'value': 291139, 'name': '丹麦'},
 {'value': 101, 'name': '阿鲁巴'},
 {'value': 1206, 'name': '斐济'},
 {'value': 12971, 'name': '伯利兹'},
 {'value': 146051, 'name': '缅甸'},
 {'value': 73247, 'name': '塞浦路斯'},
 {'value': 183, 'name': '关岛'},
 {'value': 1326, 'name': '科索沃'},
 {'value': 1, 'name': '圣皮埃尔岛和密克隆岛'},
 {'value': 111343, 'name': '吉尔吉斯斯坦'},
 {'value': 60, 'name': '博茨瓦纳'},
 {'value': 5452, 'name': '尼日尔'},
 {'value': 18599, 'name': '苏里南'},
 {'value': 31704, 'name': '佛得角'},
 {'value': 75351, 'name': '萨尔瓦多'},
 {'value': 159, 'name': '圭亚那'},
 {'value': 7662, 'name': '尼加拉瓜'},
 {'value': 28, 'name': '冈比亚'},
 {'value': 24, 'name': '东帝汶'},
 {'value': 943027, 'name': '巴基斯坦'},
 {'value': 273795, 'name': '埃及'},
 {'value': 331013, 'name': '科威特'},
 {'value': 391087, 'name': '斯洛伐克'},
 {'value': 176, 'name': '直布罗陀'},
 {'value': 99, 'name': '摩纳哥'},
 {'value': 393482, 'name': '巴拉圭'},
 {'value': 22, 'name': '荷属安的列斯'},
 {'value': 18, 'name': '多米尼克'},
 {'value': 104113, 'name': '乌兹别克斯坦'},
 {'value': 99988, 'name': '黑山'},
 {'value': 273730, 'name': '危地马拉'},
 {'value': 24755, 'name': '加蓬'},
 {'value': 36304, 'name': '苏丹'},
 {'value': 189555, 'name': '利比亚'},
 {'value': 77, 'name': '圣马丁岛'},
 {'value': 5342028, 'name': '土耳其'},
 {'value': 8, 'name': '巴布亚新几内亚'},
 {'value': 309477, 'name': '多米尼加'},
 {'value': 744377, 'name': '约旦'},
 {'value': 223805, 'name': '亚美尼亚'},
 {'value': 15, 'name': '圣基茨和尼维斯'},
 {'value': 171, 'name': '瓜德罗普'},
 {'value': 1263, 'name': '安提瓜和巴布达'},
 {'value': 409106, 'name': '玻利维亚'},
 {'value': 3777600, 'name': '哥伦比亚'},
 {'value': 27, 'name': '圣文森特和格林纳丁斯'},
 {'value': 19, 'name': '圣卢西亚'},
 {'value': 5806247, 'name': '法国'},
 {'value': 601950, 'name': '阿联酋'},
 {'value': 1411531, 'name': '加拿大'},
 {'value': 29570881, 'name': '印度'},
 {'value': 4596987, 'name': '英国'},
 {'value': 4247032, 'name': '意大利'},
 {'value': 5176051, 'name': '俄罗斯'},
 {'value': 1327431, 'name': '菲律宾'},
 {'value': 93923, 'name': '芬兰'},
 {'value': 612202, 'name': '尼泊尔'},
 {'value': 859045, 'name': '葡萄牙'},
 {'value': 6864, 'name': '也门'},
 {'value': 11, 'name': '塞舌尔'},
 {'value': 3745199, 'name': '西班牙'},
 {'value': 227765, 'name': '斯里兰卡'},
 {'value': 134115, 'name': '阿尔及利亚'},
 {'value': 39464, 'name': '柬埔寨'},
 {'value': 16662, 'name': '海地'},
 {'value': 1084636, 'name': '瑞典'},
 {'value': 123, 'name': '特里尼达和多巴哥'},
 {'value': 11575, 'name': '吉布提'},
 {'value': 659, 'name': '圣多美与普林西比'},
 {'value': 13459, 'name': '布基纳法索'},
 {'value': 1076579, 'name': '比利时'},
 {'value': 1264301, 'name': '伊拉克'},
 {'value': 34588, 'name': '马拉维'},
 {'value': 6555, 'name': '冰岛'},
 {'value': 3803, 'name': '几内亚比绍'},
 {'value': 136247, 'name': '拉脱维亚'},
 {'value': 66, 'name': '不丹'},
 {'value': 128499, 'name': '挪威'},
 {'value': 1927708, 'name': '印度尼西亚'},
 {'value': 36790, 'name': '安哥拉'},
 {'value': 187, 'name': '开曼群岛'},
 {'value': 274480, 'name': '埃塞俄比亚'},
 {'value': 12, 'name': '梵蒂冈'},
 {'value': 47760, 'name': '科特迪瓦'},
 {'value': 220033, 'name': '卡塔尔'},
 {'value': 4, 'name': '莱索托'},
 {'value': 355368, 'name': '格鲁吉亚'},
 {'value': 2455351, 'name': '墨西哥'},
 {'value': 5090, 'name': '圣马力诺'},
 {'value': 459212, 'name': '哈萨克斯坦'},
 {'value': 13828, 'name': '安道尔'},
 {'value': 49379, 'name': '牙买加'},
 {'value': 252, 'name': '格恩西岛'},
 {'value': 1079879, 'name': '罗马尼亚'},
 {'value': 238566, 'name': '阿曼'},
 {'value': 82, 'name': '列支敦士登'},
 {'value': 41966, 'name': '马达加斯加'}]

c = (
    TreeMap(init_opts=opts.InitOpts(theme=ThemeType.DARK,width="375px",height='325px'))
    .add("累计确诊", data)
)

c.render('worlds_ac.html')
c.render_notebook()
