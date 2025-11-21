# Gupta et al. - 2022 - Deep Learning (CNN) and Transfer Learning A Review

Journal of Physics:Conference Series     PAPER • OPEN ACCESSDeep Learning (CNN) and Transfer Learning: AReviewTo cite this article: Jaya Gupta et al 2022 J. Phys.: Conf. Ser. 2273 012029 View the article online for updates and enhancements.You may also likeA Ophthalmology Study on Eye Glaucomaand Retina Applied in AI and DeepLearning TechniquesS. Vaishnavi, R. Deepa and P. Nandakumar-Using Deep Learning Techniques forSandwich Panels with Truss Core DamageDetectionYabo Wang, Lingling Lu and HongweiSong-Deep learning: a branch of machinelearningP Rajendra Kumar and E B K Manash-This content was downloaded from IP address 134.95.7.248 on 21/11/2025 at 12:18AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

Deep Learning (CNN) and Transfer Learning: A Review 

Jaya Gupta1, Sunil Pathak2* and Gireesh Kumar3 

1,2Amity School of Engineering and Technology, Department of Computer Science & 
Engineering, Amity University Rajasthan, Jaipur, India. 
3Institute of Engineering & Technology, Department of Computer Science & 
Engineering, JK Lakshmipat University Jaipur, Rajasthan, India. 

corresponding author: sunilpath@gmail.com 

Abstract. Deep Learning is a machine learning area that has recently been used in a variety of 
industries.  Unsupervised,  semi-supervised,  and  supervised-learning  are  only  a  few  of  the 
strategies that have been developed to accommodate different types of learning. A number of 
experiments showed that deep learning systems fared better than traditional ones when it came 
to image processing, computer vision, and pattern recognition. Several real-world applications 
and  hierarchical  systems  have  utilised  transfer  learning  and  deep  learning  algorithms  for 
pattern recognition and classification tasks. Real-world machine learning settings, on the other 
hand, often do not support this assumption since training data can be difficult or expensive to 
get, and there is a constant need to generate  high-performance beginners  who can  work  with 
data  from a  variety of  sources. The objective of this paper is  using deep learning  to uncover 
higher-level  representational  features,  to  clearly  explain  transfer  learning,  to  provide  current 
solutions  and  evaluate  applications  in  diverse  areas  of  transfer  learning  as  well  as  deep 
learning. 

1.  Introduction 
The  term  "deep  learning"  has  recently  become  popular  in  the  computer  industry.  Many  real-time 
applications use it, and it is a division of Machine Learning as a whole. Deep Learning relies on a lot 
of data to make choices about fresh data, which is critical. Neural Networks classified as Deep Neural 
Networks  are  used  to  process  data  (DNN).  Because  neural  networks  are  commonly  used  in  deep 
learning methods, the term "deep neural networks" has gained currency. One of the most commonly 
used  deep  neural  networks  is  the  Convolutional-Neural  Network  (CNN)  [1–2].  Traditional  feature 
extraction techniques, such as SIFT, LBP, and others, require human feature extraction, but CNN does 
not. The features were extracted directly from a raw image dataset by CNN. When the networks are 
trained on a batch of photos, related features are not pre-learned. For computer vision tasks including 
object  identification,  classification,  and  recognition,  this  automated  feature  extraction  method  is  the 
most accurate learning model. Machine Learning techniques that rely on human feature extraction and 
a different algorithm to categorize each object have been around for a long time. However, in Deep 
Learning  techniques,  the  network  itself  extracts  the  features  without  involving  the  user  and  also 
classifies the items and Figure 1 depicts this. 

1

ContentfromthisworkmaybeusedunderthetermsoftheCreativeCommonsAttribution3.0licence.Anyfurtherdistributionofthisworkmustmaintainattributiontotheauthor(s)andthetitleofthework,journalcitationandDOI.PublishedunderlicencebyIOPPublishingLtd 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

Figure 1: Machine Learning vs. Deep Learning [2] 

