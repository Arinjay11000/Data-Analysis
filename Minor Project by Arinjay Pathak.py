Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> st=pd.read_csv(r"C:\Users\Lenovo\Desktop\StudentsPerformance (1).csv")
>>> pd.set_option("display.max_rows",500)
>>> pd.set_option("display.max_columns",500)
>>> pd.set_option("display.width",1000)
>>> st.head()
   gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
0  female        group B           bachelor's degree      standard                    none          72             72             74
1  female        group C                some college      standard               completed          69             90             88
2  female        group B             master's degree      standard                    none          90             95             93
3    male        group A          associate's degree  free/reduced                    none          47             57             44
4    male        group C                some college      standard                    none          76             78             75
>>> st.groupby("gender").mean()
        math score  reading score  writing score
gender                                          
female   63.633205      72.608108      72.467181
male     68.728216      65.473029      63.311203
>>> st.groupby("race/ethnicity").mean()
                math score  reading score  writing score
race/ethnicity                                          
group A          61.629213      64.674157      62.674157
group B          63.452632      67.352632      65.600000
group C          64.463950      69.103448      67.827586
group D          67.362595      70.030534      70.145038
group E          73.821429      73.028571      71.407143
>>> st.groupby("parental level of education").mean()
                             math score  reading score  writing score
parental level of education                                          
associate's degree            67.882883      70.927928      69.896396
bachelor's degree             69.389831      73.000000      73.381356
high school                   62.137755      64.704082      62.448980
master's degree               69.745763      75.372881      75.677966
some college                  67.128319      69.460177      68.840708
some high school              63.497207      66.938547      64.888268
>>> st.groupby("lunch").mean()
              math score  reading score  writing score
lunch                                                 
free/reduced   58.921127      64.653521      63.022535
standard       70.034109      71.654264      70.823256
>>> st.groupby("test preparation course").mean()
                         math score  reading score  writing score
test preparation course                                          
completed                 69.695531      73.893855      74.418994
none                      64.077882      66.534268      64.504673
>>> st.groupby("gender")["math score"].describe()
        count       mean        std   min   25%   50%   75%    max
gender                                                            
female  518.0  63.633205  15.491453   0.0  54.0  65.0  74.0  100.0
male    482.0  68.728216  14.356277  27.0  59.0  69.0  79.0  100.0
>>> st.groupby("gender")["reading score"].describe()
        count       mean        std   min    25%   50%   75%    max
gender                                                             
female  518.0  72.608108  14.378245  17.0  63.25  73.0  83.0  100.0
male    482.0  65.473029  13.931832  23.0  56.00  66.0  75.0  100.0
>>> st.groupby("gender")["writing score"].describe()
        count       mean        std   min   25%   50%    75%    max
gender                                                             
female  518.0  72.467181  14.844842  10.0  64.0  74.0  82.00  100.0
male    482.0  63.311203  14.113832  15.0  53.0  64.0  73.75  100.0
>>> st.groupby("race/ethnicity")["math score"].describe()
                count       mean        std   min    25%   50%   75%    max
race/ethnicity                                                             
group A          89.0  61.629213  14.523008  28.0  51.00  61.0  71.0  100.0
group B         190.0  63.452632  15.468191   8.0  54.00  63.0  74.0   97.0
group C         319.0  64.463950  14.852666   0.0  55.00  65.0  74.0   98.0
group D         262.0  67.362595  13.769386  26.0  59.00  69.0  77.0  100.0
group E         140.0  73.821429  15.534259  30.0  64.75  74.5  85.0  100.0
>>> st.groupby("race/ethnicity")["reading score"].describe()
                count       mean        std   min    25%   50%    75%    max
race/ethnicity                                                              
group A          89.0  64.674157  15.543762  23.0  53.00  64.0  74.00  100.0
group B         190.0  67.352632  15.177499  24.0  56.00  67.0  79.75   97.0
group C         319.0  69.103448  13.997033  17.0  60.00  71.0  78.50  100.0
group D         262.0  70.030534  13.895306  31.0  60.25  71.0  79.00  100.0
group E         140.0  73.028571  14.874024  26.0  63.00  74.0  84.00  100.0
>>> st.groupby("race/ethnicity")["writing score"].describe()
                count       mean        std   min    25%   50%    75%    max
race/ethnicity                                                              
group A          89.0  62.674157  15.468278  19.0  51.00  62.0  73.00   97.0
group B         190.0  65.600000  15.625173  15.0  55.25  67.0  78.00   96.0
group C         319.0  67.827586  14.983378  10.0  57.00  68.0  79.00  100.0
group D         262.0  70.145038  14.367707  32.0  61.00  72.0  80.00  100.0
group E         140.0  71.407143  15.113906  22.0  62.00  72.0  80.25  100.0
>>> st.groupby("parental level of education")["math score"].describe()
                             count       mean        std   min    25%   50%   75%    max
parental level of education                                                             
associate's degree           222.0  67.882883  15.112093  26.0  57.00  67.0  80.0  100.0
bachelor's degree            118.0  69.389831  14.943789  29.0  61.00  68.0  79.0  100.0
high school                  196.0  62.137755  14.539651   8.0  53.75  63.0  72.0   99.0
master's degree               59.0  69.745763  15.153915  40.0  55.50  73.0  81.0   95.0
some college                 226.0  67.128319  14.312897  19.0  59.00  67.5  76.0  100.0
some high school             179.0  63.497207  15.927989   0.0  53.00  65.0  74.0   97.0
>>> st.groupby("parental level of education")["reading score"].describe()
                             count       mean        std   min   25%   50%    75%    max
