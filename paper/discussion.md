The study sought to investigate and quantify the affinity between the byte size of the intents.json file and the
machine learning compilation runtime. This examination gauged the compilation runtime of three different data sets
of deviating sizes to determine whether the byte size particularly influenced the runtime period.
The results of the analysis indicate that while the data does not fit a strictly linear behavior, assuming a linear
relationship between the byte size and the runtime due to the program's O (N) runtime complexity is allowed.
O (N) implies that the runtime of the algorithm grows approximately linearly with the size of the input, and in this
case, the data processing steps, stemming of words and bag-of-words representation contribute to this complexity.
The analysis further indicates a possibility of an error in the runtime check in Sublime text, as the slope-intercept

line equation from two points - that being (9.75,7547) and (32.59,28496) is y=917.2066549912433x-
1395.76488616.

This is nearly identical to the least squares regression line, which means that there is a possibility that it is entirely
linear, and there was some regulation error. Either way, the research found the data to be non-linear, so external
factors must be considered.
Note that the non-linearity observed in the data could be attributed to heterogeneous data. While O (N) provides an
upper-bound estimate for runtime complexity, external factors such as nested loops or recursive calls in the code
may introduce variations and impact the actual runtime [9].
One limitation of this study is the relatively small sample size of both the computers used and the intents.json file
sizes. Generalizing these findings would benefit from larger and more diverse samples in future studies.
Additionally, exploring the effects of CPU and GPU overclocking, upgrading, or downgrading on timing could
provide valuable insights into the performance of the chatbot model.
It is entirely possible that the amount of time it takes to train each model in the Tensor Flow DNN function is
dependent on the specifications of the clone's computer. Replicating this research would require the user to utilize
the same computer specifications used in this study, and further research could be taken to find whether or not the
claim of the runtime being dependent on specifications is true. Furthermore, this study relied on deterministic
algorithms and a bag-of-words representation for data processing. However, contextual data and quality issues in
natural language processing were not thoroughly studied, which may introduce additional complexities and
variations in the runtime performance.
Despite these limitations, the present study serves as a baseline for understanding the runtime complexity of the
chatbot model in the context of artificial intelligence and machine learning algorithms. It contributes to the existing
body of knowledge and highlights the importance of considering algorithm runtime in the development and
optimization of natural language processing systems.
In conclusion, the findings of this study suggest a linear relationship between the byte size of the intents.json file and
the runtime of the chatbot model, as indicated by the O (N) runtime complexity. However, the non-linearity
observed in the data underscores the influence of heterogeneous data and external factors on the actual runtime
performance. Future research should aim to address the limitations of this study by incorporating larger sample byte
sizes, exploring hardware-related factors, and considering the impact of contextual data on the performance of
chatbot models. By expanding on these different research directions, people can further enhance the understanding
and optimization of chatbot models in real-world applications [10].