Although  it  is  based  on  the  traditional  neural  network,  deep  learning  outperforms  it  by  a  wide 
margin.  Additionally,  DL  builds  multi-layered  learning  models  by  combining  transformations  and 
graph technology.  It has been found that the most modern DL approaches have performed well in a 
wide  range  of  applications,  including  audio  and  voice,  visual  data,  and  natural  language  processing 
(NLP) [3], [4], [5], [6]. The integrity of the input-data representation is critical to the performance of 
an ML algorithm. In comparison to a poor data representation, an appropriate data representation has 
been found to deliver better performance. Thus, feature engineering has been a major study direction 
in  ML  for  many  years,  which  has  influenced  several  studies.  Features  can  be  constructed  from  raw 
data using this method. That is not to mention how field-specific it is, and how labor-intensive it can 
be. In the computer vision environment, for example, numerous types of features have been created 
and  contrasted,  such  as  Histogram  of  Oriented  Gradients  (HOG)  [7],  Scale  Invariant  Feature 
Transform  (SIFT)  [8],  and  Bag  of  Words  (BoW)  [9].  There  is  no  limit  to  how  long  a  new  study 
direction can be explored once it is discovered to be successful. Feature extraction is done in a rather 
automated manner by the DL algorithms. For researchers, this means employing the least amount of 
human work and field expertise possible to extract discriminative characteristics [9]. Multi-layer data 
representation  architecture  is  used  by  these  algorithms  to  extract  low-level  features  while  the  high-
level  characteristics  are  extracted  by  the  last  levels.  Notably,  this  form  of  architecture  was  first 
inspired  by  AI,  which  mimics  the  process  that  occurs  in  the  brain's  primary  sensory  regions.  The 
human  brain  is  able  to  automatically  derive  data  representations  from  a  variety  of  visual  contexts. 
More  specifically,  the  classification  of  objects  is  the  result  of  this  process,  while  the  scene  data 
collected  is  the  input.  This  approach  is  modeled  after  how  the  human  brain  functions.  However,  it 
draws attention to the primary benefit of Deep Learning. Due to its enormous success, deep learning 
(DL)  is  presently  most  popular  research  trends  in  machine  learning.  The  CNN  is  the  largely 
fashionable and frequently used deep learning method. CNN's coverage of DL has made it a household 
name  [10],  [11].  Comparing  CNN  to  its  predecessors,  the  most  notable  advantage  is  that  it 
mechanically  finds  the  significant  traits  without  any  supervision  of  human,  making  it  the  most 
commonly utilized technology. 

2

 
 
 
 
 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

2.  Related Work 
The use of breast cytology pictures to automatically screen for and classify cancer has been the subject 
of numerous research proposals over the last few decades. Thus, researchers are researching nucleus 
analysis  in  order  to  gain  more  information  on  cell  classification  as  either  malignant  or  benign  [12]. 
Similarly,  cluster  segmentation  and  categorization  often  make  use  of  clustering  related  algorithms, 
circular  Hough  Transform,  and  a  variety  of  statistical  features  [13],  [14].  Histopathological  image 
analysis  methods  are  rapidly  evolving  in  medical  image  investigations.  As  a  result  of  this  need, 
automated methods are sought for that are both effective and highly dependable [15], [16]. In order to 
ensure that qualitative diagnostics are carried out accurately, such procedures must be employed. The 
output  and  precision  of  the  device  are  harmed  by  the  dynamic  presence  of  operations  such  as 
segmentation,  reprocessing,  and  attribute  mining  in  traditional  process  of  machine  learning.  The 
standard of deep learning has been promoted in order to extract the important information from raw 
images  and  allow  effective  use  for  categorization  method  in  order  to  overcome  the  challenges  of 
conventional  machine  learning  methods  [16],  [17].  Data  sets  are  processed  using  a  general  learning 
approach rather than requiring changes to the functions [18]. Biomedical image processing has seen 
significant success in recent year’s credit to deep learning that focuses on different methods, such as 
determining mitotic cells from microscopic images, brain membrane segmentation, and skin condition 
classification.  Researchers  believe  that  the  computational  deep  learning  approaches  utilized  for 
transfer learning are applicable in the actual world. Computational deep-learning transfer learning is 
summarized in Table 1. 
     Research into visual anatomy, function, psychology, and computation has led to a major framework 
