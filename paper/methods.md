This controlled observational research design utilized a plethora of Python modules: NLTK, numpy, TFLearn,
Tensor Flow, random, JSON, and pickle. Controlled observational research was the most optimal approach for the
research objectives as it allowed for higher variable control, such as parameters, patterns, and byte size, and
observes the output runtime in order to determine the relationship between the byte size and the runtime.
In the Natural Language Toolkit library, the program to test the runtimes utilized the Lancaster Stemmer, which
reduces words to their root form. Creating and utilizing an instance of the Lancaster Stemmer is vital for the natural
language processing model, which simplifies text classifications and information retrieval. It allows the machine
learning algorithms to run without “worrying” about the core meaning of words. Utilizing training data from a
version that removes the dimensionality of the user input makes the program more efficient by treating similar
words as identical, thus removing the generalization and developing the efficiency of the models.
Numpy holds a plethora of important mathematical operations that were crucial in the design of this program. Array
creation for training data and output labels was completely taken care of by numpy. Numpy was also employed in
the manipulation of these arrays, transforming the output data and providing efficient computation and matrix
operation. The study integrated numpy, mainly its diverse set of arrays, with Tensor Flow to serve as input data for
training the machine learning models.
TFLearn is a deep learning library that is built on top of Tensor Flow that provides abstractions and utilities to both
build and train neural networks. Tensor Flow, the crux of this research, on top of being a popular deep learning
framework, has provided the design for this program with the ability for neural network implementation. The
Lancaster Stemmer has four steps: initialization, suffix removal, stemming rules, and termination condition. It
reduces words to their base form [5]. It defined the structure of the neural network model and trained it with data
from the arrays, allowing for efficient computation. Since it utilizes both the CPU and GPU, Tensor Flow algorithms
accelerate training processing by utilizing concepts such as parallel processing and optimization techniques to
handle large-scale data potentially. In short, Tensor Flow allows the program to use incredibly large file lengths with
the intents.json input for testing without causing additional errors.
Python’s random module was a small but significant factor in this experiment, as it added a way for the chatbot to
provide varied responses during its interactions, which is crucial for testing different responses. The JSON library
was utilized for reading data from the intents.json file, which contained structured data defining intents, patterns,
and responses for the chatbot. This allowed the program to extract and utilize the necessary information for training
and using the chatbot.
Pickle sped up the process of training data. First, it allowed for object serialization - forcing Python objects into
files. It provided me with the opportunity to load data from files in a binary format. It would read and write data in
an efficient manner by reprocessing code over and over for each implementation.
By opening the intents.json file, which contains the intents and patterns for the chatbot, it loads the content into a
variable. If there is no preprocessed data available, the model reprocesses the data from the intents file and serializes
it into a pickle file. Next, process the data from the file by extracting the words, labels, training and output data, and
patterns provided.
We then load the processed data into numpy arrays and integrate it with Tensor Flow through the binaries in the
pickle file. To reset the runtime, the program would reset Tensor Flow’s default graph, which clears any previously
defined operations and allows for complete retraining of the data. The program also defines the neural network
architecture using TFLearn with a softmax function and a DNN model. The model utilized one-thousand epochs
(amount of iterations) and a batch size of eight [6]. The epochs determined the runtime, and 1000 is a common
baseline for epochs in machine learning literature [6]. The batch size refers to the number of data points processed
through a neural network during training. The dataset is divided into a smaller subset of batches, and the batch size
determines the size of the subsets. Eight is relatively small, which helps with memory and computational efficiency.
The model was trained based on the data and saved in a TFLearn index, Meta, and data. Finally, the program
converted the user input into a bag-of-words representation of the code in the form of a numerical vector from a
predefined vocabulary [7]. The program tokenizes the sentence and stems the words in the sentence, comparing
them to the predefined vocabulary and checking for the presence of specific words to be fed into the chatbot model
to predict a suitable response based on learned patterns.
The study design was built around the described program. Other than the downloaded Python modules, materials
utilized included the lightweight data interchange format with a pre-made corpus of intents and patterns in the
Python software’s ecosystem. Furthermore, in the environmental setup, the experiments were run on Python 3.10.5
on an Alien ware Aurora R7 with an Intel(R) Core(TM) i7-8700 CPU @ 3.20 GHz (3.19 GHz usable), 16GB
(15.8GB usable) RAM with Windows 10 Home, and a GTX 1080 Ti (11121 MB VRAM). The Python code was run
in Sublime Text.
For measurement, the study tested three different byte sizes in three different trials, finding the runtime of how long
it took to create and initialize the newly processed data into the chatbot model. The IDE Sublime Text has an inbuilt
function that outputs the runtime of a program, which is what the study utilized to measure timing.
I utilized a linear regression model that examines the relationship between a set of independent and dependent
variables that is represented in the form y=bx+c where y is the dependent variable, b is the slope, c is the constant,
and x is the independent variable. The model examines the ability of the independent variables to predict the set of
dependent variables - providing a good indication of which variables are significant in relation to impacting the
other. This was important as it was possible that the entirety of this paper was built on a false pretense that the JSON
length had nothing to do with the runtime, meaning that utilizing this model would tell me both the falsehood of this
claim and if the claim was true, it would quantify it. Using a linear regression model helps identify if JSON length
has an impact on run time. If so, it helps quantify the impact.
To create this linear regression model, the experiments were run on three different data sets of varying sizes: small,
regular, and large. The small dataset was created as there are a lot of limitations to runnable byte-size maxes in the
real world, and it would deal more with utilizing chatbots for more niche purposes. The “regular” data set included
an average amount of data and was used to deal more with the application interface as it provided a byte size that
was consistent with highly-specific application chatbots. The larger byte size included an abnormally large amount
of data and was tested to check if the runtime complexity was parabolic or linear and if the linearity of the byte size
had an effect on runtime performance.
