# SurVis-XAI-Health: A Literature Visualization on Explainable AI in Digital Health

This repository hosts an interactive SurVis-based visual interface for exploring key research papers on **Explainable Artificial Intelligence (XAI)** in the domain of **Digital Health**. It presents a curated collection of 10 high-quality publications from 2022 to 2025, encompassing diverse application areas such as clinical decision support, mental health, electronic health records, and teleconsultation.

## 🔍 Focus of This Collection

- **Main Theme**: Explainable & Responsible AI in Digital Health
- **Topics Covered**:
  - Explainability methods (Grad-CAM, SHAP, LIME, etc.)
  - Survey & systematic reviews on XAI frameworks
  - XAI for EHRs, mental health, remote diagnosis, and brain tumor detection
  - Ethical concerns such as fairness, trust, and privacy
- **Publication Types**: Survey, Review, Applied Research, Experimental Studies

## 🗂 Repository Structure

```bash
.
├── index.html              # Main SurVis interface
├── about.html              # Project summary and documentation
├── js/                     # Core SurVis JS logic
├── styles/                 # Visual and layout stylesheets
├── src/data/generated/
│   ├── bib.js              # BibTeX-style entries for the 10 papers
│   ├── available_img.js    # Available thumbnails for each paper
│   ├── available_pdf.js    # PDF identifiers (if available)
│   └── draw.py             # Python helper (if used for keyword analysis)
├── src/papers_img/         # Thumbnail PNGs of each paper
└── src/papers_pdf/         # (Optional) PDF files of papers
```

## 📈 Visual Features (Powered by SurVis)

- Timeline view of publication years
- Keyword cloud with selector filtering
- Author list and clustering by keyword similarity
- BibTeX export and citation display
- Color-coded categories for thematic grouping

## 🌐 Online Deployment (GitHub Pages)

To publish your visual interface live:

1. Push this repository to GitHub (e.g., `https://github.com/Hao-Zhang123/survis-xai-health`)
2. Go to **Settings > Pages**
3. Under “Source”, choose `main` branch and `/root`
4. Your SurVis visual dashboard will be hosted at:

```
https://hao-zhang123.github.io/survis-xai-health/
```

## 📚 Paper Sources

All 10 publications are sourced from leading journals and conferences including:
- IEEE JBHI
- ACM TOCH
- Nature Communications Medicine
- Springer Artificial Intelligence Review
- MDPI Sensors & Applied Sciences
- SAGE Digital Health
- arXiv (preprints)

## ✅ Coursework Context

This project was developed as part of the **COMP4037 Research Methods** coursework at the University of Nottingham, with a focus on **Responsible AI in Digital Health**. It demonstrates not only literature review capabilities, but also interactive data visualization and technical reproducibility.

---

**Author**: Hao Zhang  
**Course**: COMP4037 – Research Methods  

```
© 2025 Hao Zhang – All rights reserved.
```