of  vision  that  starts  by  retrieving  local  patterns  of  retinal  images  in  lower  visual  cortex  [e.g.,  the 
Lateral  Geniculate  Nucleus  (LGN),  V1]  and  afterwards  incorporates  the  feature  points  to  retrieve 
global  pictures  in  better  visual  areas  [e.g.  V4  and  IT]  to  start  with  [19],  [20].  The  visual  pathways' 
local-to-global  hierarchical  organization  is  a  major  inspiration  for  Convolutional  Neural  Networks 
(CNNs).  Different  CNN  levels  have  discrete  receptive  fields  that  are  represented  by  similar  visual 
neurons  which  encode  specific  features  of  a  particular  region  of  the  field  of  vision  (i.e.,  receptive 
fields).  CNNs have been the most significant advancement in the study of artificial intelligence and 
computer vision because of their origins in biology, mathematics, and computer science (AI). Human-
level classification accuracy can be achieved by training CNNs to recognize natural scenes. Facebook, 
Google's  image  search,  and  Amazon's  product  recommendations  all  use  this  system  to  properly  tag 
images. Despite their commercial success, little is understood about how CNNs classify images and 
whether  they  have  inherent  limitations.  This  information  is  necessary  in  order  to  avoid  catastrophic 
CNN  application  problems.  The  presentation  of  CNNs  transfer  learning  depends  on  image 
classification  has  been  reported  in  the  literature  [21],  [22]  however  more  research  is  needed. 
Geometric shapes were used as the datasets for training and testing the CNNs instead of actual photos 
[23, 40]. In addition to assisting the CNNs to conduct shape classification tasks, one of our primary 
goals  was  the  transferring  of  CNN  learning  from  trained  data  to  new  datasets  (i.e.  transferring 
datasets) with various shapes that shared local/global properties with the training datasets. 

3

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

Table 1. previous research on deep learning in transfer-learning experiments is reviewed 

Author 
[34] 

Title 
Time-Independent 
Prediction of Burn 
Depth using Deep 
Convolutional 
Neural Networks 

Method 
Deep learning 
techniques of 
pretrained deep 
CNNs like ResNet- 
101, ResNet-50, 
Google Net, and 
VGG-16 

deep learning 
method 

Year 
2019 

2011 

Result 
Precision 
Average = 81.66% 
Minimum = 72.06% 
Maximum = 
88.06% 
Accuracy =90.54% 
Sensitivity = 
74.35% Specificity 
= 94.25% 

Sentiment 
Classifiers produce 
better outcomes 
than existing state-
of-the-art method. 

[35] 

[36] 

[37] 

[38] 

Domain 
Adaptation for 
Large-Scale 
Sentiment 
Classification: A 
Deep Learning 
Approach 

Deep 
convolutional 
neural networks 
with transfer 
learning for 
automated brain 
image 
classification 

Bi-Transferring 
Deep Neural 
Networks for 
Domain 
Adaptation 

Clean Net: 
Transfer Learning 
for Scalable Image 
Classifier Training 
with Label Noise 

Deep learning 
method 

Recall = 96.7% 
F1-score = 92.7% 

2020 

BTDNN (Bi-
Transferring Deep 
Neural 
Network) 

Clean Net 

Achieves good 
Precision 

Label Noise 
Reduction = 41.5% 
Performance of 
Image verification 
= 47% 
Classified Images = 
3.2% 

2016 

2018 

3.  Deep Learning  
In this discipline of Machine Learning, neural networks are used as a replica of the human brain. It is 
based  on  the  human  brain's  most  fundamental  unit,  the  neuron.  Deep  learning  is  a  term  utilized  to 
explain about the study of how neurons work together to form a model of a neural network. A deep 
learning  model  is  the  final  product  of  a  neural  network.  Most  of  the  time,  in  deep  learning, 
unstructured  data  is  used  from  which  the  deep  learning  model  pulls  characteristics  on  its  own  by 
repeatedly  training  on  data.  Transfer  Learning  refers  to  the  use  of  pre-built  models  developed  for  a 

4

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

certain collection of data as a jumping-off point for building a new model using a different set of data 
and  attributes.  This  is  a  frequent  strategy  in  which  a  model  generated  for  one  task  is  utilized  as  a 
starting point to develop a model for a different activity. 

3.1.  Convolution Neural Networks 
Recent times have seen a surge in the use of Convolutional Neural Networks (CNNs). In a CNN, there 
is an, a last output layer, input layer, and a variety of further hidden layers. Convolutional layers, fully 
connected layers, normalization layers, and pooling layers are the most common types of hidden layers 
in a CNN (ReLU). For increasingly sophisticated models, additional layers might be used. There are 
numerous examples of a standard CNN described in [24] and Figure 2.  

Figure 2: Typical CNN architecture [39] 

