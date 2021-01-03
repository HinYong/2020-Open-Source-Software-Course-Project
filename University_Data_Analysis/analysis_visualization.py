import pandas as pd
from pyecharts.charts import Bar, Pie, Geo, Liquid, Page
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType, SymbolType

# csv文件处理
df = pd.read_csv("college_data.csv")  # 读取csv文件
df_new = df.drop_duplicates(subset=['name'])  # 去除重复项
df_site = df_new[df_new['site'] != '——']
df_site = df_site[df_site['site'] != '------']

# 数据处理
# 高校总数量分析
site_counts = df_site['site'].value_counts()  # 计算一个城市出现的频率
dict_site = {'name': site_counts.index, 'counts': site_counts.values}
data = pd.DataFrame(dict_site)

# 高校质量分析 211 985 综合
df_title = df_new[df_new['title'] != '——']
df_985 = df_title[df_title['title'] == '211985']
site_counts_985 = df_985['site'].value_counts()
dict_site_985 = {'name': site_counts_985.index, 'counts': site_counts_985.values}
data_985 = pd.DataFrame(dict_site_985)
sum_985_counts = data_985['counts'].sum()
data_985['rate'] = data_985['counts'].apply(lambda x: x / sum_985_counts)

df_211 = df_title[df_title['title'] == '211']
site_counts_211 = df_211['site'].value_counts()
dict_site_211 = {'name': site_counts_211.index, 'counts': site_counts_211.values}
data_211 = pd.DataFrame(dict_site_211)
sum_211_counts = data_211['counts'].sum()
data_211['rate'] = data_211['counts'].apply(lambda x: x / sum_211_counts)

df_985_211 = pd.concat([df_211, df_985], ignore_index=True)
site_counts_985_211 = df_985_211['site'].value_counts()
dict_site_985_211 = {'name': site_counts_985_211.index, 'counts': site_counts_985_211.values}
data_985_211 = pd.DataFrame(dict_site_985_211)
sum_985_211_counts = data_985_211['counts'].sum()
data_985_211['rate'] = data_985_211['counts'].apply(lambda x: x / sum_985_211_counts)


# 柱状图页面
page = Page()
# 各地区高校数量柱状图
bar = Bar()
bar.add_xaxis(data['name'].values.tolist())
bar.add_yaxis("", data['counts'].values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    title_opts=opts.TitleOpts(title="各地区高校数量"),
    datazoom_opts=opts.DataZoomOpts()
)
bar.set_series_opts(itemstyle_opts={
    "normal": {
        "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
        "barBorderRadius": [30, 30, 30, 30],
        "shadowColor": 'rgb(0, 160, 221)'
    }})
page.add(bar)
# 各地区985高校数量柱状图
bar = Bar()
bar.add_xaxis(data_985['name'].values.tolist())
bar.add_yaxis("", data_985['counts'].values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    title_opts=opts.TitleOpts(title="各地区985高校数量"),
    datazoom_opts=opts.DataZoomOpts()
)
bar.set_series_opts(itemstyle_opts={
    "normal": {
        "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
        "barBorderRadius": [30, 30, 30, 30],
        "shadowColor": 'rgb(0, 160, 221)'
    }})
page.add(bar)
# 各地区211高校数量柱状图
bar = Bar()
bar.add_xaxis(data_211['name'].values.tolist())
bar.add_yaxis("", data_211['counts'].values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    title_opts=opts.TitleOpts(title="各地区211高校数量"),
    datazoom_opts=opts.DataZoomOpts()
)
bar.set_series_opts(itemstyle_opts={
    "normal": {
        "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
        "barBorderRadius": [30, 30, 30, 30],
        "shadowColor": 'rgb(0, 160, 221)'
    }})
page.add(bar)
# 各地区高质量高校数量柱状图
bar = Bar()
bar.add_xaxis(data_985_211['name'].values.tolist())
bar.add_yaxis("", data_985_211['counts'].values.tolist())
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    title_opts=opts.TitleOpts(title="各地区高质量高校数量", subtitle="包括211与985高校"),
    datazoom_opts=opts.DataZoomOpts()
)
bar.set_series_opts(itemstyle_opts={
    "normal": {
        "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""),
        "barBorderRadius": [30, 30, 30, 30],
        "shadowColor": 'rgb(0, 160, 221)'
    }})
page.add(bar)
page.render("templates/bar.html")


