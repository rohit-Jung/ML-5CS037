KNN algorithm
1. Clean the data, impute it and separate X(feature matrix) and y(label vector)
2. Splitting the data (X_train, y_train, split_size, seed)
    - set the seed, make an indices array, shuffle the array,
    - take how many point lies in array, divide the indices and 
    - return accordingly
3. Euclidean distance (p1, p2) - check for dimension and return acc.
4. KNN Single Predict - prediction for single query in dataset
    - (queryPoint, X_train, y_train, k)
    - with every point in X_train distance is calculated
    - the indices of distance are sorted according to the distance(np.argsort)
    - take the indices up to kth and find the label of that kth indices
    - take majority out from the labels selected (bincount and argmax)
5. KNN multi predict - prediction for every point in test data
    - (X_test, X_train, y_train, k)
    - for every point predict the values using KNN single predict
6. testing accuracy - comparing the y_true and y_test
    - calculate no. of true predictions (sum ( y_true == y_test))
    - calc. percentages return them
7. For multiple values of k 
    - take x_test, x_train, y_test, y_train , k 
        - for every k in k_values, predict using multi_predict
        - compute accuracy 
        - display the result 
    