For  a  wide  range  of  computer  vision  and  machine  learning  challenges,  CNN  architecture  has 
proven  to  be  an  outstanding  choice.  The  details  of  CNN's  training  and  prediction  are  saved  for 
subsequent sections. Modern Machine Learning applications    use this CNN model widely because of 
its  record-breaking  performance.  These  CNNs  are  built  on  a  foundation  of  linear  algebra.  Data  and 
weights  are  represented  via  matrix  vector  multiplication  [25].  For  a  picture  set,  each  layer  has  a 
different  set  of  attributes.  Using  a  facial  image  as  an  input,  for  example,  a  CNN  learns  the  basic 
characteristics  of  the  image  in  its  initial  layers,  such  as  edges,  bright  spots,  dark  spots,  and  other 
geometrical  features.  The  image's  recognizable  features,  such  as  the  eyes,  nose,  and  mouth,  will  be 
added to the following set of layers. Following that, the network may define a human face using forms 
and objects that resemble genuine human faces. The image classification process is broken down into 
smaller  segments  by  CNN,  which  matches  bits  of  the  image  rather than  the  entire  image  (features). 
Features  extracted  by  the  CNN  are  represented  by  a  3x3  grid.  Line  the  feature  up  with  the  picture 
patch in the next step, known as filtering. 

Once all the pixels have been multiplied by their corresponding feature pixels, the values are added 
up and separated by the entire amount of pixels in feature space. This process is repeated for each and 
every pixel. The feature patch contains the final value for the feature. Following that, the remaining 
feature  patches  are  subjected  to  a  similar  procedure,  which  includes  applying  the  convolution  filter 
repeatedly until one matches perfectly.  

In  the  following  layer  of  a  CNN,  called  "max  pooling,"  the  image  stack  is  reduced.  When 
attempting to pool an image, it is necessary to specify the window size (often 2x2/3x3 pixels) as well 
as the stride (e.g. frequently 2 pixels). The maximum value is afterwards recorded for each window as 
the  window  is  filtered  over  the  image  in  steps  across.  Data  can  be  reduced  in  dimension  while  still 
maintaining significant information by using max pooling. A CNN's normalization layer, also known 
as  the  Rectified  Linear  Unit  (ReLU)  procedure,  entails  setting  all  of  the  filtered  image's  negative 
values to 0. When applied to all images that have been filtered, the ReLU layer increases the model's 
nonlinear properties. Convolution, pooling, and ReLU are all used in the CNN's subsequent layering 

5

 
 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

process,  where  each  layer  feeds  the  next.  "Deep  stacking"  is  possible  when  layers  are  repeatedly 
applied. The fully connected layer, often identified as classifier, is the final layer of the CNN design. 
All of the values in this layer play a role in deciding the classification. Each intermediary layer votes 
on phantom "hidden" categories, resulting in multiple levels of fully connected layers being layered on 
top  of  one  another.  Furthermore,  each  new  layer  of  neural  networks  improves  decision-making  by 
allowing  the  network  to  learn  increasingly  more  complex  features  combinations  [26].  For  the 
convolution layer and also the values of the fully - connected layer, back propagation is utilized by the 
deep neural network. 

3.2.  Transfer Learning   
With  the  help  of  Transfer  Learning,  a  model  can  be  taught  and  refined  for  one  activity  and  then 
applied to a different one which is closely connected to it. An example of this is when what has been 
discovered and learned in one context is used to increase efficiencies and performance in another. Pre-
trained models were applied to data sets that are smaller than the actual training datasets [27]. Image 
Net was used to train the Inception-v3 model and now it is being repurposed to learn (or shift) features 
so that it can be skilled on a fresh dataset (CIFAR-10 and Caltech Faces). Initial training can be done 
using  the  Image  Net  dataset  and  Transfer  Learning  instead  of  beginning  from  scratch  with  random 
weight  initialization,  allowing  us  to  use  the  learnt  features  and  model  structure to  better fit  the  new 
dataset/task. Transfer learning of the pre-trained CNN representation is made easier with Tensor Flow. 
The topology of the CNN model is examined for picture categorization via Transfer Learning. In order 
to  identify  which  variables  influence  classification  accuracy,  researchers  must  test  and  adjust  the 
network topology and dataset features. 

