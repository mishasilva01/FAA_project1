# FAA_project1

To start, we can devide the dataset according to categorical and interger features.
Integer:
  1. age
  2. trestbps (resting blood pressure)
  3. chol (serum cholestoral)
  4. thalach (maximum heart rate achieved)
  5. oldpeak (ST depression induced by exercise relative to rest)
  6. ca (number of major vessels (0-3) colored by flourosopy) - HAS NAN VALUES
  7. num (diagnosis of heart disease)

Dealing with NaN:
  Since from our 303 observations we only have 5 observations, one way to deal with NaN values could be just *removing* those observations