# 饼图页面
page = Page()
# 各地区高校数量饼状图
pie = Pie()
pie.add("", [list(z) for z in zip(data['name'].values.tolist(), data['counts'].values.tolist())],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="各地区高校数量统计"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
page.add(pie)
# 各地区985高校数量饼状图
pie = Pie()
pie.add("", [list(z) for z in zip(data_985['name'].values.tolist(), data_985['counts'].values.tolist())],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="各地区985高校数量统计"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
page.add(pie)
# 各地区211高校数量饼状图
pie = Pie()
pie.add("", [list(z) for z in zip(data_211['name'].values.tolist(), data_211['counts'].values.tolist())],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="各地区211高校数量统计"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
page.add(pie)
# 高校数量前十名的地区
pie = Pie()
pie.add("", [list(z) for z in zip(data['name'].values.tolist()[:10], data['counts'].values.tolist()[:10])],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="高校数量前十名的地区"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
page.add(pie)
# 高校数量后十名的地区
pie = Pie()
pie.add("", [list(z) for z in zip(data['name'].values.tolist()[-10:], data['counts'].values.tolist()[-10:])],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="高校数量后十名的地区"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
page.add(pie)
page.render("templates/pie.html")


# 地图页面
page = Page()
# 全国高校数量热力图
geo = Geo()
geo.add_schema(maptype="china")
geo.add("全国高校数量热力图", [list(z) for z in zip(data['name'].values.tolist(), data['counts'].values.tolist())],
        type_=ChartType.HEATMAP)
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title="全国高校数量热力图")
)
page.add(geo)
# 全国高校数量分段图
geo = Geo()
geo.add_schema(maptype="china")
geo.add("全国高校数量段位图", [list(z) for z in zip(data['name'].values.tolist(), data['counts'].values.tolist())],
        type_=ChartType.EFFECT_SCATTER)
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=150),
    title_opts=opts.TitleOpts(title="全国高校数量段位图")
)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
page.add(geo)
# 高质量高校数量热力图
geo = Geo()
geo.add_schema(maptype="china")
geo.add("高质量高校分布热力图",
        [list(z) for z in zip(data_985_211['name'].values.tolist(), data_985_211['counts'].values.tolist())],
        type_=ChartType.HEATMAP)
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=50),
    title_opts=opts.TitleOpts(title="高质量高校分布热力图", subtitle="包括211与985高校")
)
page.add(geo)
# 高质量高校数量分段图
geo = Geo()
geo.add_schema(maptype="china")
geo.add("高质量高校数量段位图", [list(z) for z in zip(data_985_211['name'].values.tolist(), data_985_211['counts'].values.tolist())],
        type_=ChartType.EFFECT_SCATTER)
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True, max_=12, split_number=4),
    title_opts=opts.TitleOpts(title="高质量高校数量段位图", subtitle="包括211与985高校")
)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
page.add(geo)
page.render("templates/geo.html")


# 水球图页面
page = Page()
# 北京985高校占比
liquid = Liquid()
liquid.add('', [data_985['rate'].values[0]])
liquid.set_global_opts(title_opts=opts.TitleOpts(title="北京985高校占比"))
page.add(liquid)
# 北京211高校占比
liquid = Liquid()
liquid.add('', [data_211['rate'].values[0]])
liquid.set_global_opts(title_opts=opts.TitleOpts(title="北京211高校占比"))
page.add(liquid)
# 北京上海江苏985高校占比
liquid = Liquid()
liquid.add('', [sum(data_985['rate'].values[:3])])
liquid.set_global_opts(title_opts=opts.TitleOpts(title="北京上海江苏985高校占比"))
page.add(liquid)
# 北京上海江苏211高校占比
liquid = Liquid()
liquid.add('', [sum(data_211['rate'].values[:3])])
liquid.set_global_opts(title_opts=opts.TitleOpts(title="北京上海江苏211高校占比"))
page.add(liquid)
page.render("templates/liquid.html")


# 高校性质与类型页面
page = Page()
# 高校类型分析
df_type = df_new[df_new['type'] != '——']
df_type = df_type[df_type['type'] != '------']
df_type_counts = df_type['type'].value_counts()
dict_type_counts = {'name': df_type_counts.index, 'counts': df_type_counts.values}
data_type_counts = pd.DataFrame(dict_type_counts)
pie = Pie()
pie.add("",
        [list(z) for z in zip(data_type_counts['name'].values.tolist(), data_type_counts['counts'].values.tolist())],
        radius=["30%", "75%"],
        center=["40%", "50%"],
        rosetype="radius")
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="高校类型分布"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}所 占比{d}%"))
page.add(pie)
# 高校性质分析
df_nature = df_new[df_new['nature'] != '——']
df_nature = df_nature[df_nature['nature'] != '------']
df_nature_counts = df_nature['nature'].value_counts()
dict_nature_counts = {'name': df_nature_counts.index, 'counts': df_nature_counts.values}
data_nature_counts = pd.DataFrame(dict_nature_counts)
pie = Pie()
pie.add("", [list(z) for z in
             zip(data_nature_counts['name'].values.tolist(), data_nature_counts['counts'].values.tolist())],
        )
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="高校性质分布"),
    legend_opts=opts.LegendOpts(
        type_="scroll", pos_left="80%", orient="vertical"
    )
)
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}所 占比{d}%"))
page.add(pie)
page.render("templates/attribute.html")