3.2.1.  Transfer Learning Applications. The review shows that significant structures have been used to 
transfer learning. Document classification, multilingual text categorization, emotion classification, and 
spam  email  detection  are  just  a  few  of  the  many  uses  for  natural  language  processing  (NLP). 
Classification  of  films,  photos,  papers,  and  other  artefacts  is  a  part  of  these  procedures.  Muscle 
tiredness categorization, Wi-Fi location categorization, human actions categorization, pharmaceutical 
efficacy categorization, machine defect categorization, and cardiac arrhythmia categorization are some 
of the applications discussed by [28]. For the most part, the solutions evaluated could be applied to a 
wide  range  of  situations.  Natural  language  processing  and  image  processing  are  two  of  the  most 
commonly used application-oriented technologies. The use of suggestion systems can benefit from a 
number  of  different  types of  transfer  learning.  For  a  certain  field,  recommendation  services  provide 
users grades or ratings (e.g., books, movies). With only a few examples from the past (epidemiological 
data), the method lacks dependability. Information from another domain can be used in cases where 
there  is  insufficient  domain  data  for  reliable  forecasts  (for  example,  a  recent  release  of  a  film)  (for 
instance, using books). Using transfer learning methods and studies raised concerns [29]. 

4.  Case Studies 

4.1.  Image classification to predict whether it’s a nude or non-nude image 
Transfer learning is a concept where we train a model on one problem and then we can fine-tune and 
apply  it  on  another  similar  kind  of  problem.  Transfer  learning  is  beneficial  in  terms  of  reducing 
training  time,  also  need  for  huge  datasets  is  eliminated.  We  have  used  transfer  learning  for  image 
classification  using  a  neural  network  library  named  Keras.  With  the  help  of  web  scraping  5600 
training  images  and  1000  testing  images  were  scraped  from  the  internet  to  create  the  dataset.    Two 
existing  models,  VGG-16  and  VGG-19  were  applied  on  the  dataset.  VGG-16  model  has  16 
Convolution layers with  3x3 filter size, stride-1 and padding-same for all the layers and all the max 
pooling  layers  have  2x2  filter  size  and  stride-2  .VGG-19  model  is  very  much  similar  to  VGG-16 
model but with 3 additional conv layers. As pre-processing all the images are resized to 224x224. Both 

6

 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

the  models  were  trained  for  15  epochs  with  SGD  as  optimizer,  sigmoid  as  activation  function  and 
batch size as 128.For the said parameters VGG-16  gives 84.28 % accuracy while VGG-19  gives an 
accuracy of 85.39%. In this case VGG-19 is performing better than VGG-16 as with the increase in no 
of layers in CNN, model’s ability to fit more complex functions also increases.  

4.2.  Image  classification to predict whether it’s food image or not 
A dataset name Food-5K which consist of 5000 images with classes as food and non-food is used to 
perform image classification task. After pre-processing the images, ResNet-50 model was used where 
the final layer of the model was changed according to our dataset specifying no of classes. ResNet-50 
model  has  5  stages  and  every  stage  consists  of  a  convolution  block  and  an  identity  block.  Each 
convolution  block  and  identity  block  has  3  conv  layers.    This  model  reached  up  to  95  percent  in 
performance  for  20  epochs.  Because  we  used  transfer  learning  we  don’t  have  to  implement  CNN 
model from scratch and it saves training time. 

5.  Discussion 
Data and  model perspectives  have  been summarized in terms  of  the  implementation  procedures  and 
strategies for the transition of learning. Transfer learning applications have been tested in a number of 
research initiatives since their inception. In a wide range of contexts and activities, it was clear that 
transfer  learning  had  made  significant  strides.  Real-world  research  assignments,  on  the  other  hand, 
may have dealt with specific obstacles or issues. There may have been a resolution to some of these 
issues  while  others  remained  unaddressed.  Self-supervised  learning  is  a  relatively  new  approach  to 
education.  By  creating  and  executing  artificial  tasks  that  serve  no  purpose,  self-supervised  learning 
can  generate  labels  from  scratch  using  unlabeled  source  data  with  no  human  annotation.  If  you  use 
self-supervised learning, a typical and useful challenge is to compare patch locations and estimate the 
picture's rotation angle [30]. Automatically created labels can be acquired using this synthetic learning 
technique without the involvement of humans. Another technique for obtaining higher-quality image 
data is  smart imagery.  Image  noise  and artifacts  can be  minimized,  image  resolution  improved,  and 
shadows can be detected [31]. All of these factors enable deep learning algorithms to perform  more 
accurately  and  quickly.  Convolutionary  neural  networks  have  been  utilized  for  transfer  learning  for 
many  years,  along  with  other  deep  learning  methodologies,  in  a  variety  of  experiments.  For 
unsupervised  domain  adaptation,  an  adversarial  network  and  training  procedures  were  used  to 
implement  adversarial  network  and  training  methods  (GAN).  The  mixture  of  deep  learning  method 
with  transfer  learning  is  exemplified  here.  Transfer  learning  has  been  attempted  by  numerous 
researchers  in  order  to  improve  the  learning  process  [32].  Even  though  there  have  only  been  a  few 
studies published on medical image in this subject, we expect there will be more in the near future. 
According to one theory, the original algorithms' default parameter choices may not be appropriate for 
the  data  set  selected.  When  GFK  was  first  developed,  it  was  intended  to  be  used  for  object 
identification,  which  meant  that  it  could  be  directly  integrated  into  the  text  categorization  [33]. 
However,  this  resulted  in  an  unsatisfactory  outcome.  Based  on  these  findings,  it  appears  that  some 
algorithms may not be suitable for use with data from these fields. As a result, it is critical to select the 
right  algorithms  to  begin  the  research  process.  In  addition,  a  useful  algorithm  must  be  found  for 
practical applications. 

