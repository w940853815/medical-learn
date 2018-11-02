# 我的文档
## 一个描述
    数据的相关性统计方法，要求输入一个dfx(dataframe),dfy(dataframe),
    求dfx的每列和dfy的每列的相关系数及p值，需要指定相关系数的方法meathod：'pearson'
    、'kendall'、'spearman'，返回一个相关系数和p-value的dataframe在‘result‘关键字中
    
    
    方法
    -------
        get_info : 
            获取该模型的信息， 返回一个字典，包含‘id’和‘name’, 'description','limited'关键字
            含义分别为：模型的id, 模型的名称，模型的描述，模型的适用范围
        
        run:  
            参数
            ----------
            df: pandas DataFrame
                如果方法为‘pearson’，需要每列的数据都是数字型数据，不能是字符串或者object
            
            dfy: pandas DataFrame
                ‘pearson’，需要每列的数据都是数字型数据，不能是字符串或者object
                
            method: str
                需要计算相关系数的方式，可选'pearson'(默认),'kendall'、'spearman'
                
            crosstab: bool, default:False
                是否需要转换返回的dataframe的数据布局格式，如果为True则转为x,y的矩阵对应格式
            
    返回结果
    ----------        
        返回一个字典，带有‘result’关键字，其值为相关系数和p-value组成的dataframe
        
## 公式如下：
### 
## $$ \rho = \frac{\text{cov}(X,Y)}{\sigma_x \sigma_y} $$

### 相关系数r:
## $$ r = \frac{{}\sum_{i=1}^{n} (x_i - \overline{x})(y_i - \overline{y})} 
{\sqrt{\sum_{i=1}^{n} (x_i - \overline{x})^2(y_i - \overline{y})^2}}$$

## 输入的参数说明和使用场景
|系数|	使用场景|	备注|
|:--|:--|:--|
|Pearson|	定量数据，数据满足正态性时|	正态图可查看正态性，散点图展示数据关系|
|Spearman|	定量数据，数据不满足正态性时|	散点图可查看正态性，散点图展示数据关系|
|Kendall| 	定量数据一致性判断|	通常用于评分数据一致性水平研究【非关系研究】，比如评委打分，数据排名等。|

## 一张照片
![我的照片](https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2791261768,1320060678&fm=26&gp=0.jpg)


