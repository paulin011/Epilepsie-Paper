# Sewak et al. - 2020 - An overview of deep learning architecture of deep neural networks and autoencoders

An Overview of Deep Learning Architecture of Deep Neural
Networks and Autoencoders

Mohit Sewak* Sanjay K. Sahay†and Hemant Rathore‡

Abstract

Recently deep learning has shown great progress in multiple ﬁelds, but to per-
form optimally, it requires the adjustment of various architectural features and
hyper-parameters. Moreover, deep learning could be used with multiple varieties
of architecture aimed at different objectives, e.g., autoencoders are popular for
un-supervised learning applications for reducing the dimensionality of the dataset.
Similarly, deep neural networks are popular for supervised learning applications
viz., classiﬁcation, regression, etc. Besides the type of deep learning architecture,
some other decision criteria and parameter selection decisions are required for de-
termining the number of layers, size of each layer, activation and loss functions for
different layers, optimizer algorithm, regularization, etc. Thus, this papers aims
to cover different choices available under each of these major and minor decision
criteria for building a neural network and training it optimally to effectively serve
the objectives, e.g., malware detection, natural language processing, image recog-
nition, etc.

Deep Learning, Deep Neural Networks, Autoencoders, Activation Function, Loss
Function, Optimizer.

1

Introduction

According to Geoffrey Hinton (considered as the father of Deep Learning), deep learn-
ing (DL) allows computational models that are composed of multiple processing layers
to learn representations of data with multiple levels of abstraction [1]. Due to this fact,
DL has shown wide adoption in various ﬁelds with complex features, where an ab-
stracted representation may hugely alleviate downstream processing and analytics, e.g.,
we applied the different layer of DNN and auto-encoder (AE) to improve the malware
detection accuracy [2], [3].

DL method is a multiple level representation-learning methods, obtained by com-
posing non-linear but simple modules that change the representation at one level (an
raw input at the start level) into a representation at a higher, slightly more abstract
level. The main aspect of DL is that the features in these layers are not designed by
the engineers, but are learned from the data by using a general-purpose learning pro-
cedure. This formulation of DL, also called deep neural networks (DNN) is useful

*BITS, Pilani, Dept. of CS & IS, Goa Campus, Goa, India, Email: p20150023@goa.bits-pilani.ac.in
†BITS, Pilani, Dept. of CS & IS, Goa Campus, Goa, India, India, Email: ssahay@goa.bits-pilani.ac.in
‡BITS, Pilani, Dept. of CS & IS, Goa Campus, Goa, India, Email: hemantr@goa.bits-pilani.ac.in

1

for the data where features are not related from a domain perspective. For text, and
tempo-spatial or other series data, DL architectures like Recurrent Neural Networks
[4], or its variants like Long-Short Term Memory [5], and Gated Recurrent Unit [6]
are more popular. This is because, in regular DNN, backpropagation breaks down, due
to the recurrent loop, which is solved by a technique called Backpropagation Through
Time [7]. Similarly, for image and video, DL architectures like Convolutional Neural
Networks (CNN) work better as they can understand the spatial correlation of pixel
intensities in an image better, and in a more efﬁcient manner [8].

The remainder of this paper is organized as follows. In the next section, we discuss
the architecture of the DNN which determines the number of layers and neurons/nodes
in each layer. Section 3 covers the different types of activation functions which convert
the input of the neuron to an output, and also determine the function/activation for neu-
rons in each layer of the considered architecture. Section 4 discusses the different types
of loss function which ensures that the output is inline as per the objective by measur-
ing and optimizing the loss between the prediction and output. Section 5 discusses
how to minimize the loss efﬁciently and in an optimal manner while avoiding some
of the pitfalls like getting stuck in local minima and ravines. Besides the four major
criteria (Section 2 -5) which determines the network and its conﬁguration as a whole,
it is equally important to determine how to feed data into the network for training and
hyper-parameters viz., batch size, epochs, and dropout regularization to avoid over-
ﬁtting and ensuring that the model is well trained, and has been discussed in section
6. Section 7 covers the architecture and different loss functions of the auto-encoders.
Finally, in section 8 we summarize our paper.

2 Deep Neural Network Architecture: Layers and Nodes