6.  Conclusion 
The implication is that the effect of deep learning on transfer learning has been reported for machine 
learning diagnostics. Intelligent data-driven diagnostic approaches have piqued the interest of both the 
academic community and industry. A number of machine learning techniques have been implemented 
to  predict  the  life  of  machines  and  track  their  condition  in  order  to  detect  faults.  Since  these 
accomplishments, deep transfer learning has developed into the fundamental subject of deep learning 

7

 
 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

diagnostics science. To diagnose deep learning, transfer learning methods such as mutual parameters 
and  features  are  widely  employed  in  diagnostics.  For  a  variety  of  purposes,  a  variety  of  transfer 
learning  architectures  have  been  developed.  Deep  transfer  learning  is  the  subject  of  this  research, 
which focuses on recent developments and a variety of other criteria. It is nevertheless suitable to say 
that  deep-seated  learning  diagnostics  have  previously  reached  their  testing  restrictions,  even  though 
the  efficacy  of  these  approaches  has  not  been  properly  examined.  Heterogeneous  transfer  learning 
solutions  must  be  upgraded  because  of  the  wide  variety  of  data  being  collected.  Transfer  learning 
solutions can benefit from using big data systems in conjunction with larger data sets. The range and 
size of data sets used to transfer learning systems is an important subject for future research. This is 
not  the  only  area  of  study  that  deals  with  the  issue  of  label  space.  This  topic  has  the  potential  to 
become increasingly important as fresh data sets are collected and create publicly available. This is a 
promising field for further research, as there are only a few examples of transfer learning algorithms in 
the literature that deal with the unlabeled source and unlabeled goal data condition. 

References 
[1]  N., Jain, V., & Mishra, A. (2018). An Analysis Of Convolutional Neural Networks For Image 

Classification. Procedia Computer Science, 132, 377-384.  

[2] 

Fukushima,  K.  (1988).  Neocognitron:  A  hierarchical  neural  network  capable  of  visual  pattern 

recognition. Neural Networks, 1(2), 119-130.  

[3] 

Pak,  M.,  &  Kim,  S.  (2017).  A  review  of  deep  learning  in  image  recognition.  2017  4Th 
Information  Processing 

International  Conference  On  Computer  Applications  And 
Technology (CAIPT).  

[4]  Bird,  J.,  Faria,  D.,  Manso,  L.,  Ayrosa,  P.,  &Ekárt,  A.  (2021).  A  study  on  CNN  image 
classification  of  EEG  signals  represented  in  2D  and  3D.  Journal  Of  Neural  Engineering, 
18(2), 026005.  

[5]  Rawat, W., & Wang, Z. (2017). Deep Convolutional Neural Networks for Image Classification: 

A Comprehensive Review. Neural Computation, 29(9), 2352-2449.  

[6]  Loussaief,  S.,  &Abdelkrim,  A.  (2018). Machine  Learning  framework  for image  classification. 
Advances In Science, Technology And Engineering Systems Journal, 3(1), 01-10.  
[7]  Maggiori,  E.,  Tarabalka,  Y.,  Charpiat,  G.,  &Alliez,  P.  (2017).  High-Resolution  Aerial  Image 
Labeling  With  Convolutional  Neural  Networks.  IEEE  Transactions  On  Geoscience  And 
Remote Sensing, 55(12), 7092-7103.  

