🌱🔍 **Plant Disease Detection Readme** 👨‍🔬🌿

📁 **Dataset**:
The "Plant Disease Detection" project utilizes the "Plant Village" dataset. You can find the dataset at the following link: 
[Plant Village Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village) 🌿

🌿 **About the Project**:
The objective of this project is to develop a model that can detect diseases in plants. It has achieved an impressive accuracy rate of 89%. The model can identify various potato leaf diseases such as early blight and late blight, as well as healthy leaves. Furthermore, it can also detect tomato plant diseases including early blight, leaf mold, target spot, and curl virus. 🌱🍅🥔

💻 **Installation and Setup**:
1. Clone the repository:
2. Install the required dependencies:
3.  Download the "Plant Village" dataset from the provided link and place it in the project directory.
4. Run the project:
5. 

**TO RUN THE PROJECT**
1. Go to the `api` folder:
2. Install the requirements for the API:  `pip install -r requirements.txt`
3. 3.Run the project:
`python main.py`


🌱 **Usage**:
1. Use Postman or Swagger UI to access the API endpoint.

2. Make a POST request to `http://localhost:8000/predict` with the following parameters:
   - `image`: Upload an image of the plant for disease detection.

🔧 **Example using Postman**:
- Open Postman.
- Select "POST" request method.
- Set the request URL to `http://localhost:8000/pridict`.
- Under the "Body" tab, select "form-data".
- Add a key-value pair:
  - Key: `image`
  - Value: Select an image file from your local system.
- Click "Send" to get the disease detection results.
![Screenshot 2023-06-27 224141](https://github.com/pratt4/Plant-disease-detection/assets/90851204/57384b7c-5a71-4b7d-bd9b-5e2139fafc84)

  