A DNN (ﬁg. 1) consists of Artiﬁcial Neural Network (ANN) nodes in different hierar-
chical layers. These layers consist of input layer, hidden layers, and the output layer.
The number of input and output layer is ﬁxed similar to the sequential models, and
the number of nodes in these 2-layers are also ﬁxed. The input layers contain as many
nodes as the number of features in the input, and when used as a classiﬁer, the output
layer contains as many nodes as the number of classes.

There could be one or more hidden layers in the network, and the number of nodes
in each hidden layer may differ. Though recently there has been some work to provide a
scientiﬁc way using Genetic Algorithms [9, 10] to determine the number of hidden lay-
ers and nodes in each hidden layer, but mostly it is a matter of experience and trial-and-
error. Heuristics do exist, which suggests that more the non-linearity and complexity in
the data, more should be the number of layers to extract the important representations
from such non-linear/complex data. A 2-hidden layer network is capable to represent
an arbitrary decision boundary to certain accuracy with rational activation functions
and could approximate any smooth mapping with the accuracy [11].

The heuristics approach on the number of nodes in a hidden layer suggests that,
these number of nodes should remain between the number of input and output (or the
next layer) layer nodes. Some heuristics gives a roughly around two-third number of
nodes of the input layer, plus the number of nodes of the output layer, others suggest

2

Figure 1: A schematic of a sequential DNN with two hidden layers.

an upper bound of two times the number input layer nodes for the number of hidden
layer nodes. [11].

3 Activation Functions

In ANN activation function is used to convert an input signal of a node to an output
signal, and can be given as

Y = Activation(W T X + c)

where,
Y = Output,
W T = Transpose of the weight vector W of the neuron,
X = Input vector to the neuron, and
c = bias of the neuron.

For example, if we have a dataset containing n records (R1, ..., Rn), and each
record contains m features (Xr,1, ..., Xr,m), where r is the rth record in the dataset.
Then taking an instance of the ith record, whose features are given by a [1, m] matrix
[Xi,1, ..., Xi,m], which is an input to the nth (say) neuron in the lth layer represented
by Nl,n, whose weight vector W is given by another [1, m] matrix (W1, ..., Wm), with
a bias of bl,n, then the output Yi,(l,n) for the ith record from this neuron under a given
activation function f nA is given by

Yi,(l,n) = f nA(W1Xi,1 + ... + WmXi,m + bl,n)

Since training in neural networks happens through backpropagation, which requires
the activation function should be differentiable in the entire range of input. Another

3

requirement for the activation function is that it should be monotonic (continuously
increasing or decreasing in the range of the input).

The activation function for hidden and inputs layers are mostly different from that
of the output layer, as the primary function of the activation function in the input or
hidden layers is to enable non-linearity, whereas that of the output layer of a DNN used
for classiﬁcation is to give standardized class probabilities for the each class. Some of
the popular activation functions used in DL are Softmax [12], Sigmoid [13], Tanh [13],
Linear (Identity) [14], Rectiﬁer Linear Unit [15] and Exponential Linear Unit [16].

3.1 Softmax Activation

As discussed above, the output layer for a classiﬁcation, DNN should provide the class
probability for each class under consideration, and for this a softmax function is used
for its activation. As per softmax function, the probability of the output y to assume a
particular class c out of total K classes, provided the input feature vector x is given as

P (y = c|x) =

exT wj
k=1 exT wk

(cid:80)K

where, xT is the transpose of the weight vector x.

3.2 Sigmoid and Tanh Activations

There is a lot of variation available for the activation of input and hidden layers. In
traditional artiﬁcial neural networks sigmoid, hyperbolic tangent activation were used,
which is given as

Sigmoid(x) =

1
1 + e−x
2

Tanh(x) =

1 + e−2x − 1

If these activation were used in the hidden layers, it will be difﬁcult to train a
DNN, because the neurons would get stuck in the upper and lower areas of sigmoid
and hyperbolic tangent functions. This is due to the vanishing or exploding gradient
problem in such networks. This drawbacks contributes to the fact that DL could not
be practically adopted to solve complex problems until new activation functions were
discovered. In this, sigmoid functions could also be used as activation function for the
last layer, e.g., in the binary classiﬁcation.

3.3 Linear and Identity Activation

As we discussed earlier, for classiﬁcation problems sigmoid (binary classiﬁcation), and
softmax (multinomial classiﬁcation) activation could be used, as these provide steep
non-linear separation between the classes. But for regression problems (predicting
continuous variable output), Linear activation may be required. Identity activation falls

4

in the class of linear activation and is used in DL as activation for the last layer for a
regression problem for predicting a continuous output [14].

