
from sklearn.base import BaseEstimator, TransformerMixin


class NumericalImputer(BaseEstimator, TransformerMixin):
    """
    Custom scikit-learn transformer to impute missing values in numerical variables.

    Parameters:
        variables (list or str, optional): List of column names (variables) to impute missing values for.
            If a single string is provided, it will be treated as a single variable. Default is None.

    Attributes:
        variables (list): List of column names (variables) to impute missing values for.
        median_dict_ (dict): Dictionary to store the median values for each specified numerical variable during fitting.

    Methods:
        fit(X, y=None):
            Calculates the median values for the specified numerical variables from the training data.
            It returns the transformer instance itself.

        transform(X):
            Imputes missing values in the specified numerical variables using the median values and returns the modified DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Instantiate the custom transformer
    imputer = NumericalImputer(variables=['age', 'income'])

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('imputer', imputer),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """

    def __init__(self, variables=None):
        """
        Initialize the NumericalImputer transformer.

        Parameters:
            variables (list or str, optional): List of column names (variables) to impute missing values for.
                If a single string is provided, it will be treated as a single variable. Default is None.
        """
        self.variables = [variables] if not isinstance(
            variables, list) else variables

    def fit(self, X, y=None):
        """
        Calculates the median values for the specified numerical variables from the training data.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            self (NumericalImputer): The transformer instance.
        """
        self.median_dict = {}
        for var in self.variables:
            self.median_dict[var] = X[var].mean()
        print(self.median_dict)
        return self

    def transform(self, X):
        """
        Imputes missing values in the specified numerical variables using the median values and returns the modified DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_transformed (pd.DataFrame): Transformed DataFrame with missing values imputed for the specified numerical variables.
        """
        X = X.copy()
        for var in self.variables:
            X[var] = X[var].fillna(self.median_dict[var])
        return X


class FeatureSelector(BaseEstimator, TransformerMixin):
    """
    Custom scikit-learn transformer to select specific features (columns) from a DataFrame.

    Parameters:
        feature_names (list or array-like): List of column names to select as features from the input DataFrame.

    Methods:
        fit(X, y=None):
            Placeholder method that returns the transformer instance itself.

        transform(X):
            Selects and returns the specified features (columns) from the input DataFrame.

    Example usage:
    ```
    from sklearn.pipeline import Pipeline

    # Define the feature names to be selected
    selected_features = ['feature1', 'feature2', 'feature3']

    # Instantiate the custom transformer
    feature_selector = FeatureSelector(feature_names=selected_features)

    # Define the pipeline with the custom transformer
    pipeline = Pipeline([
        ('feature_selector', feature_selector),
        # Other pipeline steps...
    ])

    # Fit and transform the data using the pipeline
    X_transformed = pipeline.fit_transform(X)
    ```
    """

    def __init__(self, feature_names):
        """
        Initialize the FeatureSelector transformer.

        Parameters:
            feature_names (list or array-like): List of column names to select as features from the input DataFrame.
        """
        self.feature_names = feature_names

    def fit(self, X, y=None):
        """
        Placeholder method that returns the transformer instance itself.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            self (FeatureSelector): The transformer instance.
        """
        return self

    def transform(self, X):
        """
        Selects and returns the specified features (columns) from the input DataFrame.

        Parameters:
            X (pd.DataFrame): Input data to be transformed.

        Returns:
            X_selected (pd.DataFrame): DataFrame containing only the specified features (columns).
        """
        return X[self.feature_names]
