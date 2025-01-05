## Workshop - 2

### Notes

Time Series Analysis is Easy using pandas
Categorical is defined as object

df.info() also returns a dataframe **Imp**
df['colName']

selecting rows - iloc[] index value
loc[] index or condition can be used

filling vs dropping
drop when you don't know how to fill the nan values
categorical cols could be filled with mode and numerical with median or mean

#### Data cleaning

df.isnull() - returns a dataframe of boolean for null values
df.isnull().sum() - sum of all the null values
df.dropna() - drops row with null

#### Data imputation - filling null values

df.fillna(method='fillna') - fills value above
df.column.fillna(dataset.column.mean()) - mean of the col

df.random.seed(42) - same random values again(for reproducability)

pd.concat()

Trim the whitespaces
df['colName'].str.strip()
df['colName'].astype(int) **Careful**

df.rename(columns={})
df.drop_duplicates()

#### Data Transformation

df.pivot(index, columns, values) - convert rows to col --transpose
df.melt() - wide to long

wide format || long format **Imp**

#### Scaling

Scaling is done after data analytics is done and you want to make / train a model

Min-Max scaling - what you do when you need both the extreme values
df.standardization - mean-0 sd-1

#### Encoding

changing categorical values to nums / machine understandable

- Label Encoding
- Ordinal encoding - make a dict and map the col. with the mapping

- what is the use of name column ? is it categorical ?

One-hot encoding - making matrix | array for each coln
problem - increased column size
imp in NLP and DL not in ML
pd.dummies() - used for one hot encoding

MayaDB - Database common in use (in context of Nepal)

row and coln. concat axis=0 and axis=1
inner Join, outer, left, right \*\* what is join ?

# Machine learning

#### assumption

the sample is an iid of population with some underlying distrubution

parametric and non parametric

non parametric - we don't assume we observe the data pattern
parametric - fixed set of parameter

### problems

model selection and model fitting
parameters comes from model selection

linear regression - slope and intercept
KNN - one parameter
neural network - weight and biases

### Non parametric

- prone to overfitting [ more error in test data ] as it does only depend on data

- clustering
- Decision tree
- Support vector Machines

- group the similar data ( most easiest thing to do )

### K Nearest Neighbor (KNN)

- Instance based classifier
- based on Duck Test - looks, swims, quack like a duck then probably the duck

but how does machine measure the similarity

#### Basic idea of instance based classifier

- distance in Euclidian space
- similarity inversely proportional to similarity

train is to find(learn) optimal parameter through optimization

we don't need training in KNN because there is no parameter to learn
k - neighbors to compare

may be a noise for 1 NN - confidence low
for 2 NN - how to split - which one to assign
for 3 NN - can use majority vote for classification | for regression assign the mean

for k NN - more confidence but lots of noise decision boundary
Decision boundary may be corrupted for both low and high K

so how to calculate K(Hyper parameter - something you define) ?
parameter - something that machine learns

cross validation
never pick even value of k - experiment between 3, 5 and 7

shape the questions - how does it come ?