Identity(x) =

(cid:88)

i

xiwi

where, xi and wi corresponds to the ith element of input and weight vectors.

3.4 Rectiﬁer Linear Unit Activation

Rectiﬁer Linear Unit (ReLU) activation, solved the vanishing and exploding gradient
problem as highlighted above as the derivative of a unit for positive values [17], and
many of the popular networks use this as the activation for input/ hidden layers. ReLU
function behaves like a identity function f (x) = x for all positive x, and 0 otherwise,
given as

ReLU (x) = max(0, x)

Though the differential of ReLU is not a continuous function, it is deﬁned in the entire
range of input (1 for positive x, and 0 for otherwise). As ReLU continues to be the most
popular activation function for most of the DL architecture, hence variants of ReLU are
developed, such as

3.4.1 Leaky ReLU

In ReLU, the differential for negative x is deﬁned as 0, that means no gradient for this
range of x, which makes training through backpropagation challenging in the absence
of a gradient. Leaky ReLU [18] tries to solve this by changing ReLU slightly as

LeakyReLU(x) =

(cid:40)

ax if x < 0
if x ≥ 0
x

where, a is a constant, usually taken 0.01.

3.4.2 Randomized Leaky ReLU

In the above formulation for Leaky ReLU, the value of a is ﬁxed. If instead it is allowed
to change randomly, it is called Randomized Leaky Rectiﬁer Linear Unit (RReLU)[19],
and in such a case, its range becomes (−∞, ∞). Both of the above derivatives of ReLU
are not only continuous and monotonic but also have a monotonic gradient.

3.4.3 Parametrized ReLU

In Parametrized Rectiﬁer Linear Unit (PReLU) [20], as the name suggests, the param-
eter a of the Leaky ReLU is optimized during the training processes.

5

3.5 Exponential Linear Unit

Although the above variants of ReLU, does solve the problem of dead or not activated
neurons, there still exists another problem in them, which is mean shift. Since the
activations are predisposed to positive outputs, their mean is not zero centered, which
cause a problem in learning. To solve this problem, either a Batch Normalization [21]
layer could be applied after the activation, or else, Exponential Linear Unit (ELU)
could provide a computationally more efﬁcient solution to overcome this drawback,
and is deﬁned for positive α as

ELU (x) =

(cid:40)

x
α(exp(x) − 1)

if x > 0
if x ≤ 0

The value to which an ELU saturates for negative net inputs is controlled by the ELU
hyperparameter α. The sigmoid and tanh function are contractive almost everywhere,
but in ELU, since it’s gradient is unity it is not contractive. ELU is also able to over-
come the vanishing gradient problem as the positive part of the gradient this function
is identity.

After conﬁguring the architecture of DNN, the activation/ function of the neurons
in each layer of the architecture has been determined. Therefore, this section covers the
different types of activation functions which convert the input of the neuron to output
and for the intermediate layer. To ensure that the output is inline as per the objective, in
the next section we discuss the loss function that can be used to measure and optimize
the loss between the prediction and output under different conditions.

4 Loss Functions

The objective to train a neural network is to identify the weights (and other parameter
values) that minimizes the loss between the expected and the predicted output of a neu-
ral network, as determined by its loss function. Most of the loss functions as used in
different popular machine learning algorithms could also be used in DL, the applica-
bility of the same depends upon the target function distributions. In case of categorical
target variable, e.g., in binary classiﬁcation, commonly used loss functions are [22]

• L1 loss: (cid:107)y − o(cid:107)

• L2 loss: (cid:107)y − o(cid:107)2

• Expectation Loss: (cid:107)y − p(o)(cid:107)

• Regularized Expectation Loss: (cid:107)y − σ(o)(cid:107)2
• Hinge Loss: (cid:80)

2 − ˆyjoj)

