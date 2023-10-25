#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class DiamondsAnalysis:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        

    def task_one(self):
        """
         Question 1.
        
        Explanation: This method filters the dataframe to only include rows where the carat value 
        is strictly greater than 0.30 and strictly less than 1.08. The method then calculates 
        the proportion by dividing the number of rows that meet the condition by the total number 
        of rows in the dataframe. The resulting proportion is then returned.
        """
        condition = (self.df['carat'] > 0.30) & (self.df['carat'] < 1.08)
        proportion = len(self.df[condition]) / len(self.df)
        return proportion
    

    
    def task_two(self):
        """
     
         Question 2.
            The method identifies rows where the x and y columns (representing dimensions) 
            have equal values. It counts the number of such rows and returns this count, representing 
            diamonds with equal x and y dimensions.
        """
        equal_dimensions = len(self.df[self.df['x'] == self.df['y']])
        return equal_dimensions
    


    def task_three(self):
        """
        Question 3.
        The method calculates the mean carat value of all diamonds and then identifies 
        those diamonds with a carat value less than this mean. It counts and returns the number 
        of such diamonds.
        """
        mean_carat = self.df['carat'].mean()
        less_than_mean = len(self.df[self.df['carat'] < mean_carat])
        return less_than_mean
    
    
    
    def task_four(self):
        """
         Question 4.
        This method counts and returns the number of diamonds that have either a 'Premium' 
        or 'Ideal' cut, as per the classifications available in the dataframe.
        """
        premium_or_better = len(self.df[self.df['cut'].isin(['Premium', 'Ideal'])])
        return premium_or_better
    
        

    def task_five(self):
        """
        Question 5.
        Calculates the price per carat for each diamond and identifies the diamond with 
        the highest price per carat value. Returns the details of this diamond.
        """
        self.df['price_per_carat'] = self.df['price'] / self.df['carat']
        max_ppc_index = self.df['price_per_carat'].idxmax()
        max_diamond = self.df.loc[max_ppc_index]
        return max_diamond
    
        

    def task_six(self):
        """
        Question 6.
        Creates and displays a bar plot that visualizes the frequencies of the different 
        categories of the 'cut' attribute within the dataset.
        """
        sns.countplot(data=self.df, x='cut', order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        plt.title('Frequency of Diamonds for Each Cut')
        plt.xlabel('Cut')
        plt.ylabel('Frequency')
        plt.show()
        
        
        
    def task_seven(self):
        """
        Creates boxplots of the diamond price for each cut.
        This helps visualize the distribution of prices for each cut.
        """
        sns.boxplot(data=self.df, x='cut', y='price', order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        plt.title('Boxplot of Diamond Prices for Each Cut')
        plt.xlabel('Cut')
        plt.ylabel('Price')
        plt.show()
        
    def task_eight(self):
        """
        Creates histograms of the length, width, depth, and total depth attributes.
        This helps visualize the distribution of these attributes.
        """
        attributes = ['x', 'y', 'z', 'depth']
        for attribute in attributes:
            sns.histplot(self.df[attribute], bins=30, kde=True)
            plt.title(f'Histogram of {attribute}')
            plt.xlabel(attribute)
            plt.ylabel('Frequency')
            plt.show()
            
    def task_nine(self):
        """
        Creates a scatter plot of price vs. carat.
        This helps visualize the relationship between price and carat.
        """
        sns.scatterplot(data=self.df, x='carat', y='price')
        plt.title('Scatter Plot of Price vs. Carat')
        plt.xlabel('Carat')
        plt.ylabel('Price')
        plt.show()



# In[69]:



# The URL to GitHub CSV file
data_path = "https://raw.githubusercontent.com/somyasingh98/Assignment-5/main/diamonds.csv"

diamonds = DiamondsAnalysis(data_path)


# In[70]:


# TASK 1
proportion = diamonds.task_one()
print(f"Proportion of diamonds between .30 and 1.08 carats: {proportion}")


# In[71]:


# Task Two
equal_dimensions_count = diamonds.task_two()
print(f"Number of diamonds with equal x and y dimensions: {equal_dimensions_count}")


# In[72]:


# TASK 3
less_than_mean_count = diamonds.task_three()
print(f"Number of diamonds with a carat less than the mean carat value: {less_than_mean_count}")


# In[73]:


# TASK 4
premium_or_better_count = diamonds.task_four()
print(f"Number of diamonds with a Premium cut or better: {premium_or_better_count}")


# In[74]:


# TASK 5
highest_ppc_diamond = diamonds.task_five()
print("Diamond with the highest price per carat:")
print(highest_ppc_diamond)


# In[75]:


# Task Six
print("Displaying bar plot of the 'cut' data:")
diamonds.task_six()  


# In[76]:


# Task Seven
print("Displaying boxplots of the diamond price for each cut:")
diamonds.task_seven()


# In[77]:


# Task Eight
print("Displaying histograms of the length, width, depth, and total depth attributes:")
diamonds.task_eight()  


# In[78]:


# Task Nine
print("Displaying scatter plot of price vs. carat:")
diamonds.task_nine()  


# In[ ]:




