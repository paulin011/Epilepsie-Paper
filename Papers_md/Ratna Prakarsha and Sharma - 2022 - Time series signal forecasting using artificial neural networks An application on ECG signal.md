# Ratna Prakarsha and Sharma - 2022 - Time series signal forecasting using artificial neural networks An application on ECG signal

Contents lists available at ScienceDirect 

Biomedical Signal Processing and Control 

journal homepage: www.elsevier.com/locate/bspc 

Time series signal forecasting using artificial neural networks: An 
application on ECG signal 

Kandukuri Ratna Prakarsha , Gaurav Sharma * 

Department of ECE, CVR College of Engineering, Hyderabad, India   

A R T I C L E  I N F O    

A B S T R A C T    

Keywords: 
Time Series Forecasting 
Artificial Neural Networks (ANN) 
FFNN 
Adaptive Filter 
LMS 

Time Series Forecasting is the prediction of future values of a signal based on the observed past values. It has 
various applications in signal processing, especially in the medical field which needs high accuracy. This paper 
presents an MLP (Multilayer Perceptron), a class of FFNN (Feedforward Neural Network) for highly accurate time 
series forecasting. There are various methods of signal processing that are used in time series forecasting but each 
method is specific to the particular problem it solves. The current methods involve the use of different types of 
adaptive  filters  out of which  the most common method is LMS (Least Mean  Square) algorithm. Although the 
adaptive  filters give a decent  accuracy, but  neural networks (NN) give the results more  than satisfactory. On 
performing time series forecasting on a simulated ECG (Electrocardiogram) signal, an accuracy of 95.72% was 
achieved using ANNs (Artificial Neural Networks) competing with the LMS filter, which gave only 79% accuracy. 
When the same was implemented on real ECG data of a person suffering from Sleep Apnea, the ANNs offered 
98.68% while LMS filter displayed only 91% accuracy. Additionally, the neural network was also denoising the 
signal while predicting. A signal-to-noise ratio of 29.71 dB and 16.33 dB for Neural Network prediction and LMS 
filter prediction was attained, respectively. In the case of the real data, the aforementioned values stand at 22.8 
dB and 3.8 dB, respectively. Simulated results show that the neural networks give superior performance in time 
series forecasting than Adaptive Filters.   

1. Introduction 

A ’Time series’ is a series of data points that occur in sequential order 
over  a  period,  whereas  ’Forecasting’  is  a  prediction  of  the  future.  To 
explain it in simple terms it can be said that Time Series Forecasting is 
the prediction of future values of a series based on its past values. ECG 
signal is a time series data. It is measured in equal intervals of time at 
various  frequencies.  An  ECG  is  the  electrical  signals  generated  by  a 
human heart as it beats. It is a crucial time series data in the medical 
field. It reveals critical details about a patient’s health which may help 
diagnose or monitor sicknesses. 

Applications of time series forecasting range from signal processing 
to statistical analysis. To name a few, it could be predicting the weather 
pattern,  crop  yield,  stock  prices,  birth  rate,  etc.  [1–5].  It  can  play  a 
pivotal role in biomedical practices. An example of that could be the 
prediction and monitoring of ECG. It is important that the ECG is always 
in rhythm and maintains a proper pace. An ECG can detect cardiomy-
opathy,  heart  attacks,  coronary  heart  disease,  arrhythmias  [31],  high 
blood  pressure,  previous  history  of  heart  attacks,  etc.  Hence,  proper 

monitoring techniques are cardinal. In the current work, an ECG signal is 
predicted with two different approaches to compare  which technique 
gives  the  maximum accuracy.  As  a  matter  of fact,  if high  accuracy is 
achievable in any applications of time series forecasting, then the same 
predictions can help in taking precautions or for making the right de-
cisions at the right time. Hence, the ease of forecasting and high accu-
racy will always remain of paramount importance. 

Adaptive  filters  being  at  the  heart  of  signal  processing  offer 
numerous methods to perform signal forecasting. An adaptive filter is a 
system  that  includes  a  linear  filter  with  a  transfer  function  that  is 
controlled by variable parameters and has the ability to alter those pa-
rameters  using  optimization  techniques.  For  example,  Least  Mean 
Squares  (LMS)  Based  FIR  (Finite  Impulse  Response)  Adaptive  Filters, 
Recursive Least Squares (RLS) Based FIR Adaptive Filters, Affine Pro-
jection (AP) FIR Adaptive Filters, FIR Adaptive Filters in the Frequency 
Domain (FD), Lattice-Based (L) FIR Adaptive Filters are a few adaptive 
filters. Apart from adaptive filters, ML (Machine Learning) can also be 
used to predict signals. One such ML technique is discussed in this paper. 

a. Artificial neural networks (ANN) 

* Corresponding author. 

E-mail address: ergaurav209@yahoo.co.in (G. Sharma).  

https://doi.org/10.1016/j.bspc.2022.103705 
Received 18 December 2021; Received in revised form 31 March 2022; Accepted 9 April 2022   

BiomedicalSignalProcessingandControl76(2022)103705Availableonline20April20221746-8094/©2022ElsevierLtd.Allrightsreserved.K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

Fig. 1. Biological neuron vs artificial neuron.  

[6–8]. 

LMS filters are a category of adaptive filters that use gradient descent 
to  narrow  down  the  mean  squared  error.  It’s  filter  coefficients  adapt 
based on the instantaneous error and the rate at which they update is 
determined  by  the  learning  rate.  They  are  made  up  of  an  ADALINE 
(Adaptive Linear) network. 

Knowing the future can always allow us to be better prepared. Spe-
cifically, while forecasting signals, the conventional methods that use 
adaptive filters are not very satisfactory in terms of accuracy. Although 
they  give  an  appreciable  accuracy,  they  are  far  from  desired  value 
needed in critical applications such as in the biomedical field. Hence, 
this calls  for a  need to come up  with a  better method  for time series 
forecasting [2,5]. 

The main contributions of the present study are as follows: 