[8]  Alom, M., Hasan, M., Yakopcic, C., Taha, T., &Asari, V. (2018). Improved inception-residual 
convolutional  neural  network  for  object  recognition.  Neural  Computing  And  Applications, 
32(1), 279-293.  

[9]  CIFAR-10 and CIFAR-100 datasets. Cs.toronto.edu. (2022). Retrieved 29 January 2022, from 

https://www.cs.toronto.edu/~kriz/cifar.html 

[10]  Dutta, S., Manideep, B., Rai, S., &Vijayarajan, V. (2017). A comparative study of deep learning 
models  for  medical  image  classification.  IOP  Conference  Series:  Materials  Science  And 
Engineering, 263, 042097.  

[11]  Pouyanfar,  S.,  Sadiq,  S.,  Yan,  Y., Tian,  H., Tao,  Y., &  Reyes,  M. et  al.  (2019).  A  Survey  on 

Deep Learning. ACM Computing Surveys, 51(5), 1-36.  

[12]  Toprak,  A.  (2018).  Extreme  Learning  Machine  (ELM)-Based  Classification  of  Benign  and 

Malignant Cells in Breast Cancer. Medical Science Monitor, 24, 6537-6543.  

[13]  Zebari, D., Zeebaree, D., Abdulazeez, A., Haron, H., & Hamed, H. (2020). Improved Threshold 
Based  and  Trainable  Fully  Automated  Segmentation  for  Breast  Cancer  Boundary  and 
Pectoral Muscle in Mammogram Images. IEEE Access, 8, 203097-203116.  

[14]  Tiwari, A., Srivastava, S., & Pant, M. (2020). Brain tumor segmentation and classification from 
magnetic  resonance  images:  Review  of  selected  methods  from  2014  to  2019.  Pattern 
Recognition Letters, 131, 244-260.  

8

 
 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

[15]  Kong,  L.,  Li,  C.,  Ge,  J.,  Zhang,  F.,  Feng,  Y.,  Li,  Z.,  &  Luo,  B.  (2020).  Leveraging  multiple 
features for document sentiment classification. Information Sciences, 518, 39-55.  
[16]  Asaad Zebari, N., Asaad Zebari, D., QaderZeebaree, D., & Najeeb Saeed, J. (2021). Significant 
features  for  steganography  techniques  using  deoxyribonucleic  acid:  a  review.  Indonesian 
Journal Of Electrical Engineering And Computer Science, 21(1), 338.  

[17]  Affonso, C., Rossi, A., Vieira, F., & de Carvalho, A. (2017). Deep learning for biological image 

classification. Expert Systems With Applications, 85, 114-122.  

[18]  Kim,  H.,  Ahn,  E.,  Shin,  M.,  &  Sim,  S.  (2018).  Crack  and  Noncrack  Classification  from 
Concrete  Surface  Images  Using  Machine  Learning.  Structural  Health  Monitoring,  18(3), 
725-738.  

[19]  Hubel,, D., & Wiesel, T. (1977). Ferrier lecture  - Functional architecture of macaque monkey 
visual cortex. Proceedings Of The Royal Society Of London. Series B. Biological Sciences, 
198(1130), 1-59.  

[20]  Longuet-Higgins, H. (1982). A Theory of Vision: Vision . A Computational Investigation into 
the Human Representation and Processing of Visual Information. David Marr. Freeman, San 
Francisco, 1982. xviii, 398 pp., illus. $29.95. Science, 218(4576), 991-992.  

[21]  Liu,  S.,  John,  V.,  Blasch,  E.,  Liu,  Z.,  &  Huang,  Y.  (2018).  IR2VI:  Enhanced  Night 
Environmental  Perception  by  Unsupervised  Thermal  Image  Translation.  2018  IEEE/CVF 
Conference On Computer Vision And Pattern Recognition Workshops (CVPRW).  
[22]  Han,  D.,  Liu,  Q.,  &  Fan,  W.  (2018).  A  new  image  classification  method  using  CNN  transfer 
learning and web data augmentation. Expert Systems With Applications, 95, 43-56.   
[23]  Zheng, Y., Huang, J., Chen, T., Ou, Y., & Zhou, W. (2019). CNN classification based on global 

and local features. Real-Time Image Processing And Deep Learning 2019.  

[24]  Arun,  P.,  &Katiyar,  S.  (2013).  A  CNN  based  Hybrid  approach  towards  automatic  image 

