# 📄 Runtime Complexity of Chatbot Algorithms Based on `intents.json` File Size

> An empirical investigation of how chatbot training time scales with data input size using NLTK and TensorFlow.

---

## 📚 Abstract

This research explores the correlation between the length of an `intents.json` file and the runtime of chatbot algorithms built with **NLTK** and **TensorFlow**. By analyzing runtime performance across various file sizes, we uncover a compelling **linear relationship** using a **least squares regression model**, indicating an **O(N)** complexity. These insights provide practical baselines for developers optimizing chatbot training pipelines.

---

## 📂 Repository Structure

```
📦chatbot-runtime-analysis/
├── paper.pdf                 # Full research paper (published)
├── intents_samples/         # Sample intents.json files of varying sizes
├── run_analysis.py          # Script to measure runtime for each file size
├── regression_model.ipynb   # Jupyter notebook with regression analysis
├── plots/                   # Graphs and visualizations
└── README.md                # This file
```

---

## 🔍 Introduction

With over **1.4 billion chatbot users** globally, the efficiency of natural language processing systems is more critical than ever. This study investigates how the **size of the intents.json file**, a core input to most chatbot architectures, impacts the **runtime performance** of Python-based NLP frameworks.

We analyze how training time scales with file size and explore practical implications for developers building scalable chatbot systems.

---

## 🧪 Methods

- Programming Language: **Python 3.10.5**
- Key Libraries: `nltk`, `numpy`, `tensorflow`, `tflearn`, `json`, `pickle`, `random`
- NLP Model: **Lancaster Stemmer** + **Bag-of-Words Representation**
- Training Model: **TFLearn DNN** with 1000 epochs, batch size = 8
- Measurements: File byte size vs runtime (captured via Sublime Text IDE)

We tested 3 datasets (small, regular, large) over multiple trials and applied **linear regression** to model the relationship between size and runtime.

---

## 📊 Results

| Byte Size      | Runtime (s) - All Trials Consistent |
|----------------|-------------------------------------|
| 7,547 bytes    | 9.75 seconds                        |
| 13,248 bytes   | 15.77 seconds                       |
| 28,496 bytes   | 32.59 seconds                       |

**Least Squares Regression Line:**
```
ŷ = 914.90x - 1291.32
```

This supports the hypothesis of **O(N)** runtime complexity, with runtime scaling linearly with input size. Deterministic algorithms and fixed architecture helped maintain consistent runtimes.

---

## 📈 Visualizations

All plots are available in the `plots/` directory. The regression line fit confirms the linearity of the runtime behavior with minimal deviation.

---

## 💬 Discussion

- The results suggest an **O(N)** relationship between intents.json file size and chatbot runtime.
- Slight non-linearity may stem from hardware constraints, system noise, or heterogeneous data.
- Limitations include sample size and computational variation.
- Future work could explore contextual data impact, system hardware variations, and additional file sizes.

---

## ✅ Conclusion

This study provides a **baseline for understanding and predicting the runtime** of chatbot models trained using intents.json files. It contributes to AI runtime efficiency literature and can aid teams in resource planning and infrastructure scaling for chatbot applications.

---

## 👨‍💻 Author

**Rishi Hariharaprasad**  
12th Grade Programmer, Brandeis High School  
Rise Finalist · Congressional App Winner · International Hackathon Finalist  

> "I wrote this paper to better understand the ML algorithms used in my app and how to read data more efficiently."

---

## 📝 Citation

```
@article{hariharaprasad2023chatbot,
  title={Runtime Complexity of Chatbot Algorithms Based on intents.json File Size},
  author={Hariharaprasad, Rishi},
  journal={International Journal of Computer Science and Mobile Applications},
  volume={11},
  number={6},
  year={2023},
  pages={1--8},
  issn={2321-8363}
}
```

---

## 📄 License

This work is published under the **Creative Commons Attribution 4.0 International License**.

---

## 📚 References

1. Jovic, D. (2020). *The future is now – Chatbot statistics.*
2. Janakiram, M. (2020). *TensorFlow Turns 5.* Forbes.
3. Kakarla, S. (2021). *NLTK vs. Spacy.*
4. NLP Guide. (2021).
5. Paice, C. D. (1990). *Another stemmer.* ACM SIGIR Forum.
6. Brownlee, J. (2018). *Batch vs Epochs.* Machine Learning Mastery.
7. Brownlee, J. (2019). *Bag of Words Introduction.*
8. GeeksForGeeks. (2023). *Deterministic vs Non-Deterministic Algorithms.*
9. Olawanlet, J. (2023). *Big O Cheat Sheet.*
10. Parietal Lab. *Learning from Heterogeneous Data.*