• This study aims to perform time-series prediction using neural net-
works, contrary to the traditional method of using adaptive filters 
offered  by  signal  processing;  and  thereby  obtain  better  and  more 
accurate results.  

• This was achieved by employing time-series forecasting using neural 
networks on simulated as well as on real time ECG Signal of sleep 
apnea patient and comparing them with the traditional methods. 

The rest of the paper is structured as follows: Section 2 presents a 
review  of  the  literature  and  related  work  of  time  series  forecasting. 
Section 3 describes the proposed method followed by Section 4, which 
gives the obtained results, and a discussion of the results and a practical 
use case scenario is described. Finally, the conclusion and future scope 
are drawn in Section 5. 

2. Related works 

Dipankar Gupta [2] in a thesis mentions about time series analysis of 
ECG data and its unreliable forecasting. According to the study, linear 
systems  that  are  used  to  describe  complex  biological  systems  such  as 
ECG data are no longer satisfactory. It was mentioned in the paper that“ 
It is  assumed that parameters  of our model are known exactly  but in 
practice parameters of the model are estimated. So, some of the error 
made  in  forecasting  will  be  due  to  the  error  of  the  estimation  of  the 
parameters rather than just to the random error of the model.”. 

In Eva Volna et al. [26], the implementation of classification of ECG 
is discussed. The state of the patient is diagnosed as to whether sick or 
healthy, by classifying the ECG into 0 or 1. The concept of the paper was 
to  detect  cardiac  abnormality  based  on  the  pattern  recognised  in  the 
ECG i.e. to detect normal cycle or arrhythmia and make further diag-
nosis  based  on  it.  The  classification  was  performed  in  three  different 
methods, and one of them was to use Neural Networks. 

In accordance with [27], it can be said that deep neural networks 
(DNNs)  prove  to  be  good  for  analysing  the  ECG  signal  where  it 

Fig. 2. Adaptive filter.  

The  term  “Artificial  Neural  Network”  is  derived  from  biological 
neural networks that compose a human brain as shown in Fig. 1. They 
were created to mimic the neural networks which make up the human 
brain, hoping to allow the machines to make decisions like humans. Just 
like our brains, it may have multiple layers of networks. It has the below- 
listed layers:  

1)  Input Layer  
2)  Hidden Layers  
3)  Output Layer 

The  input  goes  through  a  series  of  transformations  in  the  hidden 
layer, which finally results in output that is conveyed through the output 
layer. The artificial neural network takes input vector X = [x1,x2,x3⋯xn] 
and computes the weighted sum of the inputs and adds a bias ‘b’ to it 
where weights are W = [w1, w2, w3⋯wn] [3]. This computation can be 
represented in Eq. (1). 

z =

∑n

i=1

wi*xi + b

(1)  

The computed value ‘z’ is fed into the activation function as an input to 
give  out  the  final  output.  The  activation  function  decides  whether  a 
given neuron must be fired or not. 

y = f (z)
↓
Activation function

(2)  

A representation of the activation function is given in Eq. (2) where f is 
any activation function and y is the final output. 

b. Adaptive filters 
Digital filters whose coefficients change to achieve an optimal state 
are  called  Adaptive  Filters.  A  cost  function  is  used  as  a  criterion  to 
optimize. A block diagram for an adaptive filter is shown in Fig. 2. There 
are many types of cost functions but almost all of them need the error 
value to be computed. The most common adaptive filter is the LMS filter 

BiomedicalSignalProcessingandControl76(2022)1037052K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

outperforms  the  cardiology  resident  medical  doctors  in  diagnosing  6 
diseases. The paper suggests eradicating the two-step approach to make 
any diagnosis using ECG where, first the features are extracted from the 
ECG  using  conventional  techniques  and  later  used  for  classifications. 
The NNs perform “end-to-end” learning where it independently extracts 
the features of ECG and learns the nature of it [19]. 

In  Sireesha  et  al.  [7],  adaptive  filter  based  on  Least  Mean  Square 
(LMS) algorithm to be applied in underwater acoustic communication. 
The paper discusses the system configuration, filter structure, and the 
implementation of the Adaptive LMS algorithm. The factors such as the 
convergence and stability of the filter which are responsible for stable 
adaptation  behaviour  are  also  discussed.  The  performance  of  the 
designed  adaptive  filter  is  compared  with  the  in-built  MATLAB  LMS 
filter. The study was found to be satisfactory and viable. 

Zeidler [9] mentions that the conditions required to implement real- 
time adaptive prediction filters that provide nearly optimal performance 
in realistic input conditions are delineated. The paper explicitly studies 
the effects of signal bandwidth, input signal-to-noise ratio (SNR), noise 
correlation,  and  noise  non-stationarity.  It  also  shows  that  the  signal 
processing gain nonlinearly degrades, as a function of input. It mentions 
that the stochastic nature of the weights bound the performance of the 
adaptive filters in the optimal filter state. 

In Oancea and Ciucu [10], it has been demonstrated that a NN can 
approximate any continuous function. Forecasting of financial data se-
ries is successfully implemented with Neural networks. It states that the 
classical  methods  used  for  time  series  prediction  like  Box-Jenkins  or 
ARIMA (Autoregressive Integrated Moving Average) assumes that there 
is a linear relationship between inputs and outputs. Neural Networks are 
said to have the advantage that can approximate nonlinear functions. In 
this  paper  they  compared  the  performances  of  different  feed  forward 
and recurrent neural networks and training algorithms for predicting the 
exchange rate EUR/RON and USD/RON. 

To discuss a few research works where the adaptive filters were used 
for prediction, it can be seen in the paper [29], that Adaptive filtering to 
predict the lung tumour motion during breathing was performed using 
linear  adaptive  filters  as  well  as  adaptive  neural  networks  algorithm. 
Wesen  et  al.  [28],  had  designed  an  adaptive  filter  for  stock  market 
prediction  using  a  correlation-based  criterion.  The  research  proposes 
novel adaptive filtering-based predictors for investment strategies to be 
used  in  the  stock  market  as  a  decision-making  engineering  tool.  In 
Shavelis et al. [30], the prediction of the future values of the vehicle 
sideslip angle is performed using neural networks and normalised least 
mean squared algorithm and compared their performance. 

In Putra and Kosala [11], artificial neural networks were found to be 
delivering better forecasting performance than the results obtained by 
the  well-known  ARIMA  technique.  They  believe  that,  unlike  conven-
tional techniques for time series analysis, an artificial neural network 

Fig. 3. ECG visualization.  

needs little information about the time series data and can be applied to 
a broad range of problems. Artificial Neural Networks are suitable for 
many tasks in pattern recognition and ML [12,13]. In this paper, an APL 
(Automated Predictive Library) system for forecasting univariate time 
series with artificial neural networks is presented. 

In Xiao et al. [39], discussed how to use of different ML models could 
be used to predict UCG (Underground Coal Gasification) to contribute to 
clean and efficient use of coal and its stable production. Dual-source long 
short-term memory (LSTM) model was proposed as the optimal solution 
for the application. In Xiao et al. [40] it is described how the insufficient 
time dependency in MTS (Multivariate Time Series) could be tackled by 
the use of a combination of attention mechanism and LSTM while per-
forming MTS prediction. 

In Kaushik et al. [14], the primary objective was to evaluate different 
statistical,  neural,  and  ensemble  techniques  in  their  ability  to  predict 
patients’ weekly average expenditures on certain pain medications. Two 
statistical models, persistence (baseline) and autoregressive integrated 
moving average (ARIMA), a multilayer perceptron (MLP) model, a long 
short-term memory (LSTM) model, and an ensemble model combining 
predictions of the ARIMA, MLP, and LSTM models were calibrated to 
predict  the  expenditures  on  two  different  pain  medications.  Results 
revealed  that  the  ensemble  model  outperformed  the  persistence, 
ARIMA, MLP, and LSTM models across both pain medications [15,16]. 
Carrying  out analysis  of ECG  has been  ever prevalent. As  medical 
fields always demand precision, efforts remain to continuously improve 
the technology to make lives of humans last longer. In Zhao et al. [32] 
the implementation of noise rejection for wearable ECGs using a com-
bination of MFSW (Modified Frequency Slice Wavelet Transform) and 
CNNs (Convolutional Neural Networks) was discussed. A classification 
model was used to detect the noisy segments of the signal. The paper 
[33], displays a comprehensive and experimental study on classification 
of  ventricular  premature  and  ischemic  heartbeats  with  the  help  of 
various methods including the use of ML models. In a different article 
[34], observations were recorded as cardiac arrhythmia was detected 
from ECG using adaptive feature extraction and modified Support Vec-
tor Machines (SVMs). There are many more such papers published to 
improve the sense making process from the biomedical signals [35,36]. 
Some papers such as [2,9,18,37] even though old, prove to be a good 
source of resources of knowledge to bridge the gap between what was 
once known and what is being studied. 

There have been quite a few theses and papers published on time 
series forecasting. Most of them were performed on statistical data using 
statistical methods such as ARIMA model (Auto-Regressive Integrated 
Moving  Average)  [18]  but  to  the  best  of  our  knowledge,  time  series 
signal prediction has not been reported in literature. Considering ANNs, 
even it has a lot of papers published on its technology but most of them 
compared the performance of several techniques present internally in 
the ANN technology [39]. Moreover, even adaptive filters have had their 
share of papers published, but even here the focus was mostly laid on 
comparison of different types of adaptive filters. But our solution comes 
from a field that is a union of all three previously mentioned areas, i.e. 
time series forecasting of a signal using ANNs and adaptive filters [17]. 
In our proposed solution we perform time series forecasting of an ECG 
signal using ANNs, as well as with conventional adaptive filters. Further, 
performance is compared. Proper implementation of the method may 
even eliminate the necessity of signal de-noising before analysis. 

3. Proposed technique 

The proposed solution involves forecasting a time series using arti-
ficial neural networks, to be more specific MLP (Multilayer Perceptron), 
a class of FFNN (Feedforward Neural Network) is used to achieve high 
accuracy. Although the adaptive filters provide a decent accuracy, the 
neural networks give us a more than satisfactory result proving to be 
better than the adaptive filters. 

Forecasting of a simulated ECG signal is performed using ANNs as 

BiomedicalSignalProcessingandControl76(2022)1037053K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

Fig. 4. Sliding window technique.  

well  as  LMS  filters.  Further,  their  performances  are  compared.  Our 
proposed solution along with giving highly accurate forecasting, also de- 
noises the signal [20]. Further, the same is also applied to a real ECG 
data of a sleep apnea patient and its outcomes are discussed in the ‘re-
sults and discussion’ section. 
a. Data Pre-processing 
i. Data Generation 
In the present study, simulated data has been used. A library called 
’Neurokit2
was implemented to simulate the required ECG data [21]. 
The library is a user-friendly package providing easy access to advanced 
bio-signal processing routines. It also allows users to add noise by a user- 
defined factor. A noise introduced simulated ECG signal is used to pre-
dict the upcoming sample value of the noiseless ECG data. 

′

ii. Visualization of ECG 
In Fig. 3, the x-axis represents the samples and y-axis represents the 
Voltage. Yellow signal is the noisy signal whereas the blue signal is the 
original signal. 

Note: As it is a simulated ECG signal it may not be exactly like an 
original ECG. The implementation presented in this paper is just a proof 
of  concept  for  the  methodologies  suggested.  However,  the  proposed 
method is also implemented and discussed on real ECG data of a sleep 
apnea patient in the ‘results and discussion’ section. 

iii. Train and Test Split 
To evaluate the model, the available data is split into two parts. The 
first  subset  is  used  to  fit  the  model  and  is  called  as  training  dataset. 
Whereas the second subset is not used to train the model; instead, it is 
used to later test the model by making inferences using data never seen 
by the model [22]. This surprise test for the model reveals the true ac-
curacy of the model. Hence, the second subset is called test data. 

Usually, 75% of data is used for training and 25% of data is used for 
testing. Hence, the 20,000 data points are split into 2 subsets of 15,000 
and 5000 for training and testing, respectively. 

