<div align="center">

# DeepWheat

A web app for wheat farmers. They upload a photo of a wheat leaf and get back the likely disease, how fast it could spread across their field, what it may cost them, and a written report on its cause, treatment and management.

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-BART-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)

[Objectives](#objectives) · [Features](#features) · [Architecture](#architecture) · [Models](#models) · [Team](#team)

<sub>Challenge 3 · Master's in Artificial Intelligence Engineering · <a href="https://www.isep.ipp.pt">ISEP</a>, Porto · 2024–25</sub>

</div>


## Objectives

The main objective of the project was to use computer vision and natural language processing to help farmers deal with crop diseases. These were the goals:

- [x] Explore several crop image datasets (banana and mango ripeness, coffee and tomato leaves) before settling on wheat
- [x] Train image models that recognise four wheat diseases, or a healthy leaf, from a photo
- [x] Estimate how a disease spreads over the days that follow and what that means in lost yield and money
- [x] Build an agricultural text corpus and train language models that write the cause, treatment and management of each disease
- [x] Put it all behind an API and a web app, working in Scrum sprints




## Features

| | Feature | What it does |
|:-:| --- | --- |
| 👤 | **Account and field** | Sign up, log in, and save your field's area, planting cost, expected yield and expected profit |
| 📷 | **Disease from a photo** | Upload a photo of a leaf and get one of five results: brown rust, yellow rust, septoria, mildew or healthy |
| 📈 | **Spread and losses** | See after how many days 20% and 80% of the field could be infected, with the yield lost in tons and the profit and planting costs lost in euros |
| 📝 | **Written report** | Read the cause, treatment and management of the disease, and download the whole report as a PDF |

## Architecture

```
React web app  →  FastAPI  →  image model (CNN + ViT)
                           →  spread and loss formulas
                           →  report model (BART)
                           →  PostgreSQL (users and fields)
```

The web app is React and TypeScript with PrimeReact and Tailwind, and it creates the PDF in the browser. The API handles sign-up and login with hashed passwords and JWT tokens, saves each user's field in PostgreSQL (run with Docker), and builds the report in one call: classify the photo, model the spread for that disease, work out the losses and generate the text. Each step is its own service, so a model can be swapped without touching the others.

## Models

**Images.** The wheat dataset was prepared at 64 and 128 pixels to keep training fast. We compared our own CNNs with a CNN combined with a Vision Transformer, and with pre-trained networks (VGG16, MobileNet, InceptionV3 and Xception). The app uses the CNN + Vision Transformer, which reached about 97% accuracy on images it had never seen. In the earlier banana and mango study, removing the background made the models worse, a sign they were also using what was around the fruit.

**Spread.** Each disease grows at its own pace, so each has its own curve: a Gompertz curve for brown rust and septoria, a logistic curve for yellow rust, and a fitted growth curve for mildew. From the field's size, the API works out the day each infection level is reached, and the losses follow from the share of the field infected.

**Text.** We built a corpus from scraped agricultural pages and PDFs, cleaned and filtered it, trained word2vec embeddings on it, and generated a synthetic question dataset. We then fine-tuned BART and Phi-2 to answer questions such as "septoria treatment". The app uses the fine-tuned BART model.

## Project structure

```
application/
├── api/                 FastAPI app: controllers, services, database access and the trained models
├── frontend/            React + TypeScript web app
├── docker/              PostgreSQL with Docker Compose
└── postman_collection/  requests for trying the API
notebooks/               image exploration and model training
report_system/           first version of the report generator
```

> The fine-tuned BART model (about 5 GB with its checkpoints) was stored with Git LFS and isn't included in this copy, so the report text needs the model added back to `application/api/ai_models/` to run.

> The main branch holds the finished app. Each model and experiment also has its own branch, named after its Scrum task (for example `SCRUM-14-Train-CNNs-for-Computer-Vision` or `phi2-text-generation`).

## Team

<table align="center">
  <tr>
    <td align="center" width="150">
      <a href="https://github.com/Marco-Nobrega-Andrade"><img src="https://github.com/Marco-Nobrega-Andrade.png?size=200" width="100" alt="Marco Andrade"/></a><br>
      <b>Marco Andrade</b><br>
      <a href="https://github.com/Marco-Nobrega-Andrade">@Marco-Nobrega-Andrade</a>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/SrMasterAD"><img src="https://github.com/SrMasterAD.png?size=200" width="100" alt="David Dias"/></a><br>
      <b>David Dias</b><br>
      <a href="https://github.com/SrMasterAD">@SrMasterAD</a>
    </td>
        <td align="center" width="150">
      <a href="https://github.com/nelsonnovais"><img src="https://github.com/nelsonnovais.png?size=200" width="100" alt="Nelson Novais"/></a><br>
      <b>Nelson Novais</b><br>
      <a href="https://github.com/nelsonnovais">@nelsonnovais</a>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/ricardoham"><img src="https://github.com/ricardoham.png?size=200" width="100" alt="Ricardo Manoel"/></a><br>
      <b>Ricardo Manoel</b><br>
      <a href="https://github.com/ricardoham">@ricardoham</a>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/alefjmelo"><img src="https://github.com/alefjmelo.png?size=200" width="100" alt="Alef Melo"/></a><br>
      <b>Alef Melo</b><br>
      <a href="https://github.com/alefjmelo">@alefjmelo</a>
    </td>
  </tr>
</table>
