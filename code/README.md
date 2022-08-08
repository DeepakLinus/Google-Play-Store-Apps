
<h1>Library Setup and Read in the Data</h1>
  <h5>You will need to install additional libraries</H5>
  <h3> The exploratory visualization of missing data
  <h1>Downloading the dataset
<h5>using opendatsets
  What is Your Kaggle username:
and Your kaggle Key:
<h1>Data Preparation<h1>
<h5>Load the csv file with the pandas
  Viewing the first 10 rows of the datset
  Viewing the columns were given in the Google-Playstore dataset
  Shape of the dataset
  <H1>Basic Exploration<H1>
<h5> We will start with basic exploration of the dataset and get a feel for how it looks<h5>

There are 23 columns and several of them have missing values. I like creating a single cell to list all the issues that need addressing and deal with them separately after I am done exploring. Then, I can cross each issue one by one as I fix them.
  I like the columns of my dataset to have snake_case because it will be easier to choose them later on (added to the list).

Also, I think these columns will not be useful for us: App ID, minimum installs, maximum installs, minimum android version, developer ID, developer website,developer email, privacy policy link.

There are 23 columns and several of them have missing values:

Sorted data in ascending order.
  <h2>Now, let's look at the app categories:
    If we look carefully, some categories of interest like Music and Eduction are given with different labels: there are both 'Music & Audio' and 'Music' labels as well as 'Education' and 'Educational' for education. They should be merged together to represent a single category.
    Descriptive statistics

Display in normal notation instead of scientific,

The numerical features of the dataset and see if they contain any issues.
    Looks like all numerical columns are within the sensible range, like rating should be between 0 and 5. But the maximum value for price is 400$ which is a bit suspicious. We will dig into that later.

Before we further explore, let's deal with the issues we highlighted. Here is the final list:

Issues List For the Dataset

Missing values in several cols: Rating, rating count, Installs, minimum and maximum installs, currency and more
Convert all columns to snake_case
Drop these columns: App ID, minimum and maximum installs, minimum android version, developer ID, website and email, privacy policy link.
Incorrect data types for release data and size
Music and education is represented by different labels
Drop unnecessary categories
    <h1>Data Cleaning</h1>
It is a good practice to start cleaning from the easiest issues.
    Drop unnecessary columns
    Collapse multiple categories into one
    Subset only for top 10 categories
    Convert released to datetime

Specifying the datetime format significantly reduces conversion time
    Convert size to float

Strip of all text and convert to numeric
    Deal With Missing Values

There seems to be much more missing values in size, well over the threshold where we can safely drop them. Let's dive deeper using the missingno package:
    ![image](https://user-images.githubusercontent.com/103175339/183484384-d936e1d4-d0bd-4a33-bdbd-980076c2a976.png)
Plotting the data sorted by category tells that nulls in size are randomly scattered. Let's plot the missingness correlation:

Also called plot the missing null values.
    ![image](https://user-images.githubusercontent.com/103175339/183484529-295cb48e-1829-44b1-94e1-9e6fedcc7c7b.png)
    The correlation matrix of missingness shows that most nulls in size are associated with nulls in rating and rating_count. This scenario falls into the Missing At Random class of missingness. This means that even though null values are random their misssingness is related to other observed values.

In most cases, you can impute them with ML techniques. But our case is specific because we don't have enough features that help predict the size or rating of an app. We have no choice but to drop them. (I am not even mentioning nulls in other columns because their proportion is marginal)

<H1>Univariate Exploration<H1>
Finally, time to create some plots. Specifically, we will look at the distribution of the numerical features of the dataset.

Let's start with rating:
  ![image](https://user-images.githubusercontent.com/103175339/183484702-a091ed52-1259-4b11-becb-555cec34ea59.png)
  It looks like, there are much more apps with no rating. We might get a better visual if omit them:
  ![image](https://user-images.githubusercontent.com/103175339/183484808-9e3df946-3326-453a-a248-b27adb436243.png)
Histogram shows that majority of the apps are rated between ~3.8 and 4.8. It is also surprising to see so many 5-star ratings

All Categories Rating

The higest rated Category
  ![image](https://user-images.githubusercontent.com/103175339/183484923-1c8ca77e-8f41-48fc-b86f-00bce111aa1a.png)
From the above plot we can see that Role Playing is the highest Rated category.

Now, let's look at how categories are distributed:
  ![image](https://user-images.githubusercontent.com/103175339/183485034-eb22f0ae-a363-40ec-90a8-04721978100a.png)
Looks like educational apps make up more than one fifth of the data.

It would be ideal if we had the install_count given as integers. But they are collapsed into categories which makes it impossible to see their distribution as a numeric feature. We got no other choice but to plot them in the same way as above:
  ![image](https://user-images.githubusercontent.com/103175339/183485263-1fa78749-9f4e-4f22-bcde-85d483f8f44e.png)

  The plot shows that the vast majority of installs are between 10 and 10k installs. Maybe, we could get a better insight if we plotted rating_count. The number of ratings is given as exact figures and logically, they are positively related to install count. Before plotting, let's get the 5-number-summary of rating_count:
  WOW! From the summary we can see that 75% of the distribution is less than 31 while the max is over 3.5 million. So, we will only plot the apps with ratings <32:
  ![image](https://user-images.githubusercontent.com/103175339/183485471-fed2cea9-a4fe-4a95-940c-8d067b89bb61.png)

This histogram tells us that about a quarter of the apps have no more than 5 ratings. This shows how competetive the mobile market is. Only a small proportion of apps can go as popular as the ones with thousands of ratings. Just for curiosity, let's explore the apps that have more than 3 million ratings:

Which Category has the highest Paid and Free apps ?

Create a mask for paid apps
    Again, price also contains some serious outliers. For best insights, we subset for apps that cost less than 15$
    ![image](https://user-images.githubusercontent.com/103175339/183485622-9181ba02-9955-4516-bffc-3a73c101f4a7.png)