iv. Sliding Window Technique 
As its name suggests, this technique involves taking a subset of data 
from a given array or string, expanding it and adding in a new value to 
the subset, and removing one beginning value, hence causing the sliding 
effect. For example, consider a list of numbers from 1 to 10. 

A window of size 4 is taken. So, the sample values in the first window 

of size 4 are 1,2,3,4 as shown in the Fig. 4. The green block represents 
the  current windows,  and  the  red  block  is  the  predicted  values.  Now 
after sliding the window to the right by one number, which is nothing 
but removing the first number from the previous window and adding a 
new number on its right a new window of size 4 whose values are 2,3,4,5 
is obtained. And for every 4 values the 5th value is predicted. In this 
way, 7 batches of size 4 each can be formed. Which would result in 7*4 
= 28  points of  data, which  is  far  greater than 10. Meanwhile,  it  also 
allows us to predict 7 consecutive values. 

In the presented study, a window size of 64 was used. The generated 
time series data only consisted of 15,000 samples but through sliding 
window  technique,  14936*64  = 955904  samples  of  input  data  were 
created for the neural network so that the model had enough values to 
learn from. 

b. Time Series Forecasting using Neural Networks 
i. Model Specifications 
The  proposed  model  uses  a  3-layer  deep  sequential  feed  forward 
neural network. The first layer consists of 32 neurons, 64 samples are fed 
as input to the first layer where they are mapped to 32 samples. Now, the 
32 samples produced by the first layer are fed into second /hidden layer 
which produce 8 samples. Further, the 8 samples are fed into the last 
/output layer, giving out a single output. 

Going into further specifications, the model uses a ReLu Activation 
Function.  The  following  points  explain  the  purpose  of  an  activation 
function:  

1.  It decides whether a neuron must be fired, which gives the ANNs a 

decision-making ability. 

2. It adds non-linearity to the network, allowing the ANNs to under-

stand complex patterns.  

3.  It helps in restricting the output of a neuron to avoid computational 

issues. 

The  chosen  activation  function,  ReLU  stands  for  Rectified  Linear 
Unit.  It  outputs  zero  if  the  input  is  negative  and  acts  as  an  identity 
function if the input is positive. The equation for the ReLU function is 
given by Eq. (3) where × is the input given to the function. 

f (x) = max(0, x)

(3) 

BiomedicalSignalProcessingandControl76(2022)1037054K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

was  mentioned  earlier.  Optimizer  tunes  the  weights  and  biases.  The 
model  is  trained  until  it  does  not  show  any  further  significant 
improvements. 

In Fig. 5, the x-axis represents the epochs, and the y-axis represents 
loss.  It  can  be  seen  that  the  loss  is  reducing  as  number  of  epochs 
progress. 

After training, the model needs to be tested. To test the model the 
predict() function is run on the test data and the predictions are made. 
These values are further used to calculate the performance of the model 
i.e., accuracy. 

c. Time Series Forecasting Using LMS Adaptive Filter 
Least mean square filter is an adaptive filter where the coefficients 
are updated in accordance with the means squared error such that it is 
least, as shown in Fig. 6. 

The predicted, i.e. the future value y(n) is the dot product of previous 
values  x(n)  and  its  corresponding  coefficients  vector  W(n)  = [w1, w2,
w3⋯wn]  where  ‘n’  is  the  instantaneous  time. The  error  is  then calcu-
lated,  and  the  filter  coefficients  are  updated  accordingly.  The  output 
sample will be as given in Eq. (5). 

y(n) = W(n). x(n) =

∑n

i=1

wi*xi

(5) 

An error ‘e’ is generated to represent the deviation of the output from 
the desired value, as in Eq. (6) where ‘d’ is the desired value at instan-
taneous time ‘n’. 

e(n) = d(n) (cid:0) y(n)

(6) 

This error signal is fed back to the network to update the weights to 
effectively predict the future samples. Now, the LMS filter makes use of 
the LMS algorithm to update the weights. It is based on the instanta-
neous values of the cost function given by Eq. (7), where C, e are cost 
function and error at instantaneous time ‘n’, respectively. 

C(n) =

)

e2(n)

(cid:0)

1
2

(7) 

Now,  to  understand  the  change  in  cost  function  with  respect  to 

change in the weights the following computations are done. 

∂C(n)/∂w = e(n)*∂e(n)/∂w  

∂e(n)/∂w = x(n) (from Eq. (6) and Eq. (5)). 

∂C(n)/∂w = (cid:0) x(n)e(n)

(8) 

Eq. (8) is called as gradient approximation. Now, the updated weight 
is given by Eq. (9) where ɳ is the adaptation constant that determines the 
convergence rate [25]. 

Fig. 5. Loss vs Epochs graph.  

Fig. 6. LMS filter block.  

Adam optimizer is used for tuning the weights and biases in order to 
achieve optimal output. It is a stochastic gradient descent algorithm that 
is based on adaptive estimation of first and second order moments. The 
loss function used is Mean Squared Error. Mean squared error (MSE) is 
the most used loss function for regressions. The loss is the mean overseen 
data  of  the  squared  differences  between  true  and  predicted  values  or 
writing it as a formula. If Y = [y1, y2, y3, ⋯yn] is a vector of true values 
and Yp  = [yp
n] is the vector of the predicted values, then the 
1
means squared error is given by Eq. (4), where y is the ith  true value and 
yp  is the ith  predicted value. 

, ⋯yp

, yp
2

, yp
3

MSE =

∑n

i=1(yi (cid:0) yp
n

i )2

(4) 

The training data is fed into the model. The training is implemented 
using the fit() method. The layers implement the activation function that 

W(n + 1) = W(n) + ηC(n)

W(n + 1) = W(n) + ηX(n)e(n)

(9) 

The  above  working  is  implemented,  and  the  required  metrics  are 

computed and noted. 

4. Results and discussion 