parental level of education                                                             
associate's degree           222.0  70.927928  13.868948  31.0  61.0  72.5  81.00  100.0
bachelor's degree            118.0  73.000000  14.285250  41.0  63.0  73.0  82.75  100.0
high school                  196.0  64.704082  14.132130  24.0  54.0  66.0  74.25   99.0
master's degree               59.0  75.372881  13.775163  42.0  65.5  76.0  84.50  100.0
some college                 226.0  69.460177  14.057049  23.0  60.0  70.5  79.75  100.0
some high school             179.0  66.938547  15.479295  17.0  56.5  67.0  79.00  100.0
>>> st.groupby("parental level of education")["writing score"].describe()
                             count       mean        std   min   25%   50%   75%    max
parental level of education                                                            
associate's degree           222.0  69.896396  14.311122  35.0  58.0  70.5  80.0  100.0
bachelor's degree            118.0  73.381356  14.728262  38.0  62.5  74.0  83.0  100.0
high school                  196.0  62.448980  14.085907  15.0  52.0  64.0  73.0  100.0
master's degree               59.0  75.677966  13.730711  46.0  67.0  75.0  85.0  100.0
some college                 226.0  68.840708  15.012331  19.0  60.0  70.0  79.0   99.0
some high school             179.0  64.888268  15.736197  10.0  54.0  66.0  77.0  100.0
>>> st.groupby("lunch")["math score"].describe()
              count       mean        std   min   25%   50%   75%    max
lunch                                                                   
free/reduced  355.0  58.921127  15.159956   0.0  49.0  60.0  69.0  100.0
standard      645.0  70.034109  13.653501  19.0  61.0  69.0  80.0  100.0
>>> st.groupby("lunch")["reading score"].describe()
              count       mean        std   min   25%   50%   75%    max
lunch                                                                   
free/reduced  355.0  64.653521  14.895339  17.0  56.0  65.0  75.0  100.0
standard      645.0  71.654264  13.830602  26.0  63.0  72.0  82.0  100.0
>>> st.groupby("lunch")["writing score"].describe()
              count       mean        std   min   25%   50%   75%    max
lunch                                                                   
free/reduced  355.0  63.022535  15.433823  10.0  53.0  64.0  74.0  100.0
standard      645.0  70.823256  14.339487  22.0  62.0  72.0  81.0  100.0
>>> 
KeyboardInterrupt
>>> st.groupby("test preparation course")["math score"].describe()
                         count       mean        std   min   25%   50%    75%    max
test preparation course                                                             
completed                358.0  69.695531  14.444699  23.0  60.0  69.0  79.00  100.0
none                     642.0  64.077882  15.192376   0.0  54.0  64.0  74.75  100.0
>>> st.groupby("test preparation course")["reading score"].describe()
                         count       mean        std   min   25%   50%   75%    max
test preparation course                                                            
completed                358.0  73.893855  13.638384  37.0  65.0  75.0  84.0  100.0
none                     642.0  66.534268  14.463885  17.0  57.0  67.0  76.0  100.0
>>> st.groupby("test preparation course")["writing score"].describe()
                         count       mean        std   min   25%   50%   75%    max
test preparation course                                                            
completed                358.0  74.418994  13.375335  36.0  66.0  76.0  83.0  100.0
none                     642.0  64.504673  14.999661  10.0  54.0  65.0  74.0  100.0
>>> st.groupby("gender").mean().plot(kind="bar")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000020E88654E20>
>>> plt.ylabel("Average marks")
Text(0, 0.5, 'Average marks')
>>> plt.title("Average Based On Gender")
Text(0.5, 1.0, 'Average Based On Gender')
>>> plt.show()
>>> st.groupby("race/ethnicity").mean().plot(kind="barh")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000020E886739D0>
>>> plt.xlabel("Average marks")
Text(0.5, 0, 'Average marks')
>>> plt.title("Average based on Ethnicity")
Text(0.5, 1.0, 'Average based on Ethnicity')
>>> plt.show()
>>> st.groupby("parental level of education").mean().plot(kind="barh")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000020E8867A160>
>>> plt.xlabel("Average marks")
Text(0.5, 0, 'Average marks')
>>> plt.title("Average Based On Parent Education")
Text(0.5, 1.0, 'Average Based On Parent Education')
>>> plt.show()
>>> st.groupby("lunch").mean().plot(kind="bar")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000020E8B435AF0>
>>> plt.ylabel("Average marks")
Text(0, 0.5, 'Average marks')
>>> plt.title("Average Based On Type Of Lunch")
Text(0.5, 1.0, 'Average Based On Type Of Lunch')
>>> plt.show()
>>> st.groupby("test preparation course").mean().plot(kind="bar")
<matplotlib.axes._subplots.AxesSubplot object at 0x0000020E8EAE1070>
>>> plt.ylabel("Average marks")
Text(0, 0.5, 'Average marks')
>>> plt.title("Average Based On Preparation Course Taken")
Text(0.5, 1.0, 'Average Based On Preparation Course Taken')
>>> plt.show()
>>> 