registration. Geodesy And Cartography, 62(1), 33-49.  

[25]  Audhkhasi, K., Osoba, O., &Kosko, B. (2016). Noise-enhanced convolutional neural networks. 

Neural Networks, 78, 15-23.  

[26]  Gao,  Y.,  &Mosalam,  K.  (2018).  Deep  Transfer  Learning  for  Image-Based  Structural  Damage 
Recognition. Computer-Aided Civil And Infrastructure Engineering, 33(9), 748-768.  
[27]  Larsen-Freeman,  D.  (2013).  Transfer  of  Learning  Transformed.  Language  Learning,  63,  107-

129.  

[28]  Ling  Shao,  Fan  Zhu,  &Xuelong  Li.  (2015).  Transfer  Learning  for  Visual  Categorization:  A 
Survey. IEEE Transactions On Neural Networks And Learning Systems, 26(5), 1019-1034.  
[29]  Li, X., Xiong, H., Chen, Z., Huan, J., Liu, J., Xu, C., & Dou, D. (2022). Knowledge Distillation 
with Attention for Deep Transfer Learning of Convolutional Networks. ACM Transactions 
On Knowledge Discovery From Data, 16(3), 1-20.  

[30]  Huang,  C.,  Lan,  Y.,  Zhang,  G.,  Xu,  G.,  Jiang,  L.,  &  Zeng,  N.  et  al.  (2020).  A  New  Transfer 
Function for Volume Visualization of Aortic Stent and Its Application to Virtual Endoscopy. 
ACM Transactions On Multimedia Computing, Communications, And Applications, 16(2s), 
1-14.  

[31]  Huang, C., Tian, G., Lan, Y., Peng, Y., Ng, E., & Hao, Y. et al. (2019). A New Pulse Coupled 
Neural  Network  (PCNN)  for  Brain  Medical  Image  Fusion  Empowered  by  Shuffled  Frog 
Leaping Algorithm. Frontiers In Neuroscience, 13.  

[32]  Huang,  C.,  Xie,  Y.,  Lan,  Y.,  Hao,  Y.,  Chen,  F.,  Cheng,  Y.,  &  Peng,  Y.  (2018).  A  New 
Framework for the Integrative Analytics of Intravascular Ultrasound and Optical Coherence 
Tomography Images. IEEE Access, 6, 36408-36419.  

[33]  Jiao, W., Wang, Q., Cheng, Y., & Zhang, Y. (2021). End-to-end prediction of weld penetration: 
A  deep  learning  and  transfer  learning  based  method.  Journal  Of  Manufacturing  Processes, 
63, 191-197.  

[34]  Cirillo,  M.,  Mirdell,  R.,  Sjöberg,  F.,  &  Pham,  T.  (2019).  Tensor  Decomposition  for  Colour 

Image Segmentation of Burn Wounds. Scientific Reports, 9(1).  

9

 
 
 
 
 
 
AICES-2022
Journal of Physics: Conference Series

2273 (2022) 012029

IOP Publishing
doi:10.1088/1742-6596/2273/1/012029

[35]  Bordes, A., Glorot, X., Weston, J., &Bengio, Y. (2013). A semantic matching energy  function 

for learning with multi-relational data. Machine Learning, 94(2), 233-259.  

[36]  Kaur, T., & Gandhi, T. (2020). Deep convolutional neural networks with transfer learning for 

automated brain image classification. Machine Vision And Applications, 31(3).  

[37]  Yang,  H.,  Zhuang,  T.,  &Zong,  C.  (2015).  Domain  Adaptation  for  Syntactic  and  Semantic 
Dependency  Parsing  Using  Deep  Belief  Networks.  Transactions  Of  The  Association  For 
Computational Linguistics, 3, 271-282.  

[38]  Xie, X., Yang, L., & Zheng, W. (2016). Learning object-specific DAGs for multi-label material 

recognition. Computer Vision And Image Understanding, 143, 183-190. 

[39]  (2022).Retrieved 29 January 2022, from https://www.mathworks.com/discovery/convolutional-

neural-network-matlab.html. 

[40]  Gupta.  J,  Pathak.  S.,  Kumar.  G.,  “  Bare  Skin  Image  Classification  using  Convolution  Neural 
Netowrk”, International Journal of Emerging Technology and Advanced Engineering, Vol. 
12,Issue 01, 2022. 

10