The  accuracy  metric  used  is  Mean  Absolute  Error  (MAE).  In  time 
series analysis, the mean absolute error is a popular metric for forecast 
error. In this paper, the mean of the absolute error is first calculated, and 
then for ease of understanding the accuracy is calculated in percentage. 
The  MAE  initially  gives  us  the  extent  of  mistakes  made  in  the  pre-
dictions. It is a value between [0,1]. 0 means that there were 0 errors 
made and 1 depicts that all the predictions were wrong. To calculate 
MAE,  the  number  of  falsely  predicted  values  is  divided  by  the  total 
number of predictions ’n’. Its mathematical representation is given in 
Eq. (10) where Ypredicted  represents the predicted values and Ytrue  repre-
sents the true values. 

Fig. 7. Prediction vs Original Signal graph (using ANNs).  

BiomedicalSignalProcessingandControl76(2022)1037055K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

of  biomedical  applications,  there  is  no  place  for  far  from  perfect 
accuracy. 

c. Comparison of LMS Filter and ANNs 
Visually comparing the Figs. 7 and 8, it can be seen that although 
LMS filter is doing a decent job, ANNs overlap almost perfectly with the 
original signal. 

Getting into the numbers, Accuracy score in this case is nothing but 
the  mean  absolute  error  of  the  selected  number  of  samples.  An  ideal 
value for it would be 0. The accuracy scores stand at 0.04 and 0.2 for 
ANNs and LMS filter prediction, respectively. Clearly, ANNs are closer to 
the ideal value [5]. From the accuracy scores, accuracy percentages are 
further calculated. An accuracy percentage of 95.53% is achieved for the 
forecasting  done  by  the  ANNs  and  an  accuracy  percentage  of  79%  is 
obtained for the forecasting done by the LMS filter [14]. 

Looking at the numbers accomplished, it can surely be agreed that 
the neural networks give a better result than the adaptive filters. The 
least mean square error is considered to be a single neuron system as its 
working is similar to the way a neural network works. In spite of that, 
the  neural  networks  give  a  way  better  result  due  to  the  provision  of 
flexibility in choosing the number of neurons, number of layers, amount 
of data, optimization algorithm, loss metrics, etc. 

Further,  on  plotting  a  graph  to  depict  errors  made per  sample  for 
both the methods, it can be observed from Fig. 9 that the ANNs produced 
very little deviation from the expected results in contrast with LMS filter. 
As  discussed  earlier,  the  signal  predicts  the  noiseless  ECG  signal 
based on the noisy ECG data. Hence, signal to noise ratio (SNR) was also 
computed as shown in Eq. (12). Neural networks method achieves an 
SNR  of  29.35  dB  while  the  LMS  filter  method  gets  an  SNR  of  16  dB. 
Clearly, the neural network performs better. To recall, neural network 
was trained using the noisy data, yet it predicted the noiseless data with 
a good accuracy and also gave a decent SNR ratio. Hence, it can be seen 
that the neural network along with predicting the future values, also de- 
noises the signal. 
(

)

SNR = 10 × log

Signal Power
Noise Power

(12) 

Although  it  adds  so  much  value  in  terms  of  accuracy  and  noise 
reduction, there are a few traits that are compromised [20,22]. It is an 
exceedingly difficult task to train using neural networks as there are so 
many ways in which they can be implemented. Proper architecture must 
be first decided as per the application and then it should be improvised 
further while observing the model’s performance. Also, sometimes the 
model needs to be trained for exceptionally long time to give satisfactory 
results. 

Moreover, if the amount of data being dealt with increases or if the 

Fig. 8. Prediction vs Original Signal graph (using LMS filter).  

MAE =

∑n

i=1

|Ypredicted (cid:0) Ytrue|
n

(10) 

After calculating the MAE, the obtained value is then subtracted from 
1 and then multiplied by 100 to convert it into percentage as given in Eq. 
(11). 

Accuracy (%) = (1 (cid:0) MAE) * 100 %

(11) 

a. Accuracy of ANNs 
After a lot of training and optimization the ML model accomplishes 
an accuracy of 95.5%. The accuracy metric used is Mean Absolute Error. 
Accuracy metrics is the proportion of the total number of predictions 
that were correct. Mean Absolute Error as its name suggests is the mean 
of the absolute error, it identifies how big of an error could be made. 

In Fig. 7, the x-axis represents the samples, and the y-axis represents 
the Voltage. The red graph is of the original signal and the blue graph is 
the  forecasted  signal.  Although  it  seems  to  be  perfectly  overlapping, 
there are little peaks of blue in the graph. From the graph, it is clear that 
the Neural Networks are performing exceptionally well. 

b. Accuracy of LMS Filter 
An accuracy of 79% is achieved using the adaptive filter. The same 
accuracy metric is used as in the case of ANNs so that the comparison is 
fair. 

In Fig. 8 the x-axis represents the samples, and the y-axis represents 
the Voltage. The red line in the graph is of the original signal and the 
blue line in the graph is the forecasted signal. Although it seems to be 
doing a decent job, it does not look satiable [18]. Especially in the case 

Fig. 9. Error vs sample graph.  

BiomedicalSignalProcessingandControl76(2022)1037056K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

Table 1 
Comparison table between ANNs and LMS filter.  

Parameter 

TSF using ANNs 

TSF using LMS filter 

Accuracy 
Noise Reduction 
SNR 
Training 
Time Complexity 

95.72% 
Good 
29.71 dB 
Difficult 
High 

79% 
Poor 
16.33 dB 
Easier to implement. 
Low  

number of layers in the neural networks increases, the time complexity 
becomes  very  high  as  it  would  increase  the  number  of  computations 
required  [41].  Consider  there  are  ‘n’  inputs  followed  by  3  layers  of 
neural networks with the number of nodes in each layer as ‘m’, ‘p’, ‘q’ 
respectively. Now, the weights of the layers can be represented as Wnm, 
Wpn, Wqp. If ‘b’ is the number of training examples, then the first layer 
will need the following computations as given in Eq.13 (ignoring addi-
tion of bias for the ease of computation and understanding) where Umb is 
the output of the first layer before applying activation function while, 
Znb is the input vector. In the current study ‘b’ is given by Eq.14 where N 
is the length of signal and ‘n’ is the window size. 

