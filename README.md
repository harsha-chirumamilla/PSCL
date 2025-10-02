# Protein Localization Prediction Using Gene Ontology

This project focuses on predicting protein subcellular localization using Gene Ontology (GO) terms and machine learning techniques. The system employs deep learning models to predict multiple possible cellular locations for proteins based on their GO term annotations.

## Project Structure

```
├── Adj_Matrices/          # Contains adjacency matrices in parquet format
├── Datasets/              # Training and testing datasets
├── Models/                # Saved trained models
├── Notebooks/            
│   ├── Act_GO.ipynb      # Actual GO term analysis notebook
│   ├── Act.ipynb         # Actual predictions notebook
│   ├── Ind_analysis.ipynb # Independent analysis notebook
│   ├── Ind.ipynb         # Independent predictions notebook
│   ├── ClassLabels.py    # Label generation utilities
│   └── multiLabelMetrics.py # Evaluation metrics
├── Relations/            # GO term relationship files
└── Utils/
    ├── adj_matrix.py     # Adjacency matrix generation
    └── Feat_generator.py # Feature vector generation
```
## Datasets

The datasets used to train and test the models are located in the `Datasets` folder. All the files in this folder are also available on Kaggle, except for the dataset `Actual_Train_GO.parquet`, which is only available on Kaggle. You can access `Actual_Train_GO.parquet` and other related datasets here: [gene-ontology](https://www.kaggle.com/datasets/harshac1306/gene-ontology).

## Features

- Multi-label classification for protein subcellular localization
- Utilizes Gene Ontology term relationships
- Supports both strict and relaxed accuracy metrics
- Feature generation using node2vec for graph embeddings
- Deep neural network models for prediction

## Technical Details
### Evaluation Metrics
- Strict accuracy (exact match)
- Relaxed accuracy
- Per-location accuracy
  
## Dependencies

- TensorFlow/Keras
- Pandas
- NumPy
- node2vec
- NetworkX
- scikit-learn
- PyArrow
- Matplotlib

## Model Performance

The models achieve the following performance metrics:
- Strict Accuracy: ~44.69% (Actual dataset)
- Relaxed Accuracy: ~91.2% (Actual Dataset)

## Usage
1. Process GO term relationships to create adjacency matrices
2. Generate feature vectors using node2vec
3. Train the model using the provided notebooks
4. Evaluate performance using dynamic thresholding approach with the threshold defined as α × max(probabilities), where α ∈ (0,1)

Note: Detailed instructions for each step are provided in the respective notebooks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- Harsha Vardhan Chirumamilla
- Tejus Paturu
- Naga Raju Reddy Maruprolu