j max(0, 1
• Squared Hinge Loss: (cid:80)
• Cross Entropy Loss: -(cid:80)

j max(0, 1

2 − ˆyjoj)2

j yj log σ(0)j

6

• Squared log Loss: -(cid:80)

j[yj log σ(0)j]2

where,
y = the true output/label vector (one hot encoded) consisting of j elements,
ˆy = true output label (categorical/class),
o = the output vector of the last layer (consisting of j elements), and
σ(o) = expectation of the probability distribution of output vector o.

Of the above loss functions, the cross-entropy loss (binary cross entropy for binary
classiﬁcation and categorical cross-entropy for multi-class classiﬁcation) is the most
popular, though some experiments indicates that hinge loss [23] and squared hinge
loss [24] could also be a good candidate to use as a loss function in DL. Some studies
also indicate that expectation loss might be a much better loss function to deal with the
noisy data [25].

5 Optimizers

In the previous section, we discussed that we need to minimize the loss for achieving
a good training for the DNN. This task of minimization of the objective function is
what the optimizer has to do in an ‘optimal’ manner. The optimizer does this by ﬁnd-
ing a good minimum for the loss function or the objective function. The computation
efﬁciency to reach this optimization is just one of the aspect that determines the ef-
fectiveness of the optimizer. Other aspects could be how robust it is, and how well it
performs under different conditions like ridges in gradient topology and skewed gradi-
ents parameters. Since most of the optimizers used in the DL are built over gradient
descent. Therefore ﬁrst we will discuss the gradient descent for academic understand-
ing, and then cover some more popular optimizers built on it.

5.1 Gradient Descent

For a DNN, the loss function J(θ) is a function of the weights that need to be optimized,
parameterized as a vector θ ∈ IRd. Since here optimization refers to minimization of
a convex function, so we need to ﬁnd the gradient of this function and move in the
opposite direction of it till we ﬁnd a (hopefully global) minima. The gradient with
respect to the weight vector θ is deﬁned as ∆θJ(θ).

The learning rate (η) determines the correction in the opposite direction of the gra-
dient that we do in each iteration. If the iteration happens over the complete data-set,
then it is called the Batch Gradient Descent (θ = θ − η.∆θJ(θ)), else, if the cor-
rection happens in an stochastic manner over every training sample (xi, yi), then it is
called a Stochastic Gradient Descent (θ = θ − η.∆θJ(θ; xi, yi)), and if the same
happens over a combination of both, i.e., a mini-batch of data n (say) samples, then it
is called a Mini-Batch Gradient Descent (θ = θ − η.∆θJ(θ; xi:i+n, yi:i+n)).

7

5.2 Nesterov accelerated gradient

If the gradient hyper-plane curves changes with different parameters (ravines), then
there may be an steep correction across some of the parameters with high gradient,
thus leading to hunting (missing the local minima and repeatedly going on opposite
direction of the convex slope) across the minima or conversely converging very slow
in the direction of the parameter whose gradient is too small. To overcome this effect
the nesterov accelerated gradient (NAG) [26], use the momentum γ, and the gradient
update of the last time step (vt−1) to update the current gradient (vt) using the look-
ahead gradient (θ − γvt−1) as vt = γvt−1 + η∆θJ(θ − γvt−1)

5.3 Adaptive Gradient

Using momentum, NAG does solve the problem of uneven gradient slope across the el-
ements of gradient hyperplane, but its an indirect approach. Adaptive Gradient (ADA-
GRAD) [27] does the same this directly. Unlike previous methods, which use the same
learning rate η for all the elements of the vector θ, ADAGRAD updates each element i
.gt,i, where gt,i is the gradient
(θt,i) of θ at step t differently as θt+1,i = θt,i −
of element i at step t, and Gt,ii ∈ Rd×d is the element (i × i) of the diagonal matrix
G at time t. Each element of G is given by Gt,ii = (cid:80)t
s,i and (cid:15), a small constant,
helps in preventing divide by zero issues. ADAGRAD has proved very effective over
large DL networks as the ones used to generate word embedding for NLP [28] and by
Google for classiﬁcation of objects in YouTube videos [29].

s=1 θ2

η√

Gt,ii+(cid:15)

5.4 ADADELTA and RMSProp

Both ADADELTA and RMSProp [30] tries to improve the ADAGRAD’s weakness
of working on the squares of all the gradient element across each step from the be-
ginning, which continuously decreases the effective learning rate monotonically in
an aggressive manner. Both of these proposes a ﬁxed step/time period across which
this effect should last (based on running average). ADADELTA replaces the diag-
onal matrix Gt with E[g2]t given as E[g2]t = λE[g2]t + (1 − λ)g2
t , where λ is
the exponential decay coefﬁcient. RMSProp sets the value of λ as 0.9, such that
E[g2]t = 0.9E[g2]t + 0.1g2
t .

5.5 Adaptive Moment Estimation

Adaptive Moment Estimation (ADAM) [31] takes ideas of adaptive learning rate from
ADAGRAD/ ADADELTA/ RMSProp and moment estimation for decaying the past
gradient changes. It use both the ﬁrst moment mt and second moment vt of the gradient
at time t to update at each step exponentially as mt = β1mt−1 + (1 − β1)gt, and
vt = β2vt−1 + (1 − β2)g2
t , where β1 and β2 are exponential decay coefﬁcients for
the ﬁrst and second order moments. The gradient is updated in each step as θt+1 =
θt − η√
ˆmt, where ˆvt and ˆmt are the bias corrected estimates of mt and vt, given

ˆvT +(cid:15)

8

and ˆvt = vt
as ˆmt = mt
1−βt
1−βt
2
1
0.9 and 0.999 respectively, and for (cid:15) is 10−8.

. Here, the suggested default values for β1 and β2 are

6 Training Considerations: Batches, Epochs & Dropout

As discussed in previous section, we use mini-batches to train a DNN, wherein the
whole data is divided into batches of ﬁxed sized. A complete batch optimization would
lead to sharp minima and poor generalization, and is not suitable for stochastic pro-
cess, and a complete stochastic/online process makes training very noisy [32]. For
effective training the other hyperparameter has to be considered are batch size, epochs
and dropout regularization.

6.1 Batch-size

As deep learning requires a lot of data to train, therefore, a large batch size may not
be optimal to hold in memory, and can lead to over-ﬁtting, where as too small batches
may require a large time to converge and may be noisy. A batch size of 32-512 samples
[32] is found to be used in general practice in deep learning.

6.2 Epochs

As mentioned earlier, a single pass over data may not be optimal, so multiple passes
over data are made for the purpose of training, and each pass over the complete data
will required (cid:100) n
b size (cid:101) batches, where n is the number of data records and b size is the
batch size. Besides prior experience and heuristics, the number of epochs are deter-
mined seeing the convergence plots of training/test error as the epoch proceed during
the training process. The weights of the network could be saved intermittently (check-
points) and the network restarted from last checkpoint/trained-state for further epochs,
if required, for further optimization of weights.

6.3 Dropout Regularization

Overﬁtting is an issue in machine learning, where during the training, model not only
learn pattern of the data, but also start ﬁtting the noise. Hence, not able to perform well
on the test data or in real-life applications. For other machine learning algorithms like
decision tree, ensembling is a very good technique to avoid overﬁtting, e.g., random
forest use it effectively. But since DL networks are hard to train, ensembling may not
be an efﬁcient method to be applied. Therefore DL use a technique called dropout
for regularization [33], in which during training, randomly some nodes from the given
layer would be dropped/switched-off. The proportion of the nodes being dropped-
out could be controlled by a parameter which determines the number of nodes to be
dropped in a particular layer. It gives a network that has smaller weights and has a
similar effect of using multiple thinned networks as in case of ensembling. Dropout is

9

applied only during training and all the nodes are retained during testing. Sometimes
this may lead to smaller test loss than training loss for some epochs.

7 Autoencoders

Autoencoders [34] was ﬁrst introduced in 1986 by Geoffrey Hinton [35] are DL ar-
chitectures for unsupervised learning. They are mainly used for data compression and
learning useful abstraction of data. There are generative or variational autoencoders as
well which can learn latent model of the data for the purpose of generating new data,
or as de-noising autoencoders to minimize the noise from the data. Autoencoders can
also be applied to generic or image data also in the form of CNNs [8]. In this section
we cover the autoencoders that are used for the dimension reduction.

7.1 Architecture

Autoencoder (ﬁg. 2) consists of a network of encoder and decoder. During training
both encoders and decoders are used. But when applied to new data for the reduction
of dimension, then only encoder are used. Like any DL architecture, AE works in layers
of neurons, and are trained using backpropogation. The layers are divided into different
encoder and decoder layers. The input is connected to the ﬁrst encoder layer. In each
subsequent layer of the encoder, the number of neurons are reduced till we reach the
last encoded layer, which has the least number of neurons, representing the bottleneck
features. The input are transformed until this layer represents the reduced dimension
of the data that is capable of representing the maximal signals in the data. After this
layer, the decoder layers are set, in which the number of neurons are increased in each
layer, until the output layer which has the same number of neurons as the input.

7.2 Loss Function

The objective while training the autoencoder is to minimize the reconstitution error
between the output (the last decoder layer) and the input (the ﬁrst encoder layer), which
ensures that even after compressing the data through the encoders, the bottleneck layers
have learn most of the relevant patterns in the data, such that it could be re-constituted
again effectively after decoding. For continuous input, squared error loss could be one
of the loss functions for AE, and is given as

L(x, x(cid:48)) = (cid:107)x − x(cid:48)(cid:107)2 = (cid:107)x − W (cid:48)(W x + b) + b(cid:48)(cid:107)2

where,
x is the input,
W, b is the weight vector and bias of the encoder, and
W (cid:48), b are the weight vector and bias of the decoder.

10

Figure 2: A schematic of an AE showing an encoder connected to the input layer
leading to bottleneck layer/ features followed by decoder leading to the reconstituted
output layer.

When considered in batches of n samples, the mean square error for the batch could

be computed by the formulae

M SE =

1
n

n
(cid:88)

i=1

L(xi, x'i)

For categorical input, cross-entropy loss as discussed in section 4 could be used.

8 Summary

There exists work that covers individual aspects of DL like loss functions, activation,
etc., but to the best of our knowledge, this is the ﬁrst paper that covers all the archi-
tectural aspects of the two most basic DL networks, i.e., DNN for supervised learning
and autoencoders for un-supervised learning. This paper started with step of choosing
the DL type based on requirement, then logically leading to the decision of selecting
the number of layers in the selected network, then structurally leading to the aspects
related decisions for each layer, namely the number of nodes and activation function
for each layer, then we cover the mathematical aspects for training the selected net-
work, namely the selection of loss function and the optimizer, and then the practical
aspects of the training, namely deciding the batch size for data samples and epochs to
train the network. However, we also believe that it would be relevant to cover other DL

11

architectures like RNN, variational AE, CNN etc., and in this direction the work is in
progress.

References

[1] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature,

521(7553):436, 2015.

[2] Mohit Sewak, Sanjay K Sahay, and Hemant Rathore. Comparison of deep learn-
ing and the classical machine learning algorithm for the malware detection. In
2018 19th IEEE/ACIS International Conference on Software Engineering, Artiﬁ-
cial Intelligence, Networking and Parallel/Distributed Computing (SNPD), pages
293–296. IEEE, 2018.

[3] Mohit Sewak, Sanjay K Sahay, and Hemant Rathore. An investigation of a deep
In Proceedings of the 13th Interna-
learning based malware detection system.
tional Conference on Availability, Reliability and Security, page 26. ACM, 2018.

[4] Alex Graves, Santiago Fern´andez, Faustino Gomez, and J¨urgen Schmidhuber.
Connectionist temporal classiﬁcation: Labelling unsegmented sequence data with
recurrent neural networks. In Proceedings of the 23rd International Conference
on Machine Learning, ICML ’06, pages 369–376, New York, NY, USA, 2006.
ACM.

[5] Sepp Hochreiter and J¨urgen Schmidhuber. Long short-term memory. Neural

computation, 9(8):1735–1780, 1997.

[6] Kyunghyun Cho, Bart Van Merri¨enboer, Caglar Gulcehre, Dzmitry Bahdanau,
Fethi Bougares, Holger Schwenk, and Yoshua Bengio. Learning phrase repre-
sentations using rnn encoder-decoder for statistical machine translation. arXiv
preprint arXiv:1406.1078, 2014.

[7] Manuel P Cu´ellar, Miguel Delgado, and MC Pegalajar. An application of non-
linear programming to train recurrent neural networks in time series prediction
problems. In Enterprise Information Systems VII, pages 95–102. Springer, 2007.

[8] Mohit Sewak, Md Rezaul Karim, and Pradeep Pujari. Practical Convolutional
Neural Networks: Implement advanced deep learning models using Python. Packt
Publishing Ltd, 2018.

[9] Mohammed Amine Janati Idrissi, Hassan Ramchoun, Youssef Ghanou, and Mo-
hamed Ettaouil. Genetic algorithm for neural network architecture optimization.
In Logistics Operations Management (GOL), 2016 3rd International Conference
on, pages 1–4. IEEE, 2016.

[10] D Stathakis. How many hidden layers and nodes?

International Journal of

Remote Sensing, 30(8):2133–2147, 2009.

12

[11] Jeff Heaton. Introduction to neural networks with Java. Heaton Research, Inc.,

2008.

[12] Christopher M. Bishop. Pattern Recognition and Machine Learning (Information

Science and Statistics). Springer-Verlag, Berlin, Heidelberg, 2006.

[13] Kevin L. Priddy and Paul E. Keller. Artiﬁcial Neural Networks: An Introduction
(SPIE Tutorial Texts in Optical Engineering, Vol. TT68). SPIE- International
Society for Optical Engineering, 2005.

[14] D. F. Specht. A general regression neural network. Trans. Neur. Netw., 2(6):568–

576, November 1991.

[15] Vinod Nair and Geoffrey E Hinton. Rectiﬁed linear units improve restricted boltz-
mann machines. In Proceedings of the 27th international conference on machine
learning (ICML-10), pages 807–814, 2010.

[16] Djork-Arn´e Clevert, Thomas Unterthiner, and Sepp Hochreiter. Fast and accu-
rate deep network learning by exponential linear units (elus). arXiv preprint
arXiv:1511.07289, 2015.

[17] Xavier Glorot, Antoine Bordes, and Yoshua Bengio. Deep sparse rectiﬁer neural
networks. In Proceedings of the fourteenth international conference on artiﬁcial
intelligence and statistics, pages 315–323, 2011.

[18] Andrew L Maas, Awni Y Hannun, and Andrew Y Ng. Rectiﬁer nonlinearities
improve neural network acoustic models. In Proc. icml, volume 30, page 3, 2013.

[19] Bing Xu, Naiyan Wang, Tianqi Chen, and Mu Li. Empirical evaluation of rectiﬁed
activations in convolutional network. arXiv preprint arXiv:1505.00853, 2015.

[20] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Delving deep into rec-
tiﬁers: Surpassing human-level performance on imagenet classiﬁcation. In Pro-
ceedings of the IEEE international conference on computer vision, pages 1026–
1034, 2015.

[21] Sergey Ioffe and Christian Szegedy.

deep network training by reducing internal covariate shift.
arXiv:1502.03167, 2015.

Batch normalization: Accelerating
arXiv preprint

[22] Katarzyna Janocha and Wojciech Marian Czarnecki. On loss functions for deep
neural networks in classiﬁcation. arXiv preprint arXiv:1702.05659, 2017.

[23] Yichuan Tang. Deep learning using linear support vector machines.

arXiv

preprint arXiv:1306.0239, 2013.

[24] Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou Zhang, and Zhuowen
Tu. Deeply-supervised nets. In Artiﬁcial Intelligence and Statistics, pages 562–
570, 2015.

13

[25] Katarzyna Janocha and Wojciech Marian Czarnecki. On loss functions for deep
neural networks in classiﬁcation. arXiv preprint arXiv:1702.05659, 2017.

[26] Yurii Nesterov. A method for unconstrained convex minimization problem with
In Doklady AN USSR, volume 269, pages

the rate of convergence o (1/kˆ 2).
543–547, 1983.

[27] John Duchi, Elad Hazan, and Yoram Singer. Adaptive subgradient methods for
online learning and stochastic optimization. Journal of Machine Learning Re-
search, 12(Jul):2121–2159, 2011.

[28] Jeffrey Pennington, Richard Socher, and Christopher Manning. Glove: Global
vectors for word representation. In Proceedings of the 2014 conference on empir-
ical methods in natural language processing (EMNLP), pages 1532–1543, 2014.

[29] Jeffrey Dean, Greg Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Mark Mao,
Andrew Senior, Paul Tucker, Ke Yang, Quoc V Le, et al. Large scale distributed
In Advances in neural information processing systems, pages
deep networks.
1223–1231, 2012.

[30] Matthew D Zeiler. Adadelta: an adaptive learning rate method. arXiv preprint

arXiv:1212.5701, 2012.

[31] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization.

arXiv preprint arXiv:1412.6980, 2014.

[32] Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyan-
skiy, and Ping Tak Peter Tang. On large-batch training for deep learning: Gener-
alization gap and sharp minima. arXiv preprint arXiv:1609.04836, 2016.

[33] Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan
Salakhutdinov. Dropout: A simple way to prevent neural networks from overﬁt-
ting. Journal of Machine Learning Research, 15:1929–1958, 2014.

[34] G. E. Hinton and R. R. Salakhutdinov. Reducing the dimensionality of data with

neural networks. Science, 313(5786):504–507, 2006.

[35] David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning internal
representations by error propagation. Technical report, California Univ San Diego
La Jolla Inst for Cognitive Science, 1985.

14