Umb = Wnm × Znb

b = (N/n)

(13)  

(14) 

The above operation would have a time complexity of O(m*n*b), as 
it is a matrix multiplication. Then the activation function is applied to 
produce the inputs to the next layer as below. 

Zmb = f (Umb)

(15) 

This operation has a complexity of O(m*b) as the operation is done 
on every element in the matrix. Overall, we would get O(m*b*n) if we 
simplify it as mentioned in Eq. (16). 

[O((m*n*b) + (m*b) ) = O(m*b*(n + 1) = O(m*b*n) ]

(16) 

Similarly, for the consecutive layers, the time complexity would be O 
(m*p*b) and O(p*q*b). The final complexity would be a sum of all the 
intermediate  complexity  multiplied  by  the  number  of  epochs,  as  the 
whole process repeats for every epoch. If e is the no. of epochs then, time 
complexity would be O(eb*(nm + mp + pq)). 

With  the  current  study  as  the  context,  the  neural  network  had  to 
make 2312 multiplications, 41 additions, and application of activation 
function another 41 times in each epoch. Training an ML model may 
take several epochs before converging at a considerable accuracy on top 
of  that  hyperparameter  tuning  is  also  necessary.  Meanwhile,  for  the 

Fig. 11. Training loss.  

adaptive filters, the time-consuming tasks could be finalising the algo-
rithm to use and implementing the algorithm. Although, even adaptive 
filters require some computations and parameter tuning, they are much 
less as compared to the neural networks. The LMS filter has a constant 
time complexity of O(N) as discussed in [38]. Since, we are making a 
prediction for every window, the complexity of LMS filter specific to the 
study’s use case would be O(N*n). Hence, keeping all this in mind, it can 
be said that ANNs demand more time and attention than the Adaptive 
filters.  But  with  continuously  evolving  hardware  technology,  time 
complexity can be improved with the help of various accelerators. 

From the above discussion, the following differences between time 
series forecasting using ANNs and LMS filter can be tabulated as shown 
in Table 1. 

d. Practical Use Case Scenario 
To verify scope of the current research work in a practical scenario, 
the proposed solution was implemented on the ECG of a person suffering 
from sleep apnea. Sleep Apnea is a sleeping disorder where the patient 
experiences halt in their breathing during sleep which often leaves them 
tired even after the nap. If it is not treated, it may lead to obesity, hy-
pertension, heart attack, heart failure, etc. As the person stops breathing, 
the  heart  rate  starts  to  decrease,  or  the  person  may  even  develop 
irregular heartbeat. Hence, ECG analysis can assist diagnose sleep apnea 
and determine the causes of cardiac arrhythmias [23]. 

The ECG data was acquired from https://archive.physionet.org/cgi 
-bin/atm/ATM,  where  healthcare  professionals  and  many  others 

Fig. 10. ECG of a sleep apnea patient.  

BiomedicalSignalProcessingandControl76(2022)1037057K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

only give 3.8 dB. It is evident from the below graphs shown in Fig. 14 
that  ANNs  make  less  errors  than  the  LMS  filters  proving  to  be  more 
reliable for forecasting. 

e. Architecture Required 
To develop an ECG prediction system in real time there are four main 
layers to be implemented as shown in the Fig. 15 [24]. The first one is 
the data acquisition layer which may use different kinds of sensors to 
acquire  ECG  data  like  electrodes,  wearable  devices,  etc.  Then  second 
layer, i.e., the pre-processing layer must be carried out. In this layer the 
data  is  pre-processed,  the  required  noise  removal,  transformation  or 
compression of data are performed. Then comes the modelling and an-
alytics layer, where efforts are made to extract meaning from the data. 
Finally comes the Visualization Applications and Interface layer where 
the findings of the previous layer are delivered to the users. The users 
may be individuals or hospitals. The computing technology may differ 
based on the context. 

5. Conclusion and future scope 

The current work was aimed at finding a method to achieve highly 
accurate time series forecasting of signals with the help of neural net-
works and beat the conventional methods of using Adaptive Filters. The 
analysis proves the superiority of the ANNs over the LMS filter by giving 
an accuracy of 95.72 % over 79% accuracy achieved by the LMS filter on 
the simulated data. And on practical data, the ANN kept its behaviour 
consistent by achieving 98.68% accuracy while LMS filter offered only 
91% accuracy. Additionally, the neural network was also de-noising the 
signal while predicting. For the simulated data an SNR (Signal to Noise 
Ratio) of 29.71 dB and 16.33 dB for Neural Network prediction and LMS 
filter prediction were attained, respectively. Whereas, on real data, SNR 
values of 22.8 dB and 3.8 dB are delivered by the ANNs and LMS filter, 
respectively. 

There will always be scope for improvement in areas such as time 
series forecasting. With the help of neural networks, much complex deep 
learning  models  can  be  applied  to  achieve  exceptional  accuracy  and 
eventually make reliable forecasts. Proper implementation of the system 
may  allow  real-time  prediction  systems.  Adopting  this  approach  may 
even  eradicate  the  need  to  de-noise  the  signal  before  analyzing. 
Constantly  advancing  computational  technologies  would  complement 
biomedical applications with high compute capacity. 

Out  of  all  the  possible  applications  for  time  series  forecasting,  it 
would  be  the  most  useful  in  biomedical  applications  where  accuracy 
plays a prominent role. For example, the same forecasting can be made 
by training the ML model with real-time ECG data which will further 
allow us to track the recovery of a patient or abnormal behaviour of the 
heart maybe predicted well before, which would allow adequate time to 
take precautions. Hence, it would be apt to study the recovery of a pa-
tient  with  cardiac  abnormalities  and  forecast  the  estimated  date  of 
complete recovery or predict a heart attack or stroke. Similar approach 
may even be used on other physiological data to improve the efficiency 
of healthcare systems. 

Fig. 12. Prediction vs Original Signal graph (using ANNs).  

Fig. 13. Prediction vs Original Signal graph (using LMS filter).  

upload  data.  It  acts  a  data  hub  for  many  researchers.  The  data  was 
recorded for around 1 min with as a frequency of 100 Hz. Fig. 10 shows 
the ECG sample values plotted against their amplitude. 

For predicting with Artificial Neural Networks, the same architecture 
used for prediction on simulated ECG was used. Fig. 11 depicts the drop 
in the loss as the epochs increase. 

Even in this case, the ANNs displayed a superior performance giving 
an accuracy of 98.68%. The performance of the ANNs is plotted in the 
Fig.  12,  the  x-axis  represents  the  samples  and  y-axis  represents  their 
amplitude. 

On predictions done using LMS filter, an accuracy of 91% was ach-
ieved. The performance of LMS filter is plotted in the Fig. 13. The x-axis 
represents the samples and y-axis represents their amplitude. 

Considering the SNR, the ANNs give 22.8 dB SNR, while LMS filters 

Fig. 14. Error vs sample graph.  

BiomedicalSignalProcessingandControl76(2022)1037058K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

Fig. 15. Architecture of ECG monitoring systems.  

CRediT authorship contribution statement 

K. Ratna Prakarsha: Conceptualization. 

Declaration of Competing Interest 

The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 

References 

[1] M.G.D. Giorgi, A. Ficarella, M. Tarantino, Assessment of the benefits of numerical 
weather predictions in wind power forecasting based on statistical methods, 
Energy 36 (7) (2011) 3968–3978. 

[2] D. Gupta, Time series analysis of ECG data and unreliable forecasting, MS Thesis, 

Texas Tech University, 1997. 

[3] N.I. Santos, A.M. Said, D.E. James, N.H. Venkatesh, Modeling solar still production 
using local weather data and artificial neural networks, Renewable Energy 40 (1) 
(2012) 71–79. 

[4] C.R. Rivero, J. Pucheta, J. Baumgartner, M. Herrera, D. Pati˜no, B. Kuchen, A NN- 
based Model for Time series forecasting in function of energy associated of series, 
in: Recent Advances in Computers, Communications, Applied Social Science and 
Mathematics, Barcelona, 2011, pp. 80–86. 

[5] J. Wang, J. Wang, W. Fang, H. Niu, Financial time series prediction using elman 
recurrent random neural networks, Comput. Intell. Neurosci. (2016), https://doi. 
org/10.1155/2016/4742515, 2016, (1-14). 

[6] I.M. Carrion, E.A. Antunez, M.M.A. Castillo, J.J.M. Canals, A Prediction Method for 
Nonlinear Time Series Analysis of Air Temperature Data by Combining the False 
Nearest Neighbors and Subspace Identification Methods, in: in ACACOS’11 
Proceedings of the 10th WSEAS international conference on Applied computer and 
applied computational science, 2011, pp. 38–43. 

[7] N. Sireesha, K. Chithra, T. Sudhakar. Adaptive filtering based on least mean square 

algorithm. In 2013 Ocean Electronics (SYMPOL) (pp. 42-48). IEEE. 2013. 
[8] T. Minerva, “Wavelet Filtering for Prediction in Time Series Analysis,” in Non- 

Linear Systems and Wavelet Analysis, Tunisia, 2010, pp. 89-94. M. Khashei and M. 
Bijari, “A novel hybridization of artificial neural networks and ARIMA models for 
time series forecasting,” Expert Systems with Applications, vol. 11, no. 2, pp. 
2664–2675, 2011. 

[9] J.R. Zeidler, Performance analysis of LMS adaptive prediction filters, Proc. IEEE 78 

(12) (1990) 1781–1806. 

[10] B. Oancea, S¸ .C. Ciucu, Time series forecasting using neural networks. arXiv 

preprint arXiv:1401.1333. 2014. 

[11] E.F. Putra, R. Kosala. Application of Artificial Neural Networks To Predict Intraday 
Trading Signals, in Recent Researches in E-Activities, Jakarta, 2011, pp. 174-179. 
[12] Q. Liu, X. Cui, M.F. Abbod, S.J. Huang, Y.Y. Han, J.S. Shieh, Brain death prediction 
based on ensembled artificial neural networks in neurosurgical intensive care unit, 
J. Taiwan Inst. Chem. Eng. 42 (1) (2011) 97–107. 

[13] D. Samek, O. Bilek, J. Cerny, Prediction of grinding parameters for plastics by 

artificial neural networks, Int. J. Mech. 5 (3) (2011) 250–261. 

[14] S. Kaushik, A. Choudhury, P.K. Sheron, N. Dasgupta, S. Natarajan, L.A. Pickett, 

V. Dutt, AI in healthcare: time-series forecasting using statistical, neural, and 
ensemble architectures, Front. Big Data 3 (2020) 4. 

[15] E. Davoodi, A.R. Khanteymoori. Horse Racing Prediction Using Artificial Neural 

Networks, in Recent Advances in Neural Networks, Fuzzy Systems & Evolutionary 
Computing, Iasi, 2010, pp. 155-160. 

[16] P. Chalupa, J. Novak, V. Bobal. Predictive Control of Ancillary Services Using 

Direct Search Methods, in Proceedings of the IFAC Symposium on Power Plants 
and Power Systems Control 2009, Tampere, 2009, paper no. F5579. 

[17] B. Zhao, H. Lu, S. Chen, J. Liu, D. Wu, Convolutional neural networks for time 

series classification, Syst. Eng. Electron. 28 (1) (2017) 162–169. 

[18] S. Lee, D.B. Fambro, Application of subset autoregressive integrated moving 

average model for short-term freeway traffic volume forecasting, Transp. Res. Rec. 
1678 (1) (1999) 179–188. 

[19] R. Tripathy, U.R. Acharya, Use of features from RR-time series and EEG signals for 
automated classification of sleep stages in deep neural network framework, 
Biocybernet. Biomed. Eng. 38 (2018) 890–902. 

BiomedicalSignalProcessingandControl76(2022)1037059K. Ratna Prakarsha and G. Sharma                                                                                                                                                                                                        

[20] H.F. Nweke, Y.W. Teh, M.A. Al-garadi, U.R. Alo, Deep learning algorithms for 

human activity recognition using mobile and wearable sensor networks: State of 
the art and research challenges, Expert Syst. Appl. 105 (2018) 233–261. 

[31] A.K. Joshi, A. Tomar, M. Tomar, A review paper on analysis of electrocardiograph 
(ECG) signal for the detection of arrhythmia abnormalities, Int. J. Advanced Res. 
Electric. Electron. Instrum. Eng. 3 (10) (2014) 12466–12475. 

[21] J. Zhang, X. Zhang, J. Niu, B.X. Hu, M.R. Soltanian, H. Qiu, L. Yang, Prediction of 
groundwater level in seashore reclaimed land using wavelet and artificial neural 
network-based hybrid model, J. Hydrol. 577 (2019), 123948. 

[22] S. Javed, M. Zakirulla, R.U. Baig, S.M. Asif, A.B. Meer, Development of artificial 
neural network model for prediction of post-streptococcus mutans in dental caries, 
Comput. Methods Programs Biomed. 186 (2020), 105198. 

[23] C.W. Zywietz, V. Von Einem, B. Widiger, G. Joseph, ECG analysis for sleep apnea 

detection, Methods Inf. Med. 43 (1) (2004) 56–59. PMID: 15026838. 

[24] M.A. Serhani, T.H. El Kassabi, H. Ismail, N.A. Nujum, ECG monitoring systems: 

review, architecture, processes, and key challenges, Sensors (Basel). 20 (6) (2020) 
1796, https://doi.org/10.3390/s20061796. 

[25] Z. Zhu, X. Gao, L. Cao, D. Pan, Y. Cai, Y. Zhu, Analysis on the adaptive filter based 
on LMS algorithm, Optik – Int. J. Light Electron Opt. 127 (2016), https://doi.org/ 
10.1016/j.ijleo.2016.02.005. 

[26] Eva Volna, Martin Kotvrba, Hashim Habiballa. ECG prediction based on 

classification via neural networks and linguistic fuzzy logic forecaster. Sci. World J. 
2015 2015, 205749, 10 pages. 

[27] A.H. Ribeiro, M.H. Ribeiro, G.M. Paix˜ao, D.M. Oliveira, P.R. Gomes, J.A. Canazart, 
M.P. Ferreira, C.R. Andersson, P.W. Macfarlane, W. Meira Jr, T.B. Sch¨on, 
Automatic diagnosis of the 12-lead ECG using a deep neural network, Nat. 
Commun. 11 (1) (2020) 1–9. 

[28] J.E. Wesen, V. Vermehren, H.M. de Oliveira. Adaptive filter design for stock market 

prediction using a correlation-based criterion. arXiv preprint arXiv:1501.07504. 
2015. 

[29] M.J. Murphy, M. Isaakson, J. Jalden, Adaptive filtering to predict lung tumor 

motion during free breathing, in: H.U. Lemke, K. Inamura, K. Doi, M.W. Vannier, A. 
G. Farman, J.H.C. Reiber (Eds.), CARS 2002 Computer Assisted Radiology and 
Surgery, Springer, Berlin, Heidelberg, 2002. 

[30] R. Shavelis, K. Ozols, M. Greitans, V. Fescenko, in: October). Performance of 

Adaptive Filters for Predicting the Future Values of the Vehicle Sideslip Angle, 
IEEE, 2018, pp. 1–6. 

[32] Z. Zhao, C. Liu, Y. Li, Y. Li, J. Wang, B.S. Lin, J. Li, Noise rejection for wearable 
ECGs using modified frequency slice wavelet transform and convolutional neural 
networks, IEEE Access 7 (2019) 34060–34067. 

[33] L. Marˇs´anov´a, M. Ronzhina, R. Smíˇsek, M. Vítek, A. Nˇemcov´a, L. Smital, 

M. Nov´akov´a, ECG features and methods for automatic classification of ventricular 
premature and ischemic heartbeats: a comprehensive experimental study, Sci. Rep. 
7 (1) (2017) 1–11. 

[34] Chia-Ping Shen, Wen-Chung Kao, Yueh-Yiing Yang, Ming-Chai Hsu, Yuan-Ting Wu, 
Feipei Lai, Detection of cardiac arrhythmia in electrocardiograms using adaptive 
feature extraction and modified support vector machines, Expert Syst. Appl. 39(9) 
2012, 7845-7852, ISSN 0957-4174. 
´
Smigiel, Sandra et al. ECG signal classification using deep learning techniques 
based on the PTB-XL dataset. Entropy (Basel, Switzerland) 23(9) 2021 1121. 
[36] X. Zhai, C. Tin, Automated ECG classification using dual heartbeat coupling based 

