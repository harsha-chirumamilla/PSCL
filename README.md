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

## Features

- Multi-label classification for protein subcellular localization
- Utilizes Gene Ontology term relationships
- Supports both strict and relaxed accuracy metrics
- Feature generation using node2vec for graph embeddings
- Deep neural network models for prediction

## Cellular Locations Predicted

The system predicts protein locations among the following cellular components:
- Membrane
- Cytoplasm
- Nucleus
- Extracellular
- Cell membrane
- Mitochondrion
- Plastid
- Endoplasmic reticulum
- Lysosome/Vacuole
- Golgi apparatus
- Peroxisome

## Technical Details
### Evaluation Metrics
- Strict accuracy (exact match)
- Relaxed accuracy
- Per-location accuracy
- Matthews Correlation Coefficient

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
- Strict Accuracy: ~44.69% (Actual GO)
- Relaxed Accuracy: ~91.2% (Actual GO)

## Usage
1. Process GO term relationships to create adjacency matrices
2. Generate feature vectors using node2vec
3. Train the model using the provided notebooks
4. Evaluate performance using dynamic thresholding approach with the threshold defined as α × max(probabilities), where α ∈ (0,1)

Note: Detailed instructions for each step are provided in the respective notebooks.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributors

- Harsha Vardhan Chirumamilla
- Tejus Paturu
- Naga Raju Reddy Maruprolu