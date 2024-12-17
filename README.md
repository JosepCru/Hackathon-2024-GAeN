# 🧬 **Automated Nanoparticle Detection in Microscope Images**

## **Overview**  
This project automates the detection and localization of nanoparticles in microscope images, a traditionally manual and time-consuming task. Using **machine learning** models and an intuitive **user interface**, researchers can efficiently analyze samples, saving significant time and effort.

The system includes:  
1. **User-Friendly Interface**: Displays the microscope's current view, detects nanoparticles, and provides real-time results.  
2. **Machine Learning Models**: Predicts the probability of nanoparticles, counts them, and identifies their centers.  
3. **Automated Navigation**: Systematically scans the sample, optimizing microscope movement to locate nanoparticles efficiently.

---

## **Features**  
- **Real-Time Detection**: Identifies nanoparticles, their quantity, and their coordinates from 256x256 microscope image sections.  
- **Large Image Analysis**: Processes large 12kx16k images by dividing them into smaller grids.  
- **Spiral Scanning**: Automatically navigates through the sample, skipping areas without nanoparticles for maximum efficiency.  
- **Visualization**: Tracks microscope movements and displays results in an intuitive interface.  
- **Synthetic Data Generation**: Creates labeled datasets to train and validate machine learning models.

---

## **Getting Started**  

### Prerequisites  
Before running the code, ensure you have the following installed:  
- Python 3.8 or higher  
- Required Python libraries:  
  ```bash
  pip install numpy pandas tensorflow keras matplotlib opencv-python
  ```  
- A working microscope setup (if applicable) or access to images for testing.  

### Project Setup  
1. Clone this repository to your local machine:  
   ```bash
   git clone https://github.com/yourusername/nanoparticle-detector.git
   cd nanoparticle-detector
   ```  

2. Prepare your datasets:  
   - Place the microscope images and corresponding label maps into the `data/` directory.  
   - Use the synthetic data generation script (`data_generator.py`) to create augmented datasets if needed.

3. Train the machine learning models:  
   - Modify the paths and hyperparameters in the `train_model.py` script.  
   - Run the training process:  
     ```bash
     python train_model.py
     ```  
   - Models will be saved to the `models/` directory.

4. Run the interface with the automated navigator:  
   ```bash
   python main_interface.py
   ```  

---

## **Directory Structure**  
```
nanoparticle-detector/
│
├── data/                   # Input images and labels
│   ├── raw/                # Original microscope images
│   ├── processed/          # Synthetic or preprocessed images
│
├── models/                 # Saved machine learning models
│   ├── spectra_model.h5    # Model for Spectra microscope
│   └── tecnai_model.h5     # Model for Tecnai microscope
│
├── scripts/  
│   ├── data_generator.py   # Script to generate synthetic data
│   ├── train_model.py      # Model training script
│   └── navigator.py        # Automated scanning algorithm
│
├── main_interface.py       # Main user interface with navigator
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── LICENSE                 # License information
```

---

## **How It Works**  
1. **Data Preparation**:  
   - Real and synthetic microscope images are collected and labeled.  
   - Images are split into 256x256 regions for model training.  

2. **Model Training**:  
   - Two machine learning models (Tecnai and Spectra) are trained to:  
     - Predict nanoparticle probability.  
     - Return the number of nanoparticles and their center coordinates.

3. **Automated Navigation**:  
   - The microscope window scans a 12kx16k image grid-by-grid.  
   - Spiral movement optimizes search efficiency, skipping empty grids.  
   - When nanoparticles are detected, the navigator focuses on high-probability regions.

4. **User Interface**:  
   - Displays the microscope's current view.  
   - Shows nanoparticle counts, coordinates, and navigation paths in real time.

---

## **Results**  
The system:  
- **Accelerates analysis** by automating nanoparticle detection.  
- **Optimizes microscope usage** with a focused navigation approach.  
- **Provides accurate predictions** with well-trained machine learning models.  

---

## **Contributing**  
Contributions are welcome! Please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes and open a pull request.

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**  
This project was developed with the support of advanced electron microscopy groups and researchers. Special thanks to our collaborators and advisors for their invaluable input.  

---

## **Contact**  
For questions or collaborations, please contact:  
📧 **your.email@example.com**  