[35]

on convolutional neural network, IEEE Access 6 (2018) 27465–27472. 

[37] Nerrand Olivier, P. Roussel-Ragot, L. Personnaz, Dreyfus G´erard, S. Marcos. Neural 
Networks and Non-linear Adaptive Filtering: Unifying Concepts and New 
Algorithms. Neural Computation. 1993. 

[38] Bei Xie; Tamal Bose, Partial Update Least-Square Adaptive Filtering, Morgan & 

Claypool, 2014. 

[39] Y. Xiao, H. Yin, T. Duan, et al., An Intelligent prediction model for UCG state based 
on dual-source LSTM, Int. J. Mach. Learn. & Cyber. (2020), https://doi.org/ 
10.1007/s13042-020-01210-7. 

[40] Y. Xiao, H. Yin, Y. Zhang, H. Qi, Y. Zhang, Z. Liu, A dual-stage attention-based 

Conv-LSTM network for spatio-temporal correlation and multivariate time series 
prediction, Int. J. Intell. Syst. 36 (5) (2021) 2036–2057. 

[41] P. Mridha, Binoy Kumar Dutta, An algorithm for analysis the time complexity for 
iterated local search (ILS), Quests J.: J. Res. Appl. Math. 7 (6) (2021) 52–54. 

BiomedicalSignalProcessingandControl76(2022)10370510
