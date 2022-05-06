# Get-Cooking-

Cooking Recommendations

### Overview
Cooking is both a passion and a big concern for some people. Cooking, on the other hand, can always use a helping hand. Being a student, deciding what to eat for lunch or dinner is always a challenge. When you only have a few ingredients in the kitchen, deciding what to make for dinner might be difficult. This prompted us to develop a system that can suggest recipes based on suggested ingredients. Recipe provider that uses web-scraped recipe data to provide users with the recipes based on their preferences and the ingredients they have.

### Goals
1. Create a search algorithm that utilizes similarity scoring to rank recipes according to the greatest similarity to the search query.
2. To provide recipes when the user has limited items in the kitchen, or cannot decide what to cook for his/meal.
3. Recommend recipes based on the dish name
4. Recommend recipes based on the ingredients the user has with him/her.

### Dataset and Pre-processing
Scraped data from : https://www.jamieoliver.com/
Content extracted:
   - Recipe_urls
   - Recipe name
   - Ingredients
   - Serves
   - Cooking_time
   - Difficulty
Pre-processed dataset:
   - Recipe_urls
   - Recipe
   - Ingredients
   - Ingredients_parsed (stopwords, measure, unnecessary words like fresh, etc. removed)


### Modules
- Data Extraction and Pre-Processing
- API for Fetching Recipes - FastAPI
- Streamlit UI
- User Authentication and User Authorization - JWT
- Airflow workflows 
- RecipeCache - For storing cache if the user has no ingredients and wants recipes to be suggested
- SendingEmails - when the user registers for subscriptions
- Data Validation and Unit testing
- Deployment on Cloud (GCP)
- Hosting Streamlit
- Visualizations
- Github Issues 

### Folder Structure
Github Folder Structure
- Streamlit UI
 -- Functionality:
If the user provides ingredients, search through the dataset and recommend recipes based on the ingredients that match. 
If the user has no ingredients, provide recipes from cache
Includes:
User authentication and authorization using JWT
App design elements
Import data validations using regex
Storing the registered users’ info and uploading it into GCP storage buckets
Files:
Streamlit.py - has the design of the UI with error handling
FoodSearch.py - takes the ingredients and gives dataframe as output based on the user